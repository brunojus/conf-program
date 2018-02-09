
from conf_misc import *
import datetime
import typing
from typing import *

__all__ = [
  'Program',
  'Conference',
  'Track',
  'Session',
  'Event',
  'Joint_Event',

  'Session_Builder',
  'Event_Builder',
  'Joint_Event_Builder',

  'datetime',
]


################################################################################
## types for Conference, Track, Session, Event, ...

class Struct_Meta(type):
  """
    Meta class for Struct objects.
    Injects __slots__ and __init__ built from _fields list.
  """

  def __new__(clss, clss_name, super_classes, namespace):
    if super_classes:
      assert super_classes == (Struct,), 'inheritance nope'

    fields = namespace.setdefault('_fields', ())

    ## inject __slots__ generated from fields

    assert '__slots__' not in namespace

    namespace['__slots__'] = tuple(f[0] for f in fields)

    ## inject __init__ method generated from fields

    assert '__init__' not in namespace

    init_name = f'{clss_name}__init__'
    init_args = ['self']
    init_help = []
    init_body = ''

    locals_  = {}
    globals_ = dict(globals())

    for field in fields:
      assert type(field) is tuple
      assert len(field) in (2, 3)

      field_name = field[0]
      field_type = field[1]

      assert field_name.isidentifier()

      ty_var  = f"_{field_name}_ty"

      assert ty_var not in globals_, f'duplicate arg {field_name!r}'

      globals_[ty_var] = field_type

      arg = f'{field_name}: {ty_var}'

      if len(field) == 3:
        field_default = field[2]

        def_var = f"_{field_name}_default"

        globals_[def_var] = field_default

        arg += f' = {def_var}'

      init_args.append(arg)
      init_help.append(f'{field_name}: {typing._type_repr(field_type)}')

      init_body += f'  self._set_field({field_name!r}, {ty_var}, {field_name})\n'

    init_body += '\n  self._post_init()\n'

    init_signature = f'def {init_name}({", ".join(init_args)}):\n'
    init_help      = f'  """{clss_name}({", ".join(init_help)})"""\n\n'

    init_code = init_signature + init_help + init_body + '\n'

    # print(init_code)
    exec(init_code, globals_, locals_)

    namespace['__init__'] = locals_[init_name]

    return type.__new__(clss, clss_name, super_classes, namespace)


class Struct(metaclass=Struct_Meta):
  def _post_init(self):
    """
      called at the end of __init__, override if needed.
    """
    pass

  def __setattr__(self, attr, value):
    raise AttributeError(f"nope, won't let you set {attr} on {type(self).__name__}@{id(self)}")

  def _init_from_dict(self, kwargs: Dict[str, object]):
    print('!', self._fields)

    for field_name, field_type in self._fields:
      arg = kwargs.pop(field_name)

      self._set_field(field_name, field_type, arg)

    if kwargs:
      raise ValueError(f'{type(self).__name__}: too many ctor arguments')

  def _set_field(self, attr, ty, value):
    if not type_check(value, ty):
      raise TypeError(f'cannot set {type(self).__name__}.{attr} to {value!r}, want a {typing._type_repr(ty)}')

    if hasattr(self, attr):
      raise TypeError(f'cannot set {type(self).__name__}.{attr}, already set')

    object.__setattr__(self, attr, value)

  def _field_tuple(self):
    return tuple(getattr(self, f) for f in self.__slots__)

  def __hash__(self):
    return hash(self._field_tuple())

  def __eq__(self, that):
    if type(self) != type(that):
      return False
    return self._field_tuple() == that._field_tuple()

  def __str__(self):
    return f'{type(self).__name__}(...)'

  def __repr__(self):
    txt = ''
    txt += type(self).__name__
    txt += '('
    txt += ', '.join(map(str, self._field_tuple()))
    txt += ')'
    return txt


class Conference(Struct):
  _fields = (('name', str),)


class Track(Struct):
  _fields = (('id', str),)


class Session(Struct):
  _fields = (
    ('track', Track),
    ('start', datetime.datetime),
    ('end',   Optional[datetime.datetime], None),
    ('title', Optional[str], None),
    ('link',  Optional[str], None),
    ('room',  Optional[str], None),
    ('chair', Optional[str], None),
  )

  def _post_init(self):
    assert not self.link or self.title

  @property
  def day(self):
    return self.start.date()


