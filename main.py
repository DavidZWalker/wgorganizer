from PyQt5.QtWidgets import QApplication
from ui.UIManager import UIManager
from core.Initializer import Initializer
import sys
     

#main
app = QApplication(sys.argv)
init = Initializer()
home = UIManager()
home.show()
sys.exit(app.exec_())