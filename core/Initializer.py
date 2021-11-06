import sys
from core.SaveData import SaveData

class Initializer():
    def __init__(self):
        
        # Load saved data
        SaveData.readJson()