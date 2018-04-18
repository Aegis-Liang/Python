import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    label = QLabel("<font color=red size=72><b>" + "Hello World!" + "</b></font>")
    label.setWindowFlags(Qt.SplashScreen)
    label.show()
    QTimer.singleShot(3000, app.quit) 
    app.exec_()    
    