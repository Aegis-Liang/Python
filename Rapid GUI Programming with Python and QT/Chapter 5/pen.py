import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class PenProertiesDialog(QDialog):
    def __init__(self, parent=None):
	super(PenProertiesDialog, self).__init__(parent)
	
	widthLabel = QLabel("&Width:")
	self.widthSpinBox = QSpinBox()
	widthLabel.setBuddy(self.widthSpinBox)
	self.widthSpinBox.setAlignment(Qt.AlignRight | Qt.AlignCenter)
	self.widthSpinBox.setRange(0, 24)
	self.beveledCheckBox = QCheckBox("&Beveled edges")
	styleLabel = QLabel("&Style:")
	self.styleComboBox = QComboBox()
	styleLabel.setBuddy(self.styleComboBox)
	self.styleComboBox.addItems(["Solid", "Dashed", "Dotted", 
                "DashDotted", "DashDotDotted"])
	okButton = QPushButton("&OK")
	cancelButton = QPushButton("&Cancel")

	buttonLayout = QHBoxLayout()
	buttonLayout.addStretch()
	buttonLayout.addWidget(okButton)
	buttonLayout.addWidget(cancelButton)

	layout = QGridLayout()
	layout.addWidget(widthLabel, 0, 0)
	layout.addWidget(self.widthSpinBox, 0, 1)
	layout.addWidget(self.beveledCheckBox, 0, 2)
	layout.addWidget(styleLabel, 1, 0)
	layout.addWidget(self.styleComboBox, 1, 1, 1, 2)
	layout.addLayout(buttonLayout, 2, 0, 1, 3)
	self.setLayout(layout)

	okButton.clicked.connect(self.accept)
	cancelButton.clicked.connect(self.reject)
	self.setWindowTitle("Pen Properties")

class PenDialog(QDialog):
    def __init__(self, parent=None):
	super(PenDialog, self).__init__(parent)

	self.width = 1
	self.beveled = False
	self.style = "Solid"

	penButtonInline = QPushButton("Set Pen...(Dumb &inline)")
	penButton = QPushButton("Set Pen...(Dumb &class)")
	self.label = QLabel("The pen has not been set.")
	self.label.setTextFormat(Qt.RichText)

	layout = QVBoxLayout()
	layout.addWidget(penButtonInline)
	layout.addWidget(penButton)
	layout.addWidget(self.label)
	self.setLayout(layout)

	penButtonInline.clicked.connect(self.setPenInline)
	penButton.clicked.connect(self.setPenProperties)
	self.setWindowTitle("Pen")
	self.updateData()
    
    def updateData(self):
	bevel = ""
	if self.beveled:
		bevel = "<br>Beveled"
	self.label.setText( "Width = {0}<br>Style = {1}{2}"
                .format(self.width, self.style, bevel) )
    
    def setPenProperties(self):
	dialog = PenProertiesDialog(self)
	dialog.widthSpinBox.setValue(self.width)
	dialog.beveledCheckBox.setChecked(self.beveled)
	dialog.styleComboBox.setCurrentIndex(dialog.styleComboBox.findText(self.style))
	if dialog.exec_():
	    self.width = dialog.widthSpinBox.value()
	    self.beveled = dialog.beveledCheckBox.isChecked()
	    self.style = str(dialog.styleComboBox.currentText())
	    self.updateData()
    
    def setPenInline(self):
	widthLabel = QLabel("&Width:")
	widthSpinBox = QSpinBox()
	widthLabel.setBuddy(widthSpinBox)
	widthSpinBox.setAlignment(Qt.AlignRight)
	widthSpinBox.setRange(0, 24)
	widthSpinBox.setValue(self.width)
	beveledCheckBox = QCheckBox("&Beveled edges")
	beveledCheckBox.setChecked(self.beveled)
	styleLabel = QLabel("&Style:")
	styleComboBox = QComboBox()
	styleLabel.setBuddy(styleComboBox)
	styleComboBox.addItems(["Solid", "Dashed", "Dotted",
                "DashDotted", "DashDotDotted"])
	styleComboBox.setCurrentIndex(styleComboBox.findText(self.style))
	okButton = QPushButton("&OK")
	cancelButton = QPushButton("Cancel")
	
	buttonLayout = QHBoxLayout()
	buttonLayout.addStretch()
	buttonLayout.addWidget(okButton)
	buttonLayout.addWidget(cancelButton)
	layout = QGridLayout()
	layout.addWidget(widthLabel, 0, 0)
	layout.addWidget(widthSpinBox, 0, 1)
	layout.addWidget(beveledCheckBox, 0, 2)
	layout.addWidget(styleLabel, 1, 0)
	layout.addWidget(styleComboBox, 1, 1, 1, 2)
	layout.addLayout(buttonLayout, 2, 0, 1, 3)
	
	form = QDialog()
	form.setLayout(layout)
	okButton.clicked.connect(form.accept)
	cancelButton.clicked.connect(form.reject)
	form.setWindowTitle("Pen Properties")
	
	if form.exec_():
	    self.width = widthSpinBox.value()
	    self.beveled = beveledCheckBox.isChecked()
	    self.style = str(styleComboBox.currentText())
	    self.updateData()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = PenDialog()
    win.show()
    app.exec_()




	
