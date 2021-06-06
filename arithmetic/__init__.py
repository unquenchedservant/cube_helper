from math import floor
import random


def get_center(width):
	return int(floor(width // 2))


def title_start(title, width):
	"""
    title_start(string title, int width)
    returns the starting position for the title given the width of the screen and the title

    Parameters:
    title - Title of the screen
    width - Width of the window
    """
	start_pos = int((width // 2) - (len(title) // 2) - len(title) % 2)
	return start_pos


def scramble_start(lines, height):
	"""
    scramble_start(string title, int width)
    returns the starting position for the scramble given the width of the screen and the title

    Parameters:
    title - Title of the screen
    width - Width of the window
    """
	start_pos = int(((height // 2) - 1) - (lines // 2) - lines % 2)
	return start_pos


def get_random(max_rand):
	"""
    get_random(int max_rand)
    returns a random number between 0 and the given max_rand

    Parameters:
    max_rand - the maximum random number allowed

    Returns:
    a random number
    """
	return floor(random.randint(0, max_rand))


def get_scramble():
	"""
    get_scramble
    returns a scramble of strength 25 based on algorithm found on ruwix

    Returns:
    A scramble of strength 25
    """
	elozo = 1986
	i = 0
	j = 0
	alg = ""
	while i < 25:
		rand = get_random(5)
		j = i
		if rand == 0 and elozo != 0 and elozo != 1:
			i = i + 1
			alg = alg + " U"
		if rand == 1 and elozo != 1 and elozo != 0:
			i = i + 1
			alg = alg + " D"
		if rand == 2 and elozo != 2 and elozo != 3:
			i = i + 1
			alg = alg + " R"
		if rand == 3 and elozo != 3 and elozo != 2:
			i = i + 1
			alg = alg + " L"
		if rand == 4 and elozo != 4 and elozo != 5:
			i = i + 1
			alg = alg + " F"
		if rand == 5 and elozo != 5 and elozo != 4:
			i = i + 1
			alg = alg + " B"
		elozo = rand
		rand = get_random(4)
		if rand <= 1 and i != j:
			j = i
			alg = alg + "'"
		elif rand == 2 and i != j:
			j = i
			alg = alg + "2"
	return alg.strip()
