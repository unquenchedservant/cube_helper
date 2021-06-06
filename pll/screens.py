import curses

import oll
import pll.algorithms as algorithms
import menu_helpers
import time
import arithmetic


def pll_2l_algs_screen(stdscr, fromOLLMenu=False, fromPLLMenu=False, fromOLL=False, fromOLLCorner=False, fromPLL=False, currentScrambleName=None, currentScramble=None, currentScrambles=None, previousName=""):
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
        for x in range(0, 6):
            menu_helpers.add_algorithm(stdscr, solutions[x].get("algorithm"), solutions[x].get("name"), i)
            i += 2
        if fromPLL or fromOLL or fromOLLCorner:
            stdscr.addstr(13, 1, "Press 'ESC' or 'q' to go back to trainer")
        elif fromPLLMenu:
            stdscr.addstr(13, 1, "Press 'ESC' or 'q' to go back to PLL menu")
        elif fromOLLMenu:
            stdscr.addstr(13, 1, "Press 'ESC' or 'q' to go back to OLL menu")
        else:
            stdscr.addstr(13, 1, "Press 'ESC' or 'q' to go back to OLL menu")

        stdscr.addstr(14, 1, "Press 'o' to go to OLL Algorithms")
        stdscr.refresh()
        k = stdscr.getch()
        if k == 27 or k == ord('b'):
            if fromOLL:
                oll.screens.oll_2l_all_trainer(stdscr, currentScrambleName=currentScrambleName, currentScramble=currentScramble, currentScrambles=currentScrambles, previousName=previousName)
            elif fromOLLCorner:
                oll.screens.oll_2l_corner_trainer(stdscr, currentScrambleName=currentScrambleName, currentScramble=currentScramble, currentScrambles=currentScrambles, previousName=previousName)
            elif fromPLL:
                pll_2l_trainer(stdscr, currentScrambleName=currentScrambleName, currentScramble=currentScramble, currentScrambles=currentScrambles, previousName=previousName)
            elif fromPLLMenu:
                screen(stdscr)
            else:
                oll.screen(stdscr)
        elif k == ord('o'):
            oll.screens.oll_2l_algs_screen(stdscr, fromOLLMenu, fromPLLMenu, fromOLL=fromOLL, fromPLL=fromPLL, fromOLLCorner=fromOLLCorner, currentScrambleName=currentScrambleName, currentScramble=currentScramble, currentScrambles=currentScrambles, previousName=previousName)


def pll_2l_trainer(stdscr, currentScrambleName=None, currentScramble = None, currentScrambles=None, previousName=""):
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
    previous_name = previousName
    scrambles = algorithms.trainer
    current_scrambles = scrambles.copy()
    status_msg = "Created by Jonathan Thorne | ©2021 "
    status_msg += " | 2-Look PLL Trainer | esc/b : back | any other key : generate new scramble"
    while True:
        stdscr.clear()
        menu_helpers.status_bar(stdscr, status_msg)
        current = ""
        if currentScramble is not None:
            scramble_name = currentScrambleName
            scramble = currentScramble
            current_scrambles = currentScrambles
            currentScrambleName = None
            currentScrambles = None
            currentScramble = None
            previousName = ""
        else:
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
            current_scrambles.pop(x)
        stdscr.addstr(1, 1, scramble_name + ": ", curses.color_pair(1))
        stdscr.addstr(2, 1, scramble)
        stdscr.addstr(7, 1, "Press 'o' for OLL Algorithms")
        stdscr.addstr(8, 1, "Press 'b' to go back")
        stdscr.addstr(9, 1, "Press 'a' to peak at the solution for current case")
        previous_name = scramble_name
        stdscr.refresh()
        k = stdscr.getch()
        if k == ord('b') or k == 27:
            screen(stdscr)
        elif k == ord('o'):
            oll.oll_2l_algs_screen(stdscr, fromPLL=True, currentScrambleName=scramble_name, currentScramble=scramble, currentScrambles=current_scrambles, previousName=previous_name)
        elif k == ord('a'):
            peak(stdscr, scramble_name, status_msg, scramble, current_scrambles)
        else:
            continue


def peak(stdscr, scramble_name, status_msg, scramble, current_scrambles):
    from . import screen
    x = 0
    y = 5
    stdscr.clear()
    menu_helpers.status_bar(stdscr, status_msg)
    stdscr.addstr(1, 1, scramble_name + ": ", curses.color_pair(1))
    stdscr.addstr(2, 1, scramble)
    stdscr.addstr(7, 1, "Press 'o' for OLL Algorithms")
    stdscr.addstr(8, 1, "Press 'b' to go back")
    stdscr.addstr(9, 1, "Press 'a' to peak at the solution for current case")
    stdscr.refresh()
    while x != 6:
        solution = algorithms.solution.get(scramble_name)
        stdscr.addstr(4, 1, solution)
        msg = "Solution disappearing in " + str(y) + " seconds"
        stdscr.addstr(5, 1, msg)
        stdscr.refresh()
        time.sleep(1)
        x += 1
        y -= 1
    stdscr.clear()
    menu_helpers.status_bar(stdscr, status_msg)
    stdscr.addstr(1, 1, scramble_name + ": ", curses.color_pair(1))
    stdscr.addstr(2, 1, scramble)
    stdscr.refresh()
    k = stdscr.getch()
    if k == ord('b') or k == 27:
        screen(stdscr)
    elif k == ord('o'):
        oll.oll_2l_algs_screen(stdscr, fromPLL=True, currentScrambleName=scramble_name, currentScramble=scramble,
                               currentScrambles=current_scrambles, previousName=scramble_name)
    if k == ord('a'):
        peak(stdscr, scramble_name, status_msg, scramble, current_scrambles)
