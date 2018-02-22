
from conf_types import *
from conf_misc  import *
import abc
import collections
import html
import io
import sys
import textwrap
import typing
import types

__all__ = [
  'HTML',
  'print_program',
  'slice_per_day',
]

## HTML non breaking space
NBSP = "\u00A0"


def print_program(program: Program, dst: typing.IO[str] = sys.stdout, *,
                  show_people: bool, font_size: int, full_page: bool,
                  time_column: bool, honour_page_breakers: bool):
  """
    print HTML for program to stream.

    Parameters:
      :show_people         show names of people associated with a talk in the table.
      :font_size           font size to use (in pt)
      :full_page           whether to generate a standalone page or just a embeddable <div>
      :honour_page_breakers whether to split tables & insert page breaks after joint events
                           with 'page_breaker=True'
  """

  h = HTML(dst)

  if full_page:
    h.print_page_header()

  h.print_program_header(font_size=font_size)

  for day in slice_per_day(program):
    h.print_day(day, show_people=show_people, time_column=time_column,
                honour_page_breakers=honour_page_breakers)

  h.print_program_footer()

  if full_page:
    h.print_page_footer()


class HTML:
  def __init__(self, dst: typing.IO[str] = sys.stdout):
    self._writer = HTML_Writer(dst)

  def print_page_header(self):
    h = self._writer

    h.html('<!DOCTYPE html>')
    h.open('html')
    h.open('head')
    h.open('title')
    h.text('HPCA/CGO/PPoPP/CC 2018 Program Schedule (Fed 24-28, 2018), Vienna, Austria')
    h.close('title')
    h.close('head')
    h.open('body')

  def print_page_footer(self):
    h = self._writer

    h.close('body')
    h.close('html')

  def print_program_header(self, *, font_size: int):
    h = self._writer

    h.open('div', id="conf_program")
    self.print_style(font_size=font_size)

  def print_program_footer(self):
    h = self._writer

    h.close('div', comment='id="conf_program"')

  def print_style(self, *, font_size: int):
    h = self._writer

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

        .page-break {{
          page-break-after: always;
        }}
      }}
    ''')
    h.close('style')
    h.html('<!-- enable Google fonts "Ubuntu" font -->')
    h.tag('link', href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet")

  def print_header(self, txt):
    h = self._writer

    h.open('h2')
    h.text(txt)
    h.close('h2')

  def print_day(self, day, *, show_people: bool, time_column: bool,
                honour_page_breakers: bool):
    """
      print HTML table for one day.

      params:
        :day  a Program for one day
        flag args have same meaning as in print_program()
    """

    assert len(list(day.conferences)), [s.title for s in day.joint_events]
    assert len(list(day.sessions)) or len(list(day.joint_events))

    h = self._writer

    def _render_session(program: Program, conf: Conference, sessions: typing.List[Session],
                        num_cols: int) -> typing.Iterable[None]:
      """
        generator that prints <td> elements for one row every time you call next on it.
        When done with its main content it just emits empty <td>s forever
      """

      assert num_cols > 1
      assert len(sessions)

      if time_column:
        num_cols -= 1
        left_border = ''
      else:
        left_border = 'border-left'

      for session in sessions:
        events = list(program.session_events(session))

        assert events

        ## session time, room

        if time_column:
          ## time gets one column, room name is put in the remaining columns
          top_border = 'border-top'

          h.open('td', f'class="{conf.name} border-left {top_border} time"')
          h.text(time_range_str(session.start, session.end))
          h.close('td')

          h.open('td', f'class="{conf.name} {left_border} border-right {top_border}"', colspan = num_cols)
          if session.room:
            h.text('Room:', NBSP.join(session.room.split()))
          h.close('td')
          yield True
        else:
          ## time and room share all available columns (separete by NBSP to avoid ugly line break)
          top_border = ''

          h.open('td', f'class="{conf.name} {left_border} border-right border-top"', colspan = num_cols)
          text = time_range_str(session.start, session.end)
          if session.room:
            text += NBSP + 'Room:' + NBSP + NBSP.join(session.room.split())
          h.text(text)
          h.close('td')
          yield True

        ## session name

        if time_column:
          h.html(f'<td class="{conf.name} border-left"></td>')

        h.open('td', f'class="{conf.name} {left_border} border-right"', colspan = num_cols)

        if session.link:
          h.open('a', f'href="{session.link}"')
        if session.title:
          h.text(session.title)
        if session.link:
          h.close('a')

        h.close('td')
        yield True

        ## session chair

        if session.chair:
          if time_column:
            h.html(f'<td class="{conf.name} border-left"></td>')

          h.open('td', f'class="{conf.name} {left_border} border-right"', colspan = num_cols)
          h.text('Session chair:', session.chair)
          h.close('td')
          yield True

        ## session events

        last_event = events[-1]

        for event in events:
          if time_column:
            h.html(f'<td class="{conf.name} border-left"></td>')

          h.open('td', f'class="{conf.name} {left_border} border-right"', colspan = num_cols)

          if event.link:
            h.open('a', f'href="{event.link}"')
          h.open('strong')
          h.text(event.title)
          h.close('strong')
          if event.link:
            h.close('a')
          if (show_people or event.important_people) and event.people:
            h.html('<br>')
            h.html(event.people)
          h.close('td')
          yield True

      ## padding (when other sessions have more events)
      while True:
        if time_column:
          h.html(f'<td class="{conf.name} border-left"></td>')

        h.html(f'<td class="{conf.name} {left_border} border-right" colspan="{num_cols}"></td>')
        yield False

    num_cols, cols_per_conf = compute_table_columns(day)

    date = next(iter(day.sessions)).day
    self.print_header(day_str(date))

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

              assert (cols_per_conf[c] // len(tracks)) == (cols_per_conf[c] / len(tracks))

              # FIXME: All sessions for one conference between two joint events currently
              #        have to have the same number of tracks.
              #        If we want different numbers of tracks per conf we need to possibly
              #        remerge after the conf split into two tracks.
              #        Example:
              #         | HPCA-A | HPCA-B |
              #         | HPCA closing    |
              #        Need to merge tracks for HPCA closing.
              sessions = program.track_sessions(track)
              session  = next(iter(sessions))
              num_rows = max(num_rows, 1 + sum([len(list(program.session_events(s))) for s in sessions]))

              renderers.append(_render_session(program, c, sessions, cols_per_track))
          else:
            renderers.append(_render_session(program, c, [], cols_per_conf[c]))

        assert num_rows > 0, 'slice with no events??'

        while True:
          clss = ''

          has_more = False

          h.open('tr', f'class="{clss}"')
          for r in renderers:
            has_more |= next(r)
          h.close('tr')

          if not has_more:
            h.open('tr', f'class="border-bottom"')
            h.close('tr')
            break

      if joint and joint.title:
        h.open('tr', 'class="border-left border-top border-right border-bottom"', comment='joint')

        assert num_cols > 1

        if time_column:
          cols = num_cols - 1
        else:
          cols = num_cols

        if joint.title:
          if time_column:
            h.open('td', 'class="time"')
            h.text(time_range_str(joint.start, joint.end))
            h.close('td')

          h.open('td', f'colspan="{cols}"')
          if not time_column:
            h.text(time_range_str(joint.start, joint.end))
            h.html('&nbsp;')

          if joint.room:
            h.html('&nbsp;')
            h.text('(' + joint.room + ')')

          if joint.title:
            if joint.link:
              h.open('a', f'href="{joint.link}"')
            h.open('strong')
            h.text(joint.title)
            h.close('strong')
            if joint.link:
              h.close('a')
          if (show_people or joint.important_people) and joint.people:
            h.text(NBSP, joint.people)
          h.close('td')
          h.close('tr')
        else:
          h.open('td', colspan=cols)
          h.close('td')

        if honour_page_breakers and joint.page_breaker:
          h.open('tr')
          h.open('td', "class='border-top'", colspan=num_cols)
          h.close('td')
          h.close('tr')
          h.close('tbody')
          h.close('table')
          self.page_break()
          h.open('table')
          h.open('tbody')

    h.open('tr', f'class="border-top"')
    h.open('td', colspan=num_cols)
    h.close('td')
    h.close('tr')

    h.close('tbody')
    h.close('table')
    self.page_break()

  def tag(self, tag, *attrs, comment = None, **kwargs):
    return self._writer.tag(tag, *attrs, comment=comment, **kwargs)

  def page_break(self):
    self._writer.tag('p', 'class="page-break"')


class HTML_Writer:
  """
    small helper for printing HTML_Writer
  """

  def __init__(self, dst, initial_indent: int = 0):
    self.lvl = initial_indent
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
    """
      Print HTML open tag <xoxo>
    """

    assert tag

    # print('BGN' + '  ' * self.lvl, tag)

    self.tag(tag, *attrs, comment=comment, **kwattrs)
    self.lvl += 2

    # validation
    self.tag_stack.append(tag)

  def close(self, tag, comment = ''):
    """
      Print HTML open tag </xoxo>
    """

    assert tag

    # print('END' + '  ' * (self.lvl - 2), tag)

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

  def tag(self, tag, *attrs, comment = None, **kwattrs):
    """
      Print HTML tag that needs no closing tag <xoxo>
    """

    assert tag

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

  assert len(list(program.conferences)), 'program has no conferences'
  assert len(list(program.sessions) + list(program.joint_events)), 'program has no events'

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

    assert len(list(slice.conferences)), f'day {day}, {[s.title for c in program.sessions]}'
    assert len(list(slice.sessions) + list(slice.joint_events)), 'program has no events'

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


def compute_table_columns(program) -> typing.Tuple[int, typing.Dict[Conference, int]]:
  """
    calculate how many columns each conference should get in the big program table.
    Each track needs at least two columns (first column is time, rest is program)
    Since a conf can have different number of active tracks per day we do some magic.

    returns tuple:
      total num columns
      num columns per conference
  """

  assert len(list(program.conferences)), 'program has no conferences'
  assert len(list(program.sessions) + list(program.joint_events)), 'program has no events'

  def safe_div(a, b):
    assert int(a / b) == a // b, f'bad div {a!r} / {b!r}'
    return a // b

  num_conferences = len(program.conferences)

  # every track gets at least two columns
  track_min_cols = 2

  ## compute number of columns per conference

  cols_per_conf = {
    c: track_min_cols * len(program.conference_tracks(c))
    for c in program.conferences
  }

  for subprogram, _ in slice_by_joint_events(program):
    # skip trailing empty program
    if not subprogram.conferences:
      continue

    for conf in subprogram.conferences:
      num_tracks          = len(subprogram.conference_tracks(conf)) * track_min_cols
      cols_per_conf[conf] = least_common_multiple(cols_per_conf[conf], num_tracks)

  cols_per_conf = types.MappingProxyType(cols_per_conf)

  ## compute total number of columns for table

  num_cols = sum(cols_per_conf.values())

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
    return f'[{time_str(start)}{NBSP}-{NBSP}{time_str(end)}]'
  else:
    return f'[{time_str(start)}]'
