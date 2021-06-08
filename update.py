import sys
import os
import requests
import PyQt6
from PyQt6.QtWidgets import (QWidget, QMessageBox, QToolTip, QPushButton, QLabel, QApplication, QHBoxLayout, QVBoxLayout)
from PyQt6.QtGui import QFont

class Update(PyQt6.QtWidgets.QMessageBox):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("Update")
		self.setText("Would you to download the latest update?")
		self.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
		self.setDefaultButton(QMessageBox.StandardButton.Yes)
		self.buttonClicked.connect(self.handleButton)
	def handleButton(self, i):
		if i.text() == "&Yes":
			response = requests.get("https://api.github.com/repos/unquenchedservant/cube_helper/releases/latest")
			download_url = response.json()["assets"][1]["browser_download_url"]
			r = requests.get(download_url, allow_redirects=True)
			open('Updater.exe', 'wb').write(r.content)
			os.system("start cmd.exe /C Updater.exe")
			sys.exit()
