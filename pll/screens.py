import curses, menu_helpers, arithmetic, pll.algorithms as algorithms



def pll_2l_algs_screen(stdscr):
    """
    pll_2l_algs_screen
    Shows algorithms for 2-Look PLL

    Parameters:
    stdscr - Curses screen
    """
    from . import screen
    curses.curs_set(0)
    stdscr.clear()
    title = "2-Look PLL Algorithms"
    status_msg = "Created by Jonathan Thorne | ©2021 | esc/b : back "
    solutions = algorithms.solutions
    while True:
        stdscr.clear()
        menu_helpers.title(stdscr, title)
        menu_helpers.status_bar(stdscr, status_msg)
        i = 1
        for x in range(0, 5):
            menu_helpers.add_algorithm(stdscr, solutions[x].get("algorithm"), solutions[x].get("name"), i)
            i += 2
        stdscr.refresh()
        k = stdscr.getch()
        if k == 27 or k == ord('b'):
            screen(stdscr)


def pll_2l_trainer(stdscr):
    """
    pll_2l_trainer_screen
    Gives random scrambles for 2-Look PLL

    Parameters:
    stdscr - Curses screen
    """
    from . import screen
    curses.curs_set(0)
    stdscr.clear()
    max_rand = 5
    previous_name = ""
    scrambles = algorithms.trainer
    current_scrambles = scrambles.copy()
    status_msg = "Created by Jonathan Thorne | ©2021 "
    status_msg += " | 2-Look PLL Trainer | esc/b : back | any other key : generate new scramble"
    while True:
        stdscr.clear()
        menu_helpers.status_bar(stdscr, status_msg)
        current = ""
        if len(current_scrambles) == 0:
            current_scrambles = scrambles.copy()
        while current == "":
            try:
                x = arithmetic.get_random(max_rand)
                current = current_scrambles[x]
            except:
                pass
        while current_scrambles[x].get("name") == previous_name:
            current = ""
            while current == "":
                try:
                    x = arithmetic.get_random(max_rand)
                    current = current_scrambles[x]
                except:
                    pass
        scramble = current_scrambles[x].get("algorithm")
        scramble_name = current_scrambles[x].get("name")
        stdscr.addstr(1, 1, scramble_name + ": ", curses.color_pair(1))
        stdscr.addstr(2, 1, scramble)
        current_scrambles.pop(x)
        previous_name = scramble_name
        stdscr.refresh()
        k = stdscr.getch()
        if k == ord('b') or k == 27:
            screen(stdscr)
