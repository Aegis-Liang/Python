import sys,math,random,string
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class NumberDialog(QDialog):
    def __init__(self, format, parent=None):
	super(NumberDialog, self).__init__(parent)

	thousandsLabel = QLabel("&Thousands separator:")
	self.thousandsEdit = QLineEdit(format["thousandsseparator"])
	thousandsLabel.setBuddy(self.thousandsEdit)
	decimalMarkerLabel = QLabel("Decimal $marker:")
	self.decimalMarkerEdit = QLineEdit(format["decimalmarker"])
	decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)
	decimalPlacesLabel = QLabel("&Decimal places:")
	self.decimalPlacesSpinBox = QSpinBox()
	decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)
	self.decimalPlacesSpinBox.setRange(0, 6)
	self.decimalPlacesSpinBox.setValue(format["decimalplaces"])
	self.redNegativesCheckBox = QCheckBox("&Red negative numbers")
	self.redNegativesCheckBox.setChecked(format["rednegatives"])

	buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
	self.format = format.copy()

	grid = QGridLayout()
	grid.addWidget(thousandsLabel, 0, 0)
	grid.addWidget(self.thousandsEdit, 0, 1)
	grid.addWidget(decimalMarkerLabel, 1, 0)
	grid.addWidget(self.decimalMarkerEdit, 1, 1)
	grid.addWidget(decimalPlacesLabel, 2, 0)
	grid.addWidget(self.decimalPlacesSpinBox, 2, 1)
	grid.addWidget(self.redNegativesCheckBox, 3, 0, 1, 2)
	grid.addWidget(buttonBox, 4, 0, 1, 2)
	self.setLayout(grid)

	buttonBox.accepted.connect(self.accept)
	buttonBox.rejected.connect(self.reject)
	self.setWindowTitle("Number format")

    def accept(self):
	class ThousandsError(Exception): pass 
	class DecimalError(Exception): pass 
	Punctuation = frozenset(" ,;:.")

	thousands = str(self.thousandsEdit.text())
	decimal = str(self.decimalMarkerEdit.text())
	try:
	    if len(decimal) == 0:
		raise DecimalError("The decimal marker may not be empty.")
	    if len(thousands) > 1:
		raise ThousandsError("The thousands separator may only be empty or one charactor.")
	    if len(decimal) > 1:
		raise DecimalError("The decimal marker must be one character.")
	    if thousands == decimal:
		raise ThousandsError("The thousands separator and decimal marker must be different.")
	    if thousands and thousands not in Punctuation:
		raise ThousandsError("The thousands separator must be in Punctuation.")
	    if decimal and decimal not in Punctuation:
		raise DecimalError("The decimal marker must be a punctuation symbol.")
	except ThousandsError as e:
	    QMessageBox.warning(self, "Thousands separator error:", str(e))
	    self.thousandsEdit.selectAll()
	    self.thousandsEdit.setFocus()
	    return 
	except DecimalError as e:
	    QMessageBox.warning(self, "Decimal marker error:", str(e))
	    self.decimalMarkerEdit.selectAll()
	    self.decimalMarkerEdit.setFocus()
	    return

	self.format["thousandsseparator"] = thousands
	self.format["decimalmarker"] = decimal
	self.format["decimalplaces"] = self.decimalPlacesSpinBox.value()
	self.format["rednegatives"] = self.redNegativesCheckBox.isChecked()

	QDialog.accept(self)

    def numberFormat(self):
	return self.format

