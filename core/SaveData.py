import sys
import json

class SaveData():
    def __init__(self):
        self.dataFilePath = "data/wginfo.json"
        self.data = {}
        self.readJson()
        

    def readJson(self):
        with open(self.dataFilePath) as file:
            data = json.load(file)
        self.data = data
        print(self.data["members"])

    def writeJson(self):
        with open(self.dataFilePath, "w") as file:
            json.dump(self.data, file)