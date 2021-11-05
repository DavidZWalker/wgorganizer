import sys
from PyQt5.QtCore import QTimer, QTime, QDate, QLocale, Qt

class DateTimeProvider():
    def getTimeAsString(self):
        currentTime = QTime.currentTime()
        return currentTime.toString('hh:mm:ss')

    def getDateAsString(self):
        currentDate = QDate.currentDate()
        return currentDate.toString("dddd, dd.MM.")