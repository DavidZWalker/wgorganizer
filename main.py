from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import * 
import sys
from UI_MainWindow import UI_MainWindow
from UI_Cleaning import UI_Cleaning
from UI_Settings import UI_Settings
from DateTimeProvider import DateTimeProvider


class UIManager():
    def __init__(self):
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.mainWindow = QMainWindow()
        self.ui = UI_MainWindow()
        self.ui.setupUI(self.mainWindow)

        self.datetimeProvider = DateTimeProvider()
        self.startTimer()

        self.cleaningScreen = UI_Cleaning()
        self.ui.content.addWidget(self.cleaningScreen)

        self.settingsScreen = UI_Settings()
        self.ui.content.addWidget(self.settingsScreen)

        self.ui.content.setCurrentWidget(self.cleaningScreen)

        self.ui.settingsButton.clicked.connect(lambda: self.switchTo("settings"))
        self.ui.putzdienstButton.clicked.connect(lambda: self.switchTo("cleaning"))

    def switchTo(self, widgetName):
        if widgetName == "cleaning":
            self.ui.content.setCurrentWidget(self.cleaningScreen)
        elif widgetName == "settings":
            self.ui.content.setCurrentWidget(self.settingsScreen)

    def show(self):
        self.mainWindow.show()

    def startTimer(self):
        timer = QTimer(self.mainWindow)
        timer.timeout.connect(self.updateTime)
        timer.start(1000)

    def updateTime(self):
        currentTimeAsString = self.datetimeProvider.getTimeAsString()
        self.ui.timelabel.setText(currentTimeAsString)

        

#main
app = QApplication(sys.argv)
home = UIManager()
home.show()
sys.exit(app.exec_())