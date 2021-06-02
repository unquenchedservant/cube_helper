import curses, menu_helpers, main

from oll.screens import oll_2l_trainer_screen, oll_2l_algs_screen


def screen(stdscr):
	"""
	oll_2l_screen
	Main screen for OLL two-look

	Parameters:
	stdscr - Curses screen
	"""
	curses.curs_set(0)
	stdscr.clear()
	x_pos = 1
	y_pos = 1
	title = "Two Look OLL"
	status_msg = "Created by Jonathan Thorne | ©2021 |"
	status_msg += " arrow keys : navigation | esc/m : main menu_helpers | enter : select"
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
				oll_2l_algs_screen(stdscr)
			if y_pos == 2:
				oll_2l_trainer_screen(stdscr)  # two_look_oll_trainer
			if y_pos == 3:
				main.screen(stdscr)
