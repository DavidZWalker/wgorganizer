from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
import sys

class UI_Settings(QWidget):
    def __init__(self):
        super().__init__()
        baseFont = "SF Pro"

        self.membersLabel = QLabel("WG-Mitglieder", self)
        self.membersLabel.setFont(QFont(baseFont, 36, 2, False))
        self.membersLabel.setGeometry(100, 100, 300, 100)

        self.applyButton = QPushButton("Übernehmen", self)
        self.applyButton.setGeometry(390,764,100,50)