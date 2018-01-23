
from conf_types import *
from conf_misc  import *
import abc
import collections
import html
import sys
import textwrap
import typing

__all__ = [
  'print_HTML_table',
]


def print_HTML_table(program: Program, dst: typing.IO[str] = sys.stdout, *,
                     show_people: bool, font_size: int, full_page: bool):
  """
    print HTML for program to stream.

    Parameters:
      :show_people   show names of people associated with a talk in the table.
      :font_size     font size to use (in pt)
      :full_page     whether to generate a standalone page or just a embeddable <div>
  """

  days = slice_per_day(program)

  h = HTML_Writer(dst)

  if full_page:
    h.html('<!DOCTYPE html>')
    h.open('html')
    h.open('head')
    h.open('title')
    h.html('HPCA/CGO/PPoPP/CC 2018 Program Schedule (Fed 24-28, 2018), Vienna, Austria')
    h.close('title')
  h.open('style', 'type="text/css"')
  h.html(f'''\
  /*
    ! OVERRIDE bootstrap.theme.css used by conf.researchr !
  */

  /*
    Bootstrap limits the main element 'div.container' width.
    The width it chooses is too small for our table so we override it.
  */
  div.container {{
    width:   90%;
    margin: auto;
  }}

  /*
    bootstrap adds a gray top border to all cells, we have our own border stuff
  */
  td {{
    border-top: none;
  }}

  /*
    ! our own CSS !
  */

  div#conf_program {{
    font-family: 'Ubuntu', sans-serif;
  }}

  table {{
    width:           100%;
    font-size:       {font_size}pt;
    border-collapse: collapse;
  }}
  th {{
    border: 1px solid black;
  }}
  .border-left {{
    border-left: 1px solid black;
  }}
  .border-right {{
    border-right: 1px solid black;
  }}
  .border-top {{
    border-top: 1px solid black;
  }}
  .border-bottom {{
    border-bottom: 1px solid black;
  }}
  th, td {{
    padding: .5em;
  }}
  td.time {{
    white-space: nowrap;
  }}

  .HPCA {{
    background-color: #FFF2CC;
  }}
  .CGO {{
    background-color: #D9EBD3;
  }}
  .PPoPP {{
    background-color: #CFE2F3;
  }}
  .CC {{
    background-color: #c4afcf;
  }}

  /* help printing preserve colors */
  @media print {{
    body {{
      -webkit-print-color-adjust: exact; /*Chrome, Safari */
      color-adjust: exact; /*Firefox*/
    }}

    .HPCA {{
      background-color: #FFF2CC !important;
    }}
    .CGO {{
      background-color: #D9EBD3;
    }}
    .PPoPP {{
      background-color: #CFE2F3;
    }}
    .CC {{
      background-color: #c4afcf;
    }}
  }}
''')
  h.close('style')
  h.html('<!-- enable Google fonts "Ubuntu" font -->')
  h.html('<link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet">')

  if full_page:
    h.close('head')
    h.open('body')
  h.open('div', id="conf_program")

  def render_session(program: Program, conf: Conference, sessions: typing.List[Session],
                     num_cols: int, html: HTML_Writer) -> typing.Iterable[None]:
    for session in sessions:
      events = list(program.session_events(session))

      assert events

      ## session time & name

      html.open('td', f'class="{conf.name} border-left border-top time"')
      html.text(time_range_str(session.start, session.end))
      html.close('td')
      html.open('td', f'class="{conf.name} border-right border-top"', colspan = num_cols - 1)
      if session.link:
        html.open('a', f'href="{session.link}"')
      if session.title:
        html.html(session.title)
      if session.link:
        html.close('a')
      html.close('td')
      yield

      ## session events

      last_event = events[-1]

      for event in events:
        h.html(f'<td class="{conf.name} border-left"></td>')
        h.open('td', f'class="{conf.name} border-right"', colspan = num_cols - 1)
        if event.link:
          h.open('a', f'href="{event.link}"')
        h.open('strong')
        h.text(event.title)
        h.close('strong')
        if event.link:
          h.close('a')
        if show_people and event.people:
          h.html('<br>')
          h.html(event.people)
        h.close('td')
        yield

    ## padding (when other sessions have more events)
    while True:
      h.html(f'<td class="{conf.name} border-left"></td>')
      h.html(f'<td class="{conf.name} border-right" colspan="{num_cols - 1}"></td>')
      yield

  for day in days:
    assert day.sessions or day.joint_events

    num_cols, cols_per_conf = columns_per_conference(day)

    h.open('h3')
    date = next(iter(day.sessions)).day
    h.html(day_str(date))
    h.close('h3')
    h.open('table')

    h.open('thead')
    h.open('tr', comment='conf headers')

    for c in day.conferences:
      h.open('th', f'colspan="{cols_per_conf[c]}" class="{c.name}"')
      h.text(c.name)
      h.close('th')

    h.close('tr')
    h.close('thead')
    h.open('tbody')

    for program, joint in slice_by_joint_events(day):
      if len(list(program.events)):
        renderers = []
        num_rows  = 0

        for c in day.conferences:
          tracks = list(program.conference_tracks(c))

          if tracks:
            for track in tracks:
              cols_per_track = cols_per_conf[c] // len(tracks)

              # FIXME: we can currently only have one session per track between two joint events
              #        if we want more than one session per conf we need to possibly remerge
              #        after the conf split into two tracks.
              #        Example:
              #         | HPCA-A | HPCA-B |
              #         | HPCA closing    |
              #        Need to merge tracks for HPCA closing.
              sessions = program.track_sessions(track)
              assert len(sessions) == 1, \
                f'problem in track {track.id!r} {[s.title for s in sessions]!r} before {joint!r}'
              session = next(iter(sessions))

              num_rows = max(num_rows, 1 + sum([len(list(program.session_events(s))) for s in sessions]))

              renderers.append(render_session(program, c, sessions, cols_per_track, h))
          else:
            renderers.append(render_session(program, c, [], cols_per_conf[c], h))

        assert num_rows > 0, 'slice with no events??'

        for row in range(0, num_rows):
          if row == 0:
            # first row has a border to top
            clss = 'border-top'
          elif row == (num_rows - 1):
            # last row has a border to bottom
            clss = 'border-bottom'
          else:
            clss = ''

          h.open('tr', f'class="{clss}"')
          for r in renderers:
            next(r)
          h.close('tr')

      if joint:
        h.open('tr', 'class="border-left border-top border-right border-bottom"', comment='joint')
        h.open('td', 'class="time"')
        if joint.title:
          h.html(time_range_str(joint.start, joint.end))
        h.close('td')
        h.open('td', f'colspan="{num_cols - 1}"')
        if joint.link:
          h.open('a', f'href="{joint.link}"')
        h.open('strong')
        h.text(joint.title)
        h.close('strong')
        if joint.link:
          h.close('a')
        if joint.people:
          h.html('<br>')
          h.html(joint.people)
        h.close('td')
        h.close('tr')

    h.close('tbody')
    h.close('table')
    h.html('<p style="page-break-after: always;"></p>')

  h.close('div', comment='id="conf_program"')

  if full_page:
    h.close('body')
    h.close('html')

  return