class NumberModelessDialog(QDialog):
    changed = pyqtSignal()

    def __init__(self, format, parent=None):
	super(NumberModelessDialog, self).__init__(parent)
	self.setAttribute(Qt.WA_DeleteOnClose)
	punctuationRe = QRegularExpression(r"[ ,;:.]")

	thousandsLabel = QLabel("&Thousands separator:")
	self.thousandsEdit = QLineEdit(format["thousandsseparator"])
	thousandsLabel.setBuddy(self.thousandsEdit)
	self.thousandsEdit.setMaxLength(1)
	self.thousandsEdit.setValidator(QRegularExpressionValidator(punctuationRe, self))

	decimalMarkerLabel = QLabel("Decimal $marker:")
	self.decimalMarkerEdit = QLineEdit(format["decimalmarker"])
	decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)
	self.decimalMarkerEdit.setMaxLength(1)
	self.decimalMarkerEdit.setValidator(QRegularExpressionValidator(punctuationRe, self))

	decimalPlacesLabel = QLabel("&Decimal places:")
	self.decimalPlacesSpinBox = QSpinBox()
	decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)
	self.decimalPlacesSpinBox.setRange(0, 6)
	self.decimalPlacesSpinBox.setValue(format["decimalplaces"])
	
	self.redNegativesCheckBox = QCheckBox("&Red negative numbers")
	self.redNegativesCheckBox.setChecked(format["rednegatives"])

	buttonBox = QDialogButtonBox(QDialogButtonBox.Apply | QDialogButtonBox.Close)
	self.format = format

	grid = QGridLayout()
	grid.addWidget(thousandsLabel, 0, 0)
	grid.addWidget(self.thousandsEdit, 0, 1)
	grid.addWidget(decimalMarkerLabel, 1, 0)
	grid.addWidget(self.decimalMarkerEdit, 1, 1)
	grid.addWidget(decimalPlacesLabel, 2, 0)
	grid.addWidget(self.decimalPlacesSpinBox, 2, 1)
	grid.addWidget(self.redNegativesCheckBox, 3, 0, 1, 2)
	grid.addWidget(buttonBox, 4, 0, 1, 2)
	self.setLayout(grid)
	
	buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.apply)
	buttonBox.rejected.connect(self.reject)
	self.setWindowTitle("Number format")

    def apply(self):
	thousands = str(self.thousandsEdit.text())
	decimal = str(self.decimalMarkerEdit.text())
	if thousands == decimal:
	    QMessageBox.warning(self, "Thousands separator error")
	    self.thousandsEdit.selectAll()
	    self.thousandsEdit.setFocus()
	    return 
	if len(decimal) == 0:
	    QMessageBox.warning(self, "Decimal marker cannot is empty.")
	    self.decimalMarkerEdit.selectAll()
	    self.decimalMarkerEdit.setFocus()
	    return

	self.format["thousandsseparator"] = thousands
	self.format["decimalmarker"] = decimal
	self.format["decimalplaces"] = self.decimalPlacesSpinBox.value()
	self.format["rednegatives"] = self.redNegativesCheckBox.isChecked()

	self.changed.emit()

class NumberLiveDialog(QDialog):
    changed = pyqtSignal()

    def __init__(self, format, callback, parent=None):
	super(NumberLiveDialog, self).__init__(parent)
	self.format = format
	self.callback = callback
	
	self.setAttribute(Qt.WA_DeleteOnClose)
	punctuationRe = QRegularExpression(r"[ ,;:.]")

	thousandsLabel = QLabel("&Thousands separator:")
	self.thousandsEdit = QLineEdit(format["thousandsseparator"])
	thousandsLabel.setBuddy(self.thousandsEdit)
	self.thousandsEdit.setMaxLength(1)
	self.thousandsEdit.setValidator(QRegularExpressionValidator(punctuationRe, self))

	decimalMarkerLabel = QLabel("Decimal $marker:")
	self.decimalMarkerEdit = QLineEdit(format["decimalmarker"])
	decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)
	self.decimalMarkerEdit.setMaxLength(1)
	self.decimalMarkerEdit.setValidator(QRegularExpressionValidator(punctuationRe, self))

	decimalPlacesLabel = QLabel("&Decimal places:")
	self.decimalPlacesSpinBox = QSpinBox()
	decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)
	self.decimalPlacesSpinBox.setRange(0, 6)
	self.decimalPlacesSpinBox.setValue(format["decimalplaces"])
	
	self.redNegativesCheckBox = QCheckBox("&Red negative numbers")
	self.redNegativesCheckBox.setChecked(format["rednegatives"])

	grid = QGridLayout()
	grid.addWidget(thousandsLabel, 0, 0)
	grid.addWidget(self.thousandsEdit, 0, 1)
	grid.addWidget(decimalMarkerLabel, 1, 0)
	grid.addWidget(self.decimalMarkerEdit, 1, 1)
	grid.addWidget(decimalPlacesLabel, 2, 0)
	grid.addWidget(self.decimalPlacesSpinBox, 2, 1)
	grid.addWidget(self.redNegativesCheckBox, 3, 0, 1, 2)
	self.setLayout(grid)
	
	self.thousandsEdit.textEdited.connect(self.checkAndFix)
	self.decimalMarkerEdit.textEdited.connect(self.checkAndFix)
	self.decimalPlacesSpinBox.valueChanged.connect(self.apply)
	self.redNegativesCheckBox.toggled.connect(self.apply)

	self.setWindowTitle("Number format")

    def checkAndFix(self):
	thousands = self.thousandsEdit.text()
	decimal = self.decimalMarkerEdit.text()
	if thousands == decimal:
	    self.thousandsEdit.clear()
	    self.thousandsEdit.setFocus()
	if len(decimal) == 0:
	    self.decimalMarkerEdit.setText(".")
	    self.decimalMarkerEdit.selectAll()
	    self.decimalMarkerEdit.setFocus()
	self.apply()

    def apply(self):
	thousands = self.thousandsEdit.text()
	decimal = self.decimalMarkerEdit.text()

	self.format["thousandsseparator"] = thousands
	self.format["decimalmarker"] = decimal
	self.format["decimalplaces"] = self.decimalPlacesSpinBox.value()
	self.format["rednegatives"] = self.redNegativesCheckBox.isChecked()

	self.callback()

