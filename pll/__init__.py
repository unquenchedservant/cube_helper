import curses
import pll.screens as screens
import menu_helpers
import main


def screen(stdscr):
    """
    pll_2l_screen
    Main screen for PLL two-look

    Parameters:
    stdscr - Curses screen
    """
    curses.curs_set(0)
    stdscr.clear()
    x_pos = 1
    y_pos = 1
    title = "Two Look PLL"
    status_msg = "Created by Jonathan Thorne | ©2021 | arrow keys : navigation | esc/q : quit | enter : select"
    options = ["Algorithms", "Trainer", "Back"]

    while True:
        stdscr.clear()
        menu_helpers.title(stdscr, title)
        menu_helpers.status_bar(stdscr, status_msg)
        i = 1
        for option in options:
            menu_helpers.add_option(stdscr, option, i, 1, y_pos)
            i += 1
        stdscr.move(y_pos, x_pos)
        stdscr.refresh()
        k = stdscr.getch()
        if k == 27 or k == ord('q'):
            main.screen(stdscr)
        elif k == curses.KEY_UP:
            y_pos -= 1
            if y_pos == 0:
                y_pos = len(options)
        elif k == curses.KEY_DOWN:
            y_pos += 1
            if y_pos >= len(options) + 1:
                y_pos = 1
        elif k == 10 or k == curses.KEY_RIGHT:
            if y_pos == 1:
                screens.pll_2l_algs_screen(stdscr, fromPLLMenu=True, fromOLLMenu=False)
            if y_pos == 2:
                screens.pll_2l_trainer(stdscr)
            if y_pos == 3:
                main.screen(stdscr)
