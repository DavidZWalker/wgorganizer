from PyQt5 import QtGui
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer
from util.DateTimeProvider import DateTimeProvider
import sys

class UI_MainWindow(QMainWindow):
    def setupUI(self, mainWindow):
        baseFont = "SF Pro"

        mainWindow.setObjectName("MainWindow")
        mainWindow.resize(1024, 600)
        mainWindow.setMinimumSize(QtCore.QSize(1024, 600))
        mainWindow.setMaximumSize(QtCore.QSize(1024, 600))
        mainWindow.setGeometry(0,0,1024,600)

        iconSize = QtCore.QSize(40,40)

        self.datetimeProvider = DateTimeProvider()
        self.startTimer()

        self.sidebar = QWidget(mainWindow)
        self.sidebar.setGeometry(0,0,80,600)
        self.sidebar.setStyleSheet("background-color: rgb(46, 46, 46)")

        self.titlebar = QWidget(mainWindow)
        self.titlebar.setGeometry(80,0,944,80)
        self.titlebar.setStyleSheet("background-color: rgb(150,150,150)")

        self.content = QStackedWidget(mainWindow)
        self.content.setGeometry(80,80,944,520)

        self.datelabel = QLabel(self.datetimeProvider.getDateAsString(), self.titlebar)
        self.datelabel.setGeometry(750,15,150,25)
        self.datelabel.setFont(QFont(baseFont, 20, 0, True))
        self.timelabel = QLabel(self.datetimeProvider.getTimeAsString(), self.titlebar)
        self.timelabel.setGeometry(750,40,150,25)
        self.timelabel.setFont(QFont(baseFont, 30, 0, True))

        self.title = QLabel("TITLE", self.titlebar)
        self.title.setGeometry(80,15,397,50)
        self.title.setFont(QFont(baseFont, 50))

        self.putzdienstButton = QToolButton(self.sidebar)
        self.putzdienstButton.setGeometry(0,0,80,80)
        self.putzdienstButton.setIcon(QtGui.QIcon("src/ui/icons/cleaning.png"))
        self.putzdienstButton.setIconSize(iconSize)

        self.settingsButton = QToolButton(self.sidebar)
        self.settingsButton.setGeometry(0,520,80,80)
        self.settingsButton.setIcon(QtGui.QIcon("src/ui/icons/gear.png"))
        self.settingsButton.setIconSize(iconSize)

    def startTimer(self):
        timer = QTimer(self)
        timer.timeout.connect(self.updateDateTime)
        timer.start(1000)

    def updateDateTime(self):
        currentDateAsString = self.datetimeProvider.getDateAsString()
        currentTimeAsString = self.datetimeProvider.getTimeAsString()
        self.datelabel.setText(currentDateAsString)
        self.timelabel.setText(currentTimeAsString)