from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
import sys

class UI_Cleaning(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "Putzdienst"
        baseFont = "SF Pro"
        
        self.thisWeekLabel = QLabel("Diese Woche", self)
        self.thisWeekLabel.setFont(QFont(baseFont, 36, 2, False))
        self.thisWeekLabel.setGeometry(100, 100, 300, 50)

        self.thisWeekName = QLabel("<NAME>", self)
        self.thisWeekName.setFont(QFont(baseFont, 72, 0, False))
        self.thisWeekName.setGeometry(150, 200, 300, 50)

        self.nextWeekLabel = QLabel("Nächste Woche", self)
        self.nextWeekLabel.setFont(QFont(baseFont, 24, 2, False))
        self.nextWeekLabel.setGeometry(100, 300, 300, 50)

        self.nextWeekName = QLabel("<NAME>", self)
        self.nextWeekName.setFont(QFont(baseFont, 48, 0, False))
        self.nextWeekName.setGeometry(150, 400, 300, 50)