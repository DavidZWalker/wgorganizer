from PyQt5.QtWidgets import QApplication
from ui.UIManager import UIManager
from core.Initializer import Initializer
from util.ThreadManager import ThreadManager
import sys  

#main
app = QApplication(sys.argv)
init = Initializer()
home = UIManager()
home.show()
try:
    sys.exit(app.exec_())
finally:
    ThreadManager.closeThreads()