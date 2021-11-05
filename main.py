from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import * 
import sys
from ui.UI_MainWindow import UI_MainWindow
from ui.UI_Cleaning import UI_Cleaning
from ui.UI_Settings import UI_Settings
from util.DateTimeProvider import DateTimeProvider


class UIManager():
    def __init__(self):
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.mainWindow = QMainWindow()
        self.ui = UI_MainWindow()
        self.ui.setupUI(self.mainWindow)

        self.datetimeProvider = DateTimeProvider()
        self.updateDateTime()
        self.startTimer()

        self.cleaningScreen = UI_Cleaning()
        self.ui.content.addWidget(self.cleaningScreen)

        self.settingsScreen = UI_Settings()
        self.ui.content.addWidget(self.settingsScreen)

        self.switchTo("cleaning")

        self.ui.settingsButton.clicked.connect(lambda: self.switchTo("settings"))
        self.ui.putzdienstButton.clicked.connect(lambda: self.switchTo("cleaning"))

    def switchTo(self, widgetName):
        if widgetName == "cleaning":
            self.ui.title.setText(self.cleaningScreen.title)
            self.ui.content.setCurrentWidget(self.cleaningScreen)
        elif widgetName == "settings":
            self.ui.title.setText(self.settingsScreen.title)
            self.ui.content.setCurrentWidget(self.settingsScreen)

    def show(self):
        self.mainWindow.show()

    def startTimer(self):
        timer = QTimer(self.mainWindow)
        timer.timeout.connect(self.updateDateTime)
        timer.start(1000)

    def updateDateTime(self):
        currentDateAsString = self.datetimeProvider.getDateAsString()
        currentTimeAsString = self.datetimeProvider.getTimeAsString()
        self.ui.datelabel.setText(currentDateAsString)
        self.ui.timelabel.setText(currentTimeAsString)

        

#main
app = QApplication(sys.argv)
home = UIManager()
home.show()
sys.exit(app.exec_())