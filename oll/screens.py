import curses
import oll.algorithms as algorithms
import menu_helpers
import arithmetic
import time

import pll.screens


def oll_2l_algs_screen(stdscr, fromOLLMenu=False, fromPLLMenu=False, fromOLL=False, fromOLLCorner=False, fromPLL=False, currentScrambleName=None,
					   currentScramble=None, currentScrambles=None, previousName=""):
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
		for x in range(0, 10):
			menu_helpers.add_algorithm(stdscr, solutions[x].get("algorithm"), solutions[x].get("name"), i)
			i += 2
		if fromPLL or fromOLL or fromOLLCorner:
			stdscr.addstr(21, 1, "Press 'ESC' or 'q' to go back to trainer")
		elif fromOLLMenu:
			stdscr.addstr(21, 1, "Press 'ESC' or 'q' to go back to OLL menu")
		elif fromPLLMenu:
			stdscr.addstr(21, 1, "Press 'ESC' or 'q' to go back to PLL menu")
		else:
			stdscr.addstr(21, 1, "Press 'ESC' or 'q' to go back to PLL menu")
		stdscr.addstr(22, 1, "Press 'p' to go to PLL Algorithms")
		stdscr.refresh()
		k = stdscr.getch()
		if k == 27 or k == ord('b'):
			if fromPLL:
				pll.screens.pll_2l_trainer(stdscr, currentScrambleName=currentScrambleName,
										   currentScramble=currentScramble, currentScrambles=currentScrambles,
										   previousName=previousName)
			elif fromOLL:
				oll_2l_all_trainer(stdscr, currentScrambleName=currentScrambleName, currentScramble=currentScramble,
								   currentScrambles=currentScrambles, previousName=previousName)
			elif fromOLLCorner:
				oll_2l_corner_trainer(stdscr, currentScrambleName=currentScrambleName, currentScramble=currentScramble,
									  currentScrambles=currentScrambles, previousName=previousName)
			elif fromOLLMenu:
				screen(stdscr)
			else:
				pll.screen(stdscr)
		if k == ord('p'):
			pll.screens.pll_2l_algs_screen(stdscr, fromPLLMenu=fromPLLMenu, fromOLLMenu=fromOLLMenu, fromOLL=fromOLL, fromOLLCorner=fromOLLCorner, fromPLL=fromPLL,
										   currentScrambleName=currentScrambleName, currentScramble=currentScramble,
										   currentScrambles=currentScrambles)


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


def oll_2l_all_trainer(stdscr, currentScrambleName=None, currentScramble=None, currentScrambles=None, previousName=""):
	"""
	oll_2l_all_trainer
	Gives random scrambles for 2-Look OLL with corners and edges

	Parameters:
		stdscr - Curses screen
	"""
	curses.curs_set(0)
	stdscr.clear()
	max_rand = 9
	previous_name = previousName
	scrambles = algorithms.all_trainer
	current_scrambles = scrambles.copy()
	status_msg = "Created by Jonathan Thorne | ©2021 |"
	status_msg += " 2-Look OLL Trainer | esc/b : back | any other key : generate new scramble"
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
			oll_2l_trainer_screen(stdscr)
		elif k == ord('p'):
			pll.screens.pll_2l_algs_screen(stdscr, currentScrambleName=scramble_name, currentScramble=scramble,
										   currentScrambles=current_scrambles, previousName=previous_name, fromOLL=True)
		elif k == ord('a'):
			peak(stdscr, scramble_name, status_msg, scramble)


def oll_2l_corner_trainer(stdscr, currentScrambleName=None, currentScramble=None, currentScrambles=None,
						  previousName=""):
	"""
	oll_2l_corner_trainer
	Gives random scrambles for corner cases of 2-look OLL

	Parameters:
		stdscr - Curses screen
	"""
	curses.curs_set(0)
	stdscr.clear()
	max_rand = 6
	previous_name = previousName
	scrambles = algorithms.corner_trainer
	current_scrambles = scrambles.copy()
	status_msg = "Created by Jonathan Thorne | ©2021 |"
	status_msg += " 2-Look OLL Trainer | esc/b : back | any other key : generate new scramble"
	while True:
		stdscr.clear()
		menu_helpers.status_bar(stdscr, status_msg)
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
			current = ""
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
			current_scrambles.pop(x)
		stdscr.addstr(1, 1, scramble_name + ": ", curses.color_pair(1))
		stdscr.addstr(2, 1, scramble)
		stdscr.addstr(7, 1, "Press 'p' for PLL Algorithms")
		stdscr.addstr(8, 1, "Press 'b' to go back")
		stdscr.addstr(9, 1, "Press 'a' to peak at the solution for current case")
		previous_name = scramble_name
		stdscr.refresh()
		k = stdscr.getch()
		if k == ord('b') or k == 27:
			oll_2l_trainer_screen(stdscr)
		elif k == ord('p'):
			pll.screens.pll_2l_algs_screen(stdscr, currentScrambleName=scramble_name, currentScramble=scramble,
										   currentScrambles=current_scrambles, previousName=previous_name,
										   fromOLLCorner=True)
		elif k == ord('a'):
			peak(stdscr, scramble_name, status_msg, scramble, current_scrambles)
		else:
			continue


def peak(stdscr, scramble_name, status_msg, scramble, current_scrambles):
	x = 0
	y = 5
	stdscr.clear()
	menu_helpers.status_bar(stdscr, status_msg)
	stdscr.addstr(1, 1, scramble_name + ": ", curses.color_pair(1))
	stdscr.addstr(2, 1, scramble)
	stdscr.addstr(7, 1, "Press 'p' for PLL Algorithms")
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
		oll_2l_trainer_screen(stdscr)
	if k == ord('p'):
		pll.screens.pll_2l_algs_screen(stdscr, currentScrambleName=scramble_name, currentScramble=scramble,
									   currentScrambles=current_scrambles, previousName=scramble_name,
									   fromOLLCorner=True)
	if k == ord('a'):
		peak(stdscr, scramble_name, status_msg, scramble, current_scrambles)
