import sys
import scramble
import pll
import oll
import update
import utilities
import os
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow
from PyQt6.QtGui import QAction, QKeySequence, QShortcut

class Screen(QMainWindow):
	def __init__(self):
		super().__init__()
		self.scrambleWindow = None
		self.mainScreen = None
		self.ollWindow = None
		self.pllWindow = None
		self.ollAlgWidget = None
		self.pllAlgWidget = None
		self.centered = False
		self.OLLAll = False
		self.OLLCorner = False
		self.isScrambleScreen = True
		self.closeEvent = self.closeWindows
		self.menubar = self.menuBar()
		self.algMenu = self.menubar.addMenu('Algorithms')
		self.trainerMenu = self.menubar.addMenu('Trainer')

		self.menubar.setStyleSheet("background-color: #383838; color: #9cb9d3;")

		self.mainAct = QAction('Main', self)
		self.ollAlgs = QAction('2-Look OLL', self)
		self.pllAlgs = QAction('2-Look PLL', self)
		self.ollAll = QAction('2-Look OLL All Cases', self)
		self.ollCorner = QAction('2-Look OLL Corner Cases', self)
		self.pllTrainer = QAction('2-Look PLL', self)
		self.exitAct = QAction('Exit', self)
		self.updateAction = QAction('Update Available!', self)

		self.mainShort = QShortcut(QKeySequence('Ctrl+m'), self)
		self.ollAlgs.setShortcut('Ctrl+o')
		self.pllAlgs.setShortcut('Ctrl+p')
		self.exitAct.setShortcut('Ctrl+q')
		self.ollAll.setShortcut('Ctrl+1')
		self.ollCorner.setShortcut('Ctrl+2')
		self.pllTrainer.setShortcut('Ctrl+3')

		self.mainShort.activated.connect(self.goToMain)
		self.exitAct.triggered.connect(self.close)
		self.mainAct.triggered.connect(self.goToMain)
		self.ollAlgs.triggered.connect(self.showOLLAlgs)
		self.pllAlgs.triggered.connect(self.showPLLAlgs)
		self.ollAll.triggered.connect(self.showOLLAll)
		self.ollCorner.triggered.connect(self.showOLLCorner)
		self.pllTrainer.triggered.connect(self.showPLL)
		self.updateAction.triggered.connect(self.update)

		self.trainerMenu.addAction(self.ollAll)
		self.trainerMenu.addAction(self.ollCorner)
		self.trainerMenu.addAction(self.pllTrainer)
		self.algMenu.addAction(self.ollAlgs)
		self.algMenu.addAction(self.pllAlgs)
		self.menubar.addAction(self.mainAct)
		self.menubar.addAction(self.exitAct)
		self.menubar.addAction(self.updateAction)
		self.initUI()

	def closeWindows(self, event):
		sys.exit()

	def update(self):
		updatePopup = update.Update()
		updatePopup.exec()

	def generateScramble(self):
		if self.isScrambleScreen == True:
			self.mainWidget.getNewScramble()

	def initUI(self):
		self.mainWidget = scramble.Screen()
		self.isScrambleScreen = True
		self.mainAct.setVisible(False)
		self.setCentralWidget(self.mainWidget)
		self.setWindowTitle('Cube Helper v0.2 - Scramble Generator')
		self.setCentralWidget(self.mainWidget)
		if not self.centered == True:
			self.resize(700, 600)
			self.center()
			self.centered = True
		self.show()
		if utilities.update_available():
			self.updateAction.setVisible(True)
			self.update()
		else:
			if os.path.exists('Updater.exe'):
				os.remove('Updater.exe')
			self.updateAction.setVisible(False)
	def center(self):
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	def showPLL(self):
		if self.pllWindow is None:
			self.pllWindow = pll.Trainer(self)
			self.pllAlgWidget = None
			self.mainAct.setVisible(True)
			self.setCentralWidget(self.pllWindow)
			self.ollWindow = None
			self.OLLCorner = False
			self.OLLAll = False
			self.isScrambleScreen = False
			self.setWindowTitle('Cube Helper v0.2 - 2-Look PLL Trainer')
	def showOLLAll(self):
		if self.ollWindow is None or self.OLLCorner == True:
			self.ollWindow = oll.AllTrainer(self)
			self.mainAct.setVisible(True)
			self.setCentralWidget(self.ollWindow)
			self.OLLCorner = False
			self.OLLAll = True
			self.pllWindow = None
			self.isScrambleScreen = False
			self.setWindowTitle('Cube Helper v0.2 - 2-Look OLL (All) Trainer')
	def showOLLCorner(self):
		if self.ollWindow is None or self.OLLAll == True:
			self.ollWindow = oll.CornerTrainer(self)
			self.mainAct.setVisible(True)
			self.setCentralWidget(self.ollWindow)
			self.pllWindow = None
			self.OLLCorner = True
			self.OLLAll = False
			self.isScrambleScreen = False
			self.setWindowTitle('Cube Helper v0.2 - 2-Look OLL (Corner) Trainer')

	def showOLLAlgs(self):
		if self.ollAlgWidget is None:
			self.windowStart = self.pos()
			y_pos = self.menubar.mapToGlobal(self.menubar.pos()).y()
			self.ollAlgWidget = oll.Algorithms(self.windowStart, y_pos, self)
		else:
			self.ollAlgWidget = None
	def showPLLAlgs(self):
		if self.pllAlgWidget is None:
			self.windowEndX = self.pos().x() + self.frameGeometry().width()
			self.windowY = self.menubar.mapToGlobal(self.menubar.pos()).y()
			self.pllAlgWidget = pll.Algorithms(self.windowEndX, self.windowY, self)
		else:
			self.pllAlgWidget = None
	def goToMain(self):
		if self.mainAct.isVisible():
			self.isScrambleScreen = True
			self.initUI()
