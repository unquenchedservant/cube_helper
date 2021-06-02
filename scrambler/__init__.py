import curses, menu_helpers, arithmetic, main
from math import ceil

def screen(stdscr):
	curses.curs_set(0)
	status_msg = "Created by Jonathan Thorne | Random Scramble Generator | ©2021 | esc/m : main menu"
	while True:
		stdscr.clear()
		menu_helpers.status_bar(stdscr, status_msg)
		scramble = arithmetic.get_scramble()
		menu_helpers.center_scramble(stdscr, scramble)
		stdscr.refresh()
		k = stdscr.getch()
		if k == ord('m') or k == 27:
			main.screen(stdscr)