import sys
from core.SaveData import SaveData

class Cleaning():
    def __init__(self):
        self.activeCleaner = ""
        self.nextCleaner = ""
        self.setActiveCleaner()
        self.setNextCleaner()
        
    def setActiveCleaner(self):
        self.activeCleaner = SaveData.data["activeCleaningDuty"]

    def setNextCleaner(self):
        members = SaveData.data["members"]
        nextNum = 0
        for i in range(len(members) - 1):
            if members[i]["name"] == self.activeCleaner:
                nextNum = i + 1
        if nextNum > len(members) - 1:
            nextNum = 0
        self.nextCleaner = members[nextNum]["name"]