class Event(Struct):
  _fields = (
    ('title',            str),
    ('session',          Session),
    ('people',           Optional[str], None),
    ('link',             Optional[str], None),
    ('start',            Optional[datetime.datetime], None),
    ('end',              Optional[datetime.datetime], None),
    ('important_people', bool, False),
  )

  def _post_init(self):
    assert not self.link or self.title

    assert (self.start is None) or (self.start >= self.session.start)
    assert (self.end   is None) or (self.end   <= self.session.end)

    assert (self.start is None and self.end is None) or (self.start < self.end)

    assert not self.important_people or self.people

  @property
  def day(self):
    if self.start:
      return self.start.date()
    return None


class Joint_Event(Struct):
  _fields = (
    ('start',            datetime.datetime),
    ('title',            Optional[str], None),
    ('end',              Optional[datetime.datetime], None),
    ('link',             Optional[str], None),
    ('people',           Optional[str], None),
    ('room',             Optional[str], None),
    ('important_people', bool, False),
  )

  def _post_init(self):
    assert not self.link or not self.people or self.title

    assert (self.end is None) or (self.start < self.end)

    assert not self.important_people or self.people

  @property
  def day(self):
    return self.start.date()


################################################################################
## builer APIs

class Track_Builder:
  def __init__(self, *, sessions = (), **fields):
    self.sessions = sessions or []
    self.fields   = fields

  def session(self, **kwargs):
    sess = Session_Builder(**kwargs)
    self.sessions.append(sess)
    return sess

  def build(self, program, conference: Conference) -> Track:
    track = program.add_track(conference)

    for sess in self.sessions:
      if type(sess) is not Session_Builder:
        raise TypeError(f'wanted an Event, got a {type(sess).__name__}')

      sess.build(program, track)

    return sess


class Session_Builder:
  def __init__(self, *, events = (), **fields):
    self.events  = events or []
    self.fields  = fields

  def event(self, **kwargs):
    evt = Event_Builder(**kwargs)
    self.events.append(evt)
    return evt

  def build(self, program, track: Track) -> Session:
    sess = Session(track=track, **self.fields)
    program._add_session(sess)

    for evt in self.events:
      if type(evt) is not Event_Builder:
        raise TypeError(f'wanted an Event, got a {type(evt).__name__}')

      evt.build(program, sess)

    return sess


class Event_Builder:
  def __init__(self, **fields):
    self.fields = fields

  def build(self, program, session: Session) -> Event:
    fields = dict(self.fields)

    fields['people'] = ', '.join(fields.get('people', []))

    evt = Event(session=session, **fields)
    program._add_event(evt)
    return evt


class Joint_Event_Builder:
  def __init__(self, **fields):
    self.fields = fields

  def build(self, program) -> Joint_Event:
    fields = dict(self.fields)

    fields['people'] = ', '.join(fields.get('people', []))

    evt = Joint_Event(**fields)
    program._add_joint_event(evt)
    return evt


################################################################################
## conf program builder

