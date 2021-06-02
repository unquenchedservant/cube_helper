import curses, sys, scrambler
import menu_helpers, oll, pll


def screen(stdscr):
	curses.start_color()
	curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
	curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.curs_set(0)
	stdscr.clear()
	x_pos = 1
	y_pos = 1
	title = "Cube Scrambler"
	status_msg = "Created by Jonathan Thorne | ©2021 | arrow keys : navigation | esc : quit | enter : select"
	options = ["Scramble Generator", "2-Look OLL Helper", "2-Look PLL Helper"]

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
			sys.exit()
		elif k == curses.KEY_UP:
			if y_pos == 1:
				y_pos = len(options)
			else:
				y_pos -= 1
		elif k == curses.KEY_DOWN:
			y_pos += 1
			if y_pos >= len(options) + 1:
				y_pos = 1
		elif k == 10 or k == curses.KEY_RIGHT:
			if y_pos == 1:
				scrambler.screen(stdscr)
			elif y_pos == 2:
				oll.screen(stdscr)  # oll helper
			elif y_pos == 3:
				pll.screen(stdscr)
		elif k == ord('1'):
			scrambler.screen(stdscr)
		elif k == ord('2'):
			oll.screen(stdscr)  # oll helper
		elif k == ord('3'):
			pll.screen(stdscr)
