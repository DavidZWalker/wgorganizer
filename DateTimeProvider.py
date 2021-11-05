import sys
from PyQt5.QtCore import QTimer, QTime, Qt

class DateTimeProvider():
    def getTimeAsString(self):
        currentTime = QTime.currentTime()
        return currentTime.toString('hh:mm:ss')