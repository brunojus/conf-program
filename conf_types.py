
from conf_misc import *
import datetime
import itertools
from typing import *

__all__ = [
  'Struct',
  'Program',
  'Conference',
  'Track',
  'Session',
  'Event',

  'datetime',
]


class Struct:
  def __setattr__(self, attr, value):
    raise AttributeError(f"nope, won't let you set {attr} on {type(self).__name__}@{id(self)}")

  def _set_field(self, attr, ty, value):
    if not hasattr(type(self), '_fields'):
      type(self)._fields = ()

    if attr not in self._fields:
      type(self)._fields += (attr,)

    if not type_check(value, ty):
      raise TypeError(f'cannot set {type(self).__name__}.{attr} to {value!r}, want a {ty.__name__}')

    if hasattr(self, attr):
      raise TypeError(f'cannot set {type(self).__name__}.{attr}, already set')

    object.__setattr__(self, attr, value)

  # def _xinit_from_dict(self, kwargs: Dict[str, object]):
  #   for field_name, field_type in self._fields:
  #     arg = kwargs.pop(field_name)

  #     self._set_field(field_name, field_type, arg)

  #   if kwargs:
  #     raise ValueError(f'{type(self).__name__}: too many ctor arguments')

  def _field_tuple(self):
    return tuple(getattr(self, f) for f in self._fields)

  def __hash__(self):
    return hash(self._field_tuple())

  def __eq__(self, that):
    if type(self) != type(that):
      return False
    return self._field_tuple() == that._field_tuple()

  def __repr__(self):
    txt = ''
    txt += type(self).__name__
    txt += '('
    txt += ', '.join(f'{f}: {getattr(self, f)!r}' for f in self._fields)
    txt += ')'
    return txt


class Conference(Struct):
  def __init__(self, name: str):
    self._set_field('name', str, name)


class Track(Struct):
  _fields = (('id', str))

  def __init__(self, **kwargs):
    print('1', kwargs)
    self._init_from_dict(self, kwargs)


class Session(Struct):
  def __init__(self, *, title, track, link,
               start: datetime.datetime, end,
               chair: Optional[str]):
    self._set_field('title', Optional[str], title)
    self._set_field('track', Track, track)
    self._set_field('link',  Optional[str], link)
    self._set_field('start', datetime.datetime, start)
    self._set_field('end',   Optional[datetime.datetime], end)
    self._set_field('chair', Optional[str], chair)

  @property
  def day(self):
    return self.start.date()


class Event(Struct):
  def __init__(self, title: str, link,
               start, end, people):
    self._set_field('title',  str, title)
    self._set_field('link',   Optional[str], link)
    self._set_field('start',  Optional[datetime.datetime], start)
    self._set_field('end',    Optional[datetime.datetime], end)
    self._set_field('people', str, people)

  @property
  def day(self):
    if self.start:
      return self.start.date()
    return None


class Joint_Event(Struct):
  def __init__(self, title: str, link: str,
               start: datetime.datetime, end, people):
    assert not link or title, f'Joint_Event has link ({link!r}), but no title'

    self._set_field('title',  str, title)
    self._set_field('link',   str, link)
    self._set_field('start',  datetime.datetime, start)
    self._set_field('end',    Optional[datetime.datetime], end)
    self._set_field('people', str, people)

  @property
  def day(self):
    return self.start.date()


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
      elif hasattr(val, 'copy'):
        return val.copy()
      else:
        return val

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
    track  = Track(f'{conf.name} {len(tracks) + 1}')

    self._tracks[track.id] = track
    tracks.append(track)

    return track

  def add_session(self, *, track, title = None, link = None, start, end = None, chair = None, events: List[Event] = ()):
    session = Session(title=title, track=track, link=link, start=start, end=end, chair=chair)

    assert session not in self._sessions, f'session {session!r} created twice'
    self._sessions.append(session)

    self._track_2_sessions.setdefault(track, []).append(session)

    for event in events:
      self._add_event_to_session(event, session)

    return session

  def add_event(self, title, link = None, start = None, end = None, people: List[str] = ()):
    people = self._format_people(people)

    event = Event(title, link, start, end, people)

    assert event not in self._events, f'event {event!r} created twice'
    self._events.append(event)

    return event

  def add_joint_event(self, *, title = '', link = '', start, end = None, people = ()):
    people = self._format_people(people)
    event  = Joint_Event(title, link, start, end, people)

    assert event not in self._joint_events, f'joint event {title!r} created twice'

    self._joint_events.append(event)
    return event

  def _format_people(self, people):
    if type(people) is str:
      return people
    else:
      return ', '.join(people)

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

  ## private parts

  def _add_event_to_session(self, event, session):
    assert type(event) is Event
    assert type(session) is Session
    assert (event.start is None) or (event.start >= session.start)
    assert (event.end   is None) or (event.end   <= session.end)

    self._session_2_events.setdefault(session, []).append(event)
