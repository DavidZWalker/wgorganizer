from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
import sys
from UI_MainWindow import UI_MainWindow
from UI_Cleaning import UI_Cleaning


class MainScreen():
    def __init__(self):
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.mainWindow = QMainWindow()
        self.ui = UI_MainWindow()
        self.ui.setupUI(self.mainWindow)

        cleaningScreen = UI_Cleaning()
        self.ui.content.addWidget(cleaningScreen)
        self.ui.content.setCurrentWidget(cleaningScreen)

    def show(self):
        self.mainWindow.show()
        

#main
app = QApplication(sys.argv)
home = MainScreen()
home.show()
sys.exit(app.exec_())