class Program:
  def __init__(self, other: Optional['Program'] = None):
    """
      Copy conferences, tracks, events, ... from other conference or
      initialize empty.
      New conference will have same Conference, Event, Track, ... objects,
      but new internal lists, sets, ...
      So modifying one does not change the other
    """

    assert other is None or type(other) is Program

    def try_copy(val):
      if type(val) is dict:
        return {try_copy(kv[0]): try_copy(kv[1]) for kv in val.items()}
      if type(val) is set:
        return {try_copy(e) for e in val}
      if type(val) is str:
        return val
      if isinstance(val, Struct):
        return val
      if hasattr(val, 'copy'):
        return val.copy()

      raise TypeError(f"unsupported type {type(val).__name__}")

    def init(slot, ty):
      if other is None:
        val = type_instantiate(ty)
      else:
        val = getattr(other, slot)
        assert type_check(val, ty), f'expect {ty}, have {type(val)}'
        val = try_copy(val)

      setattr(self, slot, val)

    init('_conferences',  Dict[str, Conference])
    init('_tracks',       Dict[str, Track])
    init('_sessions',     List[Session])
    init('_events',       List[Event])
    init('_joint_events', List[Joint_Event])

    init('_conf_2_tracks',    Dict[Conference, List[Track]])
    init('_track_2_sessions', Dict[Track,      List[Session]])
    init('_session_2_events', Dict[Session,    List[Event]])

  ## builders

  def add_conference(self, title: str):
    try:
      return self._conferences[title]
    except KeyError:
      c = Conference(title)
      self._conferences[title] = c
      return c

  def add_track(self, conf: Conference):
    tracks = self._conf_2_tracks.setdefault(conf, [])
    track  = Track(id = f'{conf.name} {len(tracks) + 1}')

    self._tracks[track.id] = track
    tracks.append(track)

    return track

  def _add_session(self, session):
    assert type(session) is Session

    assert session not in self._sessions, f'session {session!r} created twice'
    self._sessions.append(session)

    self._track_2_sessions.setdefault(session.track, []).append(session)

    return session

  def _add_event(self, event):
    assert type(event) is Event, event

    assert event not in self._events, f'event {event!r} created twice'
    self._events.append(event)

    self._session_2_events.setdefault(event.session, []).append(event)

  def _add_joint_event(self, event):
    assert type(event) is Joint_Event, event

    assert event not in self._joint_events, f'joint event {event!r} created twice'

    self._joint_events.append(event)
    return event

  ## slicing

  def prune(self):
    """
      Remove Conferences, Tracks & Sessions with no events.
    """

    dead_sessions = []
    for s in self.sessions:
      assert type(s) is Session, repr(s)
      if not self.session_events(s):
        dead_sessions.append(s)

    for s in dead_sessions:
      self.remove_session(s)

    dead_tracks = []
    for t in self.tracks:
      if not self.track_sessions(t):
        dead_tracks.append(t)

    for t in dead_tracks:
      self.remove_track(t)

    dead_conferences = []
    for c in self.conferences:
      if not self.conference_tracks(c):
        dead_conferences.append(c)

    for c in dead_conferences:
      self.remove_conference(c)

    # prune orphan events that are in no session
    dead_events = list(self.events)
    for s in self.sessions:
      for e in self.session_events(s):
        try:
          dead_events.remove(e)
        except ValueError as v:
          print('?', s, e)
          # for de in dead_events:
          #   print('!', de)
          raise v

    for e in dead_events:
      self.remove_event(e)

  def slice(self, session_predicate, joint_event_predicate = None) -> 'Program':
    if joint_event_predicate is None:
      joint_event_predicate = session_predicate

    copy = Program(self)

    dead_sessions = []
    for s in copy.sessions:
      if not session_predicate(s):
        dead_sessions.append(s)

    for s in dead_sessions:
      copy.remove_session(s)

    dead_joint_events = []
    for j in copy.joint_events:
      if not joint_event_predicate(j):
        dead_joint_events.append(j)

    for je in dead_joint_events:
      copy.remove_joint_event(je)

    copy.prune()

    return copy

  def remove_conference(self, conf):
    self._conferences.pop(conf.name)
    for t in self._conf_2_tracks.pop(conf, ()):
      self.remove_track(t)

  def remove_track(self, track):
    assert type(track) is Track
    self._tracks.pop(track.id)

    for tracks in self._conf_2_tracks.values():
      if track in tracks:
        tracks.remove(track)

    for s in self._track_2_sessions.pop(track, ()):
      self.remove_session(s)

  def remove_session(self, session):
    assert type(session) is Session
    self._sessions.remove(session)

    for sessions in self._track_2_sessions.values():
      if session in sessions:
        sessions.remove(session)

    for e in self._session_2_events.pop(session, ()):
      self.remove_event(e)

  def remove_event(self, event):
    self._events.remove(event)

    for events in self._session_2_events.values():
      if event in events:
        events.remove(event)

  def remove_joint_event(self, event):
    assert type(event) is Joint_Event
    self._joint_events.remove(event)

  ## query

  @property
  def conferences(self):
    return self._conferences.values()

  @property
  def tracks(self):
    return self._tracks.values()

  @property
  def sessions(self):
    return iter(self._sessions)

  @property
  def events(self):
    return iter(self._events)

  @property
  def joint_events(self):
    return iter(self._joint_events)

  @property
  def people(self):
    return self._people.keys()

  def conference_tracks(self, conf):
    return self._conf_2_tracks.get(conf, ())

  def conference_sessions(self, conf):
    for t in self.conference_tracks(conf):
      yield from self.track_sessions(t)

  def track_sessions(self, track):
    return self._track_2_sessions.get(track, ())

  def session_events(self, session):
    return self._session_2_events.get(session, ())

