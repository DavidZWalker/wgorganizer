from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
import sys
from core.WGInfo import WGInfo

class UI_Settings(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Settings"
        self.model = WGInfo()
        baseFont = "SF Pro"

        self.membersLabel = QLabel("WG-Mitglieder", self)
        self.membersLabel.setFont(QFont(baseFont, 36, 2, False))
        self.membersLabel.setGeometry(80, 80, 300, 50)

        self.applyButton = QPushButton("Übernehmen", self)
        self.applyButton.setGeometry(764,440,150,50)