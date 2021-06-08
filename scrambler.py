import sys
from main import Screen
from PyQt6 import sip
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
	app = QApplication(sys.argv)
	screen = Screen()
	sys.exit(app.exec())