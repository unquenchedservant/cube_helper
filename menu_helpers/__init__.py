from math import ceil
import arithmetic
import curses


def center_scramble(stdscr, scramble):
    fake_str = " " * 20
    display_x = arithmetic.title_start(fake_str, stdscr.getmaxyx()[1])
    lines = ceil(len(scramble) / 20)
    display_y = arithmetic.scramble_start(lines, stdscr.getmaxyx()[0])
    total_lines = stdscr.getmaxyx()[0] - 1
    stdscr.attron(curses.color_pair(3))
    magic_y_end = 5 - lines
    stdscr.addstr(int(display_y) - 1, int(display_x) - 3, " " * 26)
    for x in range(0, magic_y_end):
        stdscr.addstr(int(display_y + lines + x), int(display_x) - 3, " " * 26)
        x += 1

    while lines != 0:
        cur_line_size = 20
        cur_line = scramble[:cur_line_size]
        if not (cur_line.endswith("'") or cur_line.endswith("2") or cur_line.endswith(" ")):
            cur_line_size = cur_line_size + 1
            cur_line = scramble[:cur_line_size]
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(int(display_y), display_x - 3, " " * 3)
        stdscr.addstr(int(display_y), display_x, cur_line.strip())
        magic_number = 23  - len(cur_line.strip())
        stdscr.addstr(int(display_y), display_x + len(cur_line.strip()), " "*magic_number)
        stdscr.attroff(curses.color_pair(3))
        scramble = scramble[cur_line_size:]
        lines -= 1
        display_y += 1


def title(stdscr, title_str):
    """
    title
    Creates a title for curses menus

    Parameters:
    stdscr - curses screen
    title - title string
    """
    display_x = arithmetic.title_start(title_str, stdscr.getmaxyx()[1])
    stdscr.attron(curses.color_pair(1))
    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(0, display_x, title_str)
    stdscr.attroff(curses.A_BOLD)
    stdscr.attroff(curses.color_pair(1))


def status_bar(stdscr, status_msg):
    """
    status_bar
    Creates the status bar on the bottom of curses screens

    Parameters:
    stdscr - curses screen
    status_msg - message to be displayed
    """
    display_y = stdscr.getmaxyx()[0] - 1
    magic_number = (stdscr.getmaxyx()[1] - len(status_msg) - 1)
    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(display_y, 0, status_msg)
    stdscr.addstr(display_y, len(status_msg), " " * magic_number)
    stdscr.attroff(curses.color_pair(3))


def add_option(stdscr, option, dis_y, dis_x, y_pos):
    """
    add_option (stdscr, string option, int dis_y, int dis_x, int y_pos)
    Adds option to menus

    Parameters:
    stdscr - curses screen
    option - string for menu_helpers option
    dis_y  - where the option should be placed on the y position
    dis_x  - where the option should be placed on the x position
    y_pos  - where the cursor currently is(for highlighting purposes)
    """
    if y_pos == dis_y:
        stdscr.attron(curses.color_pair(3))
    stdscr.addstr(dis_y, dis_x, option)
    if y_pos == dis_y:
        stdscr.attroff(curses.color_pair(3))


def add_algorithm(stdscr, alg, name, y_pos):
    """
    add_algorithm(stdscr, string alg, string name, int y_pos)
    Remix of add_option, for adding algorithims with color scheme on single line

    Parameters:
    stdscr - curses screen
    alg    - Algorithm to be displayed
    name   - Title of the algorithm
    y_pos  - Where to display algorithm on the y axis
    """
    stdscr.addstr(y_pos, 1, name)
    stdscr.addstr(y_pos, 12, "-")
    stdscr.attron(curses.color_pair(4))
    stdscr.addstr(y_pos, 14, alg)
    stdscr.attroff(curses.color_pair(4))