class Form(QDialog):
    X_MAX = 26
    Y_MAX = 60

    def __init__(self, parent=None):
	super(Form, self).__init__(parent)

	self.numberDlg = None
	self.format = { "thousandsseparator":",", "decimalmarker":".", 
                "decimalplaces":2, "rednegatives": False } 
	self.numbers = {}
	for x in range(self.X_MAX):
	    for y in range(self.Y_MAX):
		self.numbers[(x,y)] = 10000 * random.random() - 5000

	self.table = QTableWidget()
	modalButton = QPushButton("Set numbe format...(&Modal)")
	modelessButton = QPushButton("Set number format...(M&odeless)")
	liveButton = QPushButton("Set number format...(&Live)")

	buttonLayout = QHBoxLayout()
	buttonLayout.addStretch()
	buttonLayout.addWidget(modalButton)
	buttonLayout.addWidget(modelessButton)
	buttonLayout.addWidget(liveButton)
	layout = QVBoxLayout()
	layout.addWidget(self.table)
	layout.addLayout(buttonLayout)
	self.setLayout(layout)

	modalButton.clicked.connect(self.setNumberFormatByModal)
	modelessButton.clicked.connect(self.setNumberFormatByModeless)
	liveButton.clicked.connect(self.setNumberFormatByLive)

	self.setWindowTitle("Set Number Format")
	self.refreshTable()

    def refreshTable(self):
	self.table.clear()
	self.table.setRowCount(self.Y_MAX)
	self.table.setColumnCount(self.X_MAX)
	self.table.setHorizontalHeaderLabels(list(string.ascii_uppercase))

	for x in range(self.X_MAX):
	    for y in range(self.Y_MAX):
		fraction, whole = math.modf(self.numbers[(x,y)])
		sign = "-" if whole < 0 else ""
		whole = "{0}".format(int(math.floor(abs(whole))))
		digits = []
		for i, digit in enumerate(reversed(whole)):
		    if i and i % 3 == 0:
			digits.insert(0, self.format["thousandsseparator"])
		    digits.insert(0, digit)
		if self.format["decimalplaces"]:
		    fraction = "{0:.7f}".format(abs(fraction))
		    fraction = self.format["decimalmarker"] + fraction[2:self.format["decimalplaces"]+2]
		else:
		    fraction = ""
		text = "{0}{1}{2}".format(sign, "".join(digits), fraction)
		item = QTableWidgetItem(text)
		item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
		if sign and self.format["rednegatives"]:
		    item.setBackground(Qt.red)
		self.table.setItem(y, x, item)

    def setNumberFormatByModal(self):
	dlg = NumberDialog(self.format, self)
	if dlg.exec_():
	    self.format = dlg.numberFormat()
	    self.refreshTable()

    def setNumberFormatByModeless(self):
	dlg = NumberModelessDialog(self.format, self)
	dlg.show()
	dlg.changed.connect(self.refreshTable)

    def setNumberFormatByLive(self):
	if self.numberDlg is None:
	    self.numberDlg = NumberLiveDialog(self.format, self.refreshTable, self)
	self.numberDlg.show()
	self.numberDlg.raise_()
	self.numberDlg.activateWindow()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
