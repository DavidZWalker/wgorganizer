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
        self.membersLabel.setGeometry(80, 30, 300, 50)

        vSpacing = 55
        i = 1
        for member in self.model.members:
            txtEdit = QTextEdit(member["name"], self)
            txtEdit.setFont(QFont(baseFont, 24, 2, False))
            txtEdit.setGeometry(100,50+vSpacing*i,300,50)
            i+=1

        self.applyButton = QPushButton("Übernehmen", self)
        self.applyButton.setGeometry(764,440,150,50)