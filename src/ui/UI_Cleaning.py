from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
import sys
import schedule
from core.Cleaning import Cleaning
from core.TabBase import TabBase

class UI_Cleaning(QWidget, TabBase):
    
    def __init__(self):
        super().__init__()
        self.title = "Putzdienst"
        self.model = Cleaning()
        self.model.setUiUpdateCallback(self.updateCleaningDuty)
        baseFont = "SF Pro"

        self.thisWeekLabel = QLabel("Diese Woche", self)
        self.thisWeekLabel.setFont(QFont(baseFont, 36, 2, False))
        self.thisWeekLabel.setGeometry(80, 80, 300, 50)

        self.thisWeekName = QLabel(self.model.activeCleaner, self)
        self.thisWeekName.setFont(QFont(baseFont, 72, 0, False))
        self.thisWeekName.setGeometry(120, 150, 300, 75)

        self.nextWeekLabel = QLabel("Nächste Woche", self)
        self.nextWeekLabel.setFont(QFont(baseFont, 24, 2, False))
        self.nextWeekLabel.setGeometry(80, 275, 300, 50)

        self.nextWeekName = QLabel(self.model.nextCleaner, self)
        self.nextWeekName.setFont(QFont(baseFont, 48, 0, False))
        self.nextWeekName.setGeometry(120, 325, 300, 75)

    def updateCleaningDuty(self):
        self.thisWeekName.setText(self.model.activeCleaner)
        self.nextWeekName.setText(self.model.nextCleaner)

    def updateUI(self):
        self.thisWeekName.setText(self.model.activeCleaner)
        self.nextWeekName.setText(self.model.nextCleaner)

    def onSwitch(self):
        self.model.loadActiveCleaner()
        self.model.loadNextCleaner()
        self.updateUI()