import curses, update, main, utilities, os

if __name__ == "__main__":
	os.system("title Cube Helper v0.11")
	if utilities.update_available():
		curses.wrapper(update.screen)
	else:
		if os.path.exists('Updater.exe'):
			os.remove('Updater.exe')
		curses.wrapper(main.screen)
