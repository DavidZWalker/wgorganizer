from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
import sys
from core.WGInfo import WGInfo
from core.TabBase import TabBase

class UI_Members(QWidget, TabBase):

    def __init__(self):
        super().__init__()
        self.title = "Mitgliederverwaltung"
        self.model = WGInfo()
        self.__memberTextEdits = []
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
            self.__memberTextEdits.append(txtEdit)
            i+=1

        self.applyButton = QPushButton("Übernehmen", self)
        self.applyButton.setGeometry(764,440,150,50)
        self.applyButton.clicked.connect(self.onApplyClicked)

    def onApplyClicked(self):
        members = []
        for textEdit in self.__memberTextEdits:
            members.append(textEdit.toPlainText())
        self.model.applyChanges(members) 

    def onSwitch(self):
        for num in range(len(self.model.members)):
            self.__memberTextEdits[num].setText(self.model.members[num]["name"])
