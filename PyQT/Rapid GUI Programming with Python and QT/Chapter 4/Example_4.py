import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(QDialog):
    def __init__(self, parent=None):
        
        super(Form, self).__init__(parent)
        
        dial = QDial()
        dial.setNotchesVisible(True)
        
        spinbox = QSpinBox()
        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)
        
        dial.valueChanged.connect(spinbox.setValue)
        spinbox.valueChanged.connect(dial.setValue)
        #self.connect(dial, SIGNAL("valueChanged(int)"),
        #spinbox.setValue)
        #self.connect(spinbox, SIGNAL("valueChanged(int)"),
        #dial.setValue)
        #self.setWindowTitle("Signals and Slots")
        
        spinbox.valueChanged.emit(10)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()   
    
    #form.spinbox.emit()