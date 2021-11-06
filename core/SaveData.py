import sys
import json

class SaveData():
    dataFilePath = "data/wginfo.json"
    data = {}

    def readJson():
        with open(SaveData.dataFilePath) as file:
            jsonData = json.load(file)
        SaveData.data = jsonData

    def writeJson():
        with open(SaveData.dataFilePath, "w") as file:
            json.dump(SaveData.data, file)