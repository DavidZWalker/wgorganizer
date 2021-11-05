from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
import sys

class UI_MainWindow(QMainWindow):
    def setupUI(self, mainWindow):
        baseFont = "SF Pro"

        mainWindow.setObjectName("MainWindow")
        mainWindow.resize(1024, 600)
        mainWindow.setMinimumSize(QtCore.QSize(1024, 600))
        mainWindow.setMaximumSize(QtCore.QSize(1024, 600))

        mainWindow.setGeometry(0,0,1024,600)

        self.sidebar = QWidget(mainWindow)
        self.sidebar.setGeometry(0,0,80,600)
        self.sidebar.setStyleSheet("background-color: rgb(46, 46, 46)")

        self.titlebar = QWidget(mainWindow)
        self.titlebar.setGeometry(80,0,944,80)
        self.titlebar.setStyleSheet("background-color: rgb(150,150,150)")

        self.content = QStackedWidget(mainWindow)
        self.content.setGeometry(80,80,944,520)

        self.datelabel = QLabel("DATE PH", self.titlebar)
        self.datelabel.setGeometry(800,15,100,25)
        self.datelabel.setFont(QFont(baseFont, 20, 0, True))
        self.timelabel = QLabel("TIME PH", self.titlebar)
        self.timelabel.setGeometry(800,40,100,25)
        self.timelabel.setFont(QFont(baseFont, 24, 0, True))

        self.title = QLabel("TITLE", self.titlebar)
        self.title.setGeometry(80,15,397,50)
        self.title.setFont(QFont(baseFont, 50))

        self.putzdienstButton = QToolButton(self.sidebar)
        self.putzdienstButton.setGeometry(0,0,80,80)

        self.settingsButton = QToolButton(self.sidebar)
        self.settingsButton.setGeometry(0,520,80,80)