class HTML_Writer:
  """
    small helper for printing HTML_Writer
  """

  def __init__(self, dst):
    self.lvl = 0
    self.dst = dst

    # validation
    self.tag_stack = []

  def html(self, *args):
    self.write_html_text(
      ' '.join(map(str, args)),
      self.dst,
      quote    = False,
      indent   = self.lvl,
      nl_to_br = False,
    )

  def text(self, *args, nl_to_br = False):
    self.write_html_text(
      ' '.join(map(str, args)),
      self.dst,
      quote    = True,
      indent   = self.lvl,
      nl_to_br = nl_to_br,
    )

  def open(self, tag, *attrs, comment = None, **kwattrs):
    txt = [
      # TODO: quote/validate
      tag,
      *attrs,
      *(f'{key}={repr(str(kwattrs[key]))}' for key in kwattrs)
    ]

    self.dst.write(' ' * self.lvl)
    self.dst.write('<' + ' '.join(txt) + '>')
    if comment:
      self.dst.write(f' <!-- {comment} -->')
    self.dst.write('\n')
    self.lvl += 2

    # validation
    self.tag_stack.append(tag)

  def close(self, tag, comment = ''):
    # validation
    assert self.tag_stack
    expected = self.tag_stack.pop()
    assert expected == tag, f"expected tag {expected!r}, got {tag!r}"

    self.lvl -= 2
    assert self.lvl >= 0

    self.dst.write(' ' * self.lvl)
    self.dst.write(f'</{tag}>')
    if comment:
      self.dst.write(f' <!-- {comment} -->')
    self.dst.write('\n')

  @staticmethod
  def write_html_text(txt, dst: typing.IO[str], *,
                      indent: typing.Optional[int], quote: bool, nl_to_br: bool):
    if quote:
      txt = html.escape(txt)
      txt = txt.replace('®', '&reg;')

    if indent is not None:
      txt = textwrap.dedent(txt)
      txt = textwrap.indent(txt, ' ' * indent)

    if nl_to_br:
      txt = txt.splitlines()
      joiner = '<br>\n' if self.nl_to_br else '\n'
      txt = joiner.join(txt)

    dst.write(txt)
    dst.write('\n')


