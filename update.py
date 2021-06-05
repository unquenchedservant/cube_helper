import curses
import menu_helpers
import arithmetic
import sys
import subprocess
import main
import os
import requests


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
	title = "Cube Scrambler Update Available"
	center_pos = arithmetic.get_center(stdscr.getmaxyx()[0])
	yes_x_pos = center_pos - 6
	no_x_pos = center_pos + 3
	x_pos = yes_x_pos
	while True:
		stdscr.clear()
		menu_helpers.title(stdscr, title)
		last_y_pos = menu_helpers.center_scramble(stdscr, "Would you like to download the update now?")
		yesno_y_pos = last_y_pos + 2

		if x_pos == yes_x_pos:
			stdscr.addstr(yesno_y_pos, yes_x_pos, "Yes", curses.color_pair(3))
		else:
			stdscr.addstr(yesno_y_pos, yes_x_pos, "Yes")
		if x_pos == no_x_pos:
			stdscr.addstr(yesno_y_pos, no_x_pos, "No", curses.color_pair(3))
		else:
			stdscr.addstr(yesno_y_pos, no_x_pos, "No")
		stdscr.move(y_pos, x_pos)
		stdscr.refresh()
		k = stdscr.getch()
		if k == 27 or k == ord('b'):
			main.screen(stdscr)
		if k == curses.KEY_LEFT or k == curses.KEY_RIGHT or k == curses.KEY_UP or k == curses.KEY_DOWN:
			if x_pos == yes_x_pos:
				x_pos = no_x_pos
			else:
				x_pos = yes_x_pos

		elif k == 10:
			if x_pos == yes_x_pos:
				response = requests.get("https://api.github.com/repos/unquenchedservant/cube_helper/releases/latest")
				download_url = response.json()["assets"][1]["browser_download_url"]
				r = requests.get(download_url, allow_redirects=True)
				open('Updater.exe', 'wb').write(r.content)
				os.system("start cmd.exe /C Updater.exe")
				sys.exit()
			else:
				main.screen(stdscr)
