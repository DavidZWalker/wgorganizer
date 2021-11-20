import sys
import schedule
import time
import threading
from core.SaveData import SaveData
from util.ThreadManager import ThreadManager

class Cleaning():
    def __init__(self):
        self.activeCleaner = ""
        self.nextCleaner = ""
        self.loadActiveCleaner()
        self.loadNextCleaner()
        self.scheduleUpdate()
        
    def loadActiveCleaner(self):
        self.activeCleaner = SaveData.data["activeCleaningDuty"]

    def loadNextCleaner(self):
        members = SaveData.data["members"]
        nextNum = 0
        for i in range(len(members) - 1):
            if members[i]["name"] == self.activeCleaner:
                nextNum = i + 1
        if nextNum > len(members) - 1:
            nextNum = 0
        self.nextCleaner = members[nextNum]["name"]

    def updateCleaningDuty(self):
        SaveData.data["activeCleaningDuty"] = self.nextCleaner
        self.loadActiveCleaner()
        self.loadNextCleaner()
        SaveData.writeJson()
        self.uiUpdateCallback()

    def scheduleUpdate(self):
        schedule.every().monday.at("00:00").do(self.updateCleaningDuty)
        schedThread = threading.Thread(target=self.doScheduler)
        ThreadManager.addThread(schedThread)
        schedThread.start()

    def doScheduler(self):
        while ThreadManager.run_threads:
            schedule.run_pending()
            time.sleep(1)

    def setUiUpdateCallback(self, callback):
        self.uiUpdateCallback = callback
