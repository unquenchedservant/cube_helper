import arithmetic
from PyQt6.QtWidgets import QApplication,QFrame, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QDialog, QMenu, QMainWindow
class Screen(QFrame):
	def __init__(self):
		super().__init__()
		self.mainLayout = QVBoxLayout()
		self.setStyleSheet("background-color: #121212;")
		self.scramble = arithmetic.get_scramble()
		self.scrambleText = QLabel(self.scramble, self)
		self.scrambleText.setWordWrap(True)
		self.scrambleText.setStyleSheet("font: 30px; color: #9cb9d3;")
		self.newScramble = QPushButton("New Scramble", self)
		self.newScramble.setStyleSheet("margin-right: 20%; margin-left: 20%; background-color: #383838; color: #9cb9d3; font: 20px; border-style: outset; border-width: 2px; border-radius: 10px; border-color: #9cb9d3;")
		self.mainLayout.addWidget(self.scrambleText)
		self.mainLayout.addWidget(self.newScramble)
		self.newScramble.clicked.connect(self.getNewScramble)
		self.setLayout(self.mainLayout)

	def getNewScramble(self):
		self.mainLayout.removeWidget(self.scrambleText)
		self.mainLayout.removeWidget(self.newScramble)
		self.scramble = arithmetic.get_scramble()
		self.scrambleText = QLabel(self.scramble, self)
		self.scrambleText.setWordWrap(True)
		self.newScramble.setStyleSheet("margin-right: 30px; margin-left: 30px; background-color: #383838; color: #9cb9d3; font: 20px; border-style: outset; border-width: 2px; border-radius: 10px; border-color: #9cb9d3;")
		self.scrambleText.setStyleSheet("font: 30px; color: #9cb9d3;")
		self.mainLayout.addWidget(self.scrambleText)
		self.mainLayout.addWidget(self.newScramble)