def slice_per_day(program: Program) -> typing.List[Program]:
  """slice program into per day subprograms."""

  days: Set[datetime.date] = set()

  ## get list of days of conference
  for s in program.sessions:
    days.add(s.start.date())
  for s in program.joint_events:
    days.add(s.start.date())

  days = sorted(days)

  slices = []

  for day in days:
    slice = program.slice(lambda s: s.day == day)
    slices.append(slice)

  return slices


def slice_by_joint_events(program: Program) -> [(Program, typing.Optional[Event])]:
  """
    slice program into pairs (program only of sessions starting before joint event, joint event).
    The returned list is sorted by joint events.
    Only the last such pair will have a None joint event.
  """

  out = []

  joint_events = sorted(program.joint_events, key=lambda s: s.start)
  last_joint   = None

  # FIXME: broken if there are not joint events

  for joint in joint_events:
    before  = program.slice(lambda s: s.start <  joint.start)
    program = program.slice(lambda s: s.start >= joint.start)

    out.append((before, joint))

    last_joint = joint

  # list of events after last joint event
  if last_joint:
    last = program.slice(lambda s: s.start >= last_joint.start, lambda j: False)
  else:
    last = Program()

  out.append((last, None))

  return out


class HTML_AST(abc.ABC):
  @abc.abstractmethod
  def render(self, dst: HTML_Writer):
    ...


class HTML_Text(HTML_AST):
  """
    escaped HTML text
  """

  def __init__(self, txt, nl_to_br: bool):
    self.txt      = txt
    self.nl_to_br = nl_to_br

  def render(self, dst: HTML_Writer):
    dst.text(self.txt, nl_to_br = self.nl_to_br)


def columns_per_conference(program) -> typing.Tuple[int, typing.Dict[Conference, int]]:
  """
    calculate how many columns each conference should get in the big program table.
    Each track needs at least two columns (first column is time, rest is program)
    Since a conf can have different number of active tracks per day we do some magic.

    returns tuple:
      total num columns
      num columns per conference
  """

  def safe_div(a, b):
    assert int(a / b) == a // b, f'bad div {a!r} / {b!r}'
    return a // b

  num_conferences = len(program.conferences)

  ## compute total number of columns for table

  # at least one column per conference
  num_cols = num_conferences

  for subprogram, _ in slice_by_joint_events(program):
    # skip trailing empty program
    if not subprogram.conferences:
      continue

    # every track gets at least two columns
    currenty_active_tracks = len(subprogram.tracks) * 2

    num_cols = least_common_multiple(num_cols, currenty_active_tracks)

  ## compute number of columns per conference

  cols_per_conf = collections.Counter()

  max_active_tracks          = len(program.conferences)
  cols_per_track             = safe_div(num_cols, max_active_tracks)

  for subprogram, _ in slice_by_joint_events(program):
    # skip trailing empty program
    if not subprogram.conferences:
      continue

    currently_active_tracks = len(subprogram.tracks)

    if currently_active_tracks > max_active_tracks:
      cols_per_track = safe_div(num_cols, currently_active_tracks)

      for conf in subprogram.conferences:
        cols_per_conf[conf] = cols_per_track * len(subprogram.conference_tracks(conf))

  return num_cols, cols_per_conf


def day_str(date: datetime.date) -> str:
  day = date.day

  if 4 <= day <= 20 or 24 <= day <= 30:
      suffix = "th"
  else:
      suffix = ["st", "nd", "rd"][day % 10 - 1]

  return date.strftime('%A %B %d' + suffix + ', %Y')


def time_str(time: datetime.time) -> str:
  return time.strftime('%H:%M')


def time_range_str(start: datetime.time, end: datetime.time) -> str:
  assert start

  if end:
    return f'[{time_str(start)} - {time_str(end)}]'
  else:
    return f'[{time_str(start)}]'
