import pll.algorithms as algorithms
import arithmetic

from PyQt6.QtWidgets import QApplication, QGridLayout, QFrame, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QDialog, QMenu, QMainWindow
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QKeySequence, QShortcut
class Algorithms(QWidget):
    def __init__(self, windowX, windowY, parent):
        super().__init__()
        self.mainLayout = QGridLayout()
        self.windowY = windowY
        self.windowX = windowX
        self.setStyleSheet("background-color: #121212;")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.closeWindowAct = QShortcut(QKeySequence('Ctrl+p'), self)
        self.ollWindowAct = QShortcut(QKeySequence('Ctrl+o'), self)
        self.quitAct = QShortcut(QKeySequence('Ctrl+q'), self)
        self.mainAct = QShortcut(QKeySequence('Ctrl+m'), self)
        self.newScramble = QShortcut(QKeySequence('Space'), self)
        self.closeWindowAct.activated.connect(parent.showPLLAlgs)
        self.ollWindowAct.activated.connect(parent.showOLLAlgs)
        self.newScramble.activated.connect(parent.generateScramble)
        self.quitAct.activated.connect(parent.close)
        self.mainAct.activated.connect(parent.goToMain)
        self.nameStyle = "font: 16px !important; font-weight: bold !important; color: #9cb9d3 !important; border-width: 0px !important; padding: 0px; "
        self.algStyle = "font: 12px !important; color: #ffffff !important; border-width: 0px !important; padding: 0px;"
        self.algStyle2 = "font: 12px; color: #9cb9d3; background-color: #383838; border-style: outset; border-width: 2px; border-radius: 10px; border-color: #9cb9d3; max-height: 60px;"
        solutions = algorithms.solutions
        grid_row = 1
        grid_col = 0
        for x in range(0, 6):
            position = (grid_row, grid_col)
            grid_row += 1
            algCard = QWidget()
            algLayout = QVBoxLayout()
            name = QLabel(solutions[x].get("name"), self)
            algorithm = QLabel(solutions[x].get("algorithm"), self)
            name.setStyleSheet(self.nameStyle)
            algorithm.setStyleSheet(self.algStyle)
            algLayout.addWidget(name)
            algLayout.addWidget(algorithm)
            algCard.setLayout(algLayout)
            algCard.setStyleSheet(self.algStyle2)
            self.mainLayout.addWidget(algCard, *position)
        self.setLayout(self.mainLayout)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.move(self.windowX, self.windowY)
        self.resize(500, 600)
        self.setWindowTitle("2-Look PLL Algorithms")
        self.show()

class Trainer(QFrame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.mainLayout = QGridLayout()
        self.scrambles = algorithms.trainer
        self.current_scrambles = self.scrambles.copy()
        self.currentScramble = None
        self.scramble_name = None
        self.scramble = ""
        self.previousName = None
        self.solution = ""
        self.setStyleSheet("background-color: #121212;")
        self.newScramble = QPushButton("Next", self)
        self.newScramble.setShortcut('Space')
        self.newScramble.setStyleSheet("margin-right: 20%; margin-left: 20%; background-color: #383838; color: #9cb9d3; font: 20px; border-style: outset; border-width: 2px; border-radius: 10px; border-color: #9cb9d3;")
        self.scrambleText = QLabel(self.scramble, self)
        self.scrambleText.setStyleSheet("font: 30px; color: #9cb9d3;")
        self.showSolution = QPushButton("Show Solution")
        self.showSolution.setShortcut("s")
        self.showSolution.setStyleSheet("margin-bottom: 50px; margin-top: 50px; margin-right: 200px; margin-left: 200px; background-color: #383838; color: #9cb9d3; font: 20px; border-style: outset; border-width: 2px; border-radius: 10px; border-color: #9cb9d3;")
        self.mainLayout.addWidget(self.scrambleText, *(1, 1))
        self.mainLayout.addWidget(self.showSolution, *(2, 1))
        self.mainLayout.addWidget(self.newScramble, *(3, 1))
        self.solutionLabel = QLabel(self.solution, self)
        self.solutionLabel.setStyleSheet("font: 20px; color: #9cb9d3;")
        self.showSolution.clicked.connect(self.show_solution)
        self.newScramble.clicked.connect(self.get_new)
        self.setLayout(self.mainLayout)
        self.get_new()

    def show_solution(self):
        for i in reversed(range(self.mainLayout.count())):
            self.mainLayout.itemAt(i).widget().setParent(None)
        self.solution = algorithms.solution.get(self.scramble_name)
        self.solutionLabel = QPushButton(self.solution, self)
        self.solutionLabel.setStyleSheet(
            "margin-bottom: 50px; margin-top: 50px; margin-right: 200px; margin-left: 200px; font: 20px; color: #9cb9d3;border-style: outset; border-width: 2px; border-radius: 10px; border-color: #9cb9d3; background-color: #121212;")
        self.scrambleText.setWordWrap(True)
        self.scrambleText.setStyleSheet("font: 30px; color: #9cb9d3;")
        self.mainLayout.addWidget(self.scrambleText, *(1, 1))
        self.mainLayout.addWidget(self.solutionLabel, *(2, 1))
        self.mainLayout.addWidget(self.newScramble, *(3, 1))
        self.setLayout(self.mainLayout)
        timer = QTimer()
        timer.singleShot(3000, self.hide_solution)

    def hide_solution(self):
        for i in reversed(range(self.mainLayout.count())):
            self.mainLayout.itemAt(i).widget().setParent(None)
        self.mainLayout.addWidget(self.scrambleText, *(1, 1))
        self.mainLayout.addWidget(self.showSolution, *(2, 1))
        self.mainLayout.addWidget(self.newScramble, *(3, 1))
        self.setLayout(self.mainLayout)

    def get_new(self):
        for i in reversed(range(self.mainLayout.count())):
            self.mainLayout.itemAt(i).widget().setParent(None)
        current = ""
        while current == "":
            try:
                x = arithmetic.get_random(9)
                current = self.current_scrambles[x]
            except:
                continue
        while self.current_scrambles[x].get("name") == self.previousName:
            current = ""
            while current == "":
                try:
                    x = arithmetic.get_random(9)
                    current = self.current_scrambles[x]
                except:
                    continue
        self.scramble = self.current_scrambles[x].get("algorithm")
        self.scramble_name = self.current_scrambles[x].get("name")
        self.scrambleText = QLabel(self.scramble, self)
        self.scrambleText.setWordWrap(True)
        self.scrambleText.setStyleSheet("font: 30px; color: #9cb9d3;")
        self.mainLayout.addWidget(self.scrambleText, *(1, 1))
        self.mainLayout.addWidget(self.showSolution, *(2, 1))
        self.mainLayout.addWidget(self.newScramble, *(3, 1))
        self.setLayout(self.mainLayout)

