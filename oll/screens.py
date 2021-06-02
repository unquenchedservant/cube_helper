import curses, oll.algorithms as algorithms
import menu_helpers
import arithmetic
import time


def oll_2l_algs_screen(stdscr):
	"""
		oll_2l_algs_screen
		Shows algorithms for 2-Look OLL

		Parameters:
			stdscr - Curses screen
	"""
	from . import screen
	curses.curs_set(0)
	stdscr.clear()
	title = "2-Look OLL Algorithms"
	status_msg = "Created by Jonathan Thorne | ©2021 | esc/b : back "
	solutions = algorithms.solutions
	while True:
		stdscr.clear()
		menu_helpers.title(stdscr, title)
		menu_helpers.status_bar(stdscr, status_msg)
		i = 1
		for x in range(0, 9):
			menu_helpers.add_algorithm(stdscr, solutions[x].get("algorithm"), solutions[x].get("name"), i)
			i += 2
		stdscr.refresh()
		k = stdscr.getch()
		if k == 27 or k == ord('b'):
			screen(stdscr)


def oll_2l_trainer_screen(stdscr):
	"""
	oll_2l_trainer_screen
	A menu_helpers for selecting the type of algorithms you want to train on (corner or edge and corner)

	Parameters:
		stdscr - Curses screen
	"""
	from . import screen
	curses.curs_set(0)
	stdscr.clear()
	x_pos = 1
	y_pos = 1
	title = "2-Look OLL Trainer"
	status_msg = "Created by Jonathan Thorne | ©2021 | arrow keys : navigation | esc/b : back | enter : select"
	options = ["Edges and Corners", "Corners"]

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
		if k == 27 or k == ord('b'):
			screen(stdscr)
		elif k == curses.KEY_UP:
			y_pos -= 1
			if y_pos == 0:
				y_pos = len(options) + 1
		elif k == curses.KEY_DOWN:
			y_pos += 1
			if y_pos >= len(options) + 1:
				y_pos = 1
		elif k == 10 or k == curses.KEY_RIGHT:
			if y_pos == 1:
				oll_2l_all_trainer(stdscr)
			if y_pos == 2:
				oll_2l_corner_trainer(stdscr)
			if y_pos == 3:
				screen(stdscr)


def oll_2l_all_trainer(stdscr):
	"""
	oll_2l_all_trainer
	Gives random scrambles for 2-Look OLL with corners and edges

	Parameters:
		stdscr - Curses screen
	"""
	curses.curs_set(0)
	stdscr.clear()
	max_rand = 9
	previous_name = ""
	scrambles = algorithms.all_trainer
	current_scrambles = scrambles.copy()
	status_msg = "Created by Jonathan Thorne | ©2021 |"
	status_msg += " 2-Look OLL Trainer | esc/b : back | any other key : generate new scramble"
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
				continue
		while current_scrambles[x].get("name") == previous_name:
			current = ""
			while current == "":
				try:
					x = arithmetic.get_random(max_rand)
					current = current_scrambles[x]
				except:
					continue
		scramble = current_scrambles[x].get("algorithm")
		scramble_name = current_scrambles[x].get("name")
		stdscr.addstr(1, 1, scramble_name + ": ", curses.color_pair(1))
		stdscr.addstr(2, 1, scramble)
		current_scrambles.pop(x)
		previous_name = scramble_name
		stdscr.refresh()
		k = stdscr.getch()
		if k == ord('b') or k == 27:
			oll_2l_trainer_screen(stdscr)


def oll_2l_corner_trainer(stdscr):
	"""
	oll_2l_corner_trainer
	Gives random scrambles for corner cases of 2-look OLL

	Parameters:
		stdscr - Curses screen
	"""
	curses.curs_set(0)
	stdscr.clear()
	max_rand = 6
	previous_name = ""
	scrambles = algorithms.corner_trainer
	current_scrambles = scrambles.copy()
	status_msg = "Created by Jonathan Thorne | ©2021 |"
	status_msg += " 2-Look OLL Trainer | esc/b : back | any other key : generate new scramble"
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
				continue
		while current_scrambles[x].get("name") == previous_name:
			current = ""
			while current == "":
				try:
					x = arithmetic.get_random(max_rand)
					current = current_scrambles[x]
				except:
					continue
		scramble = current_scrambles[x].get("algorithm")
		scramble_name = current_scrambles[x].get("name")
		stdscr.addstr(1, 1, scramble_name + ": ", curses.color_pair(1))
		stdscr.addstr(2, 1, scramble)
		current_scrambles.pop(x)
		previous_name = scramble_name
		stdscr.refresh()
		k = stdscr.getch()
		if k == ord('b') or k == 27:
			oll_2l_trainer_screen(stdscr)
		elif k == ord('p'):
			peak(stdscr, scramble_name, status_msg, scramble)


def peak(stdscr, scramble_name, status_msg, scramble):
	x = 0
	y = 5
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
		oll_2l_trainer_screen(stdscr)
	if k == ord('p'):
		peak(stdscr, scramble_name, status_msg, scramble)
