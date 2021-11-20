from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
import sys
from core.Settings import Settings
from core.TabBase import TabBase

class UI_Settings(QWidget, TabBase):

    def __init__(self):
        super().__init__()
        self.title = "Einstellungen"
        self.model = Settings()
        pass

    def onSwitch(self):
        pass