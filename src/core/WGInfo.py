import sys
from core.SaveData import SaveData

class WGInfo():
    def __init__(self):
        self.members = []
        self.members = SaveData.data["members"]

    def applyChanges(self, members):
        for i in range(len(members)):
            SaveData.data["members"][i]["name"] = members[i]
        self.members = SaveData.data["members"]
        SaveData.writeJson()
        
