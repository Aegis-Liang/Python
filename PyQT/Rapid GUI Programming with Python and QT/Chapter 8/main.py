import os
import platform
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
from moviedata import *
from addmoviedlg import AddEditMovieDialog

ImagePath = os.path.dirname(__file__) + "/images/"

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)

		self.movies = MovieContainer()
		self.table = QTableWidget()
		self.setCentralWidget(self.table)
		self.updateTable()

		self.dirty = False
		self.printer = None

		self.statusBar().showMessage("Ready")
		
		# file menu
		fileNewAction = self.createAction("&New", QKeySequence.New, 
			QIcon(ImagePath+"filenew.png"), "new file")
		fileNewAction.triggered.connect(self.fileNew)
		
		fileOpenAction = self.createAction("&Open", QKeySequence.Open,
			QIcon(ImagePath+ "fileopen.png"), "open file")
		fileOpenAction.triggered.connect(self.fileOpen)
		
		fileSaveAction = self.createAction("&Save", QKeySequence.Save, 
			QIcon(ImagePath+"filesave.png"), "save file")
		fileSaveAction.triggered.connect(self.fileSave)
		
		fileSaveAsAction = self.createAction("Save &as","Atl+a", 
			QIcon(ImagePath+"filesaveas.png"), "Save as new file")
		fileSaveAsAction.triggered.connect(self.fileSaveAs)
		
		fileImportDomAction = self.createAction("&Import from DOM", "Ctrl+I", 
			tip="Import file from DOM")
		fileImportDomAction.triggered.connect(self.fileImportDom)
		
		fileExportXmlAction = self.createAction("&Export to XML file", "Ctrl+E",
			tip="Export to xml file")
		fileExportXmlAction.triggered.connect(self.fileExportXml)

		filePrintAction = self.createAction("&Print", QKeySequence.Print, 
			QIcon(ImagePath+"fileprint.png"), "Print file")
		filePrintAction.triggered.connect(self.filePrint)
		
		fileQuitAction = self.createAction("&Quit", "Ctrl+Q", 
			QIcon(ImagePath+"filequit.png"), "Close the application")
		fileQuitAction.triggered.connect(self.close)
		
		self.fileMenu = self.menuBar().addMenu("&File")
		self.fileMenuActions = (fileNewAction, fileOpenAction, 
			fileSaveAction, fileSaveAsAction, None, 
			fileImportDomAction, fileExportXmlAction, None, 
			filePrintAction,None, 
			fileQuitAction)
		self.addActions(self.fileMenu, self.fileMenuActions)

		# edit menu
		editAddAction = self.createAction("&Add", "Ctrl+A", QIcon(ImagePath+"editadd.png"), 
			"Add movie data")
		editAddAction.triggered.connect(self.editAdd)
		editEditAction = self.createAction("&Edit", "Ctrl+E", QIcon(ImagePath+"editedit.png"),
			"Edit the current movie")
		editEditAction.triggered.connect(self.editEdit)

		self.editMenu = self.menuBar().addMenu("&Edit")
		self.editMenuActions = (editAddAction, editEditAction)
		self.addActions(self.editMenu, self.editMenuActions)
		
		# help menu 
		helpHelpAction = self.createAction("&Help", QKeySequence.HelpContents)
		helpHelpAction.triggered.connect(self.helpHelp)
		helpAboutAction = self.createAction("&About")
		helpAboutAction.triggered.connect(self.helpAbout)
		helpMenu = self.menuBar().addMenu("&Help")
		self.addActions(helpMenu, (helpHelpAction, helpAboutAction))

		fileToolbar = self.addToolBar("File")
		fileToolbar.setObjectName("FileToolBar")
		self.addActions(fileToolbar, (fileNewAction, fileOpenAction, 
			fileSaveAction, fileSaveAsAction))

		# settings
		settings = QSettings()
		self.recentFiles = []
		if settings.value("RecentFiles"):
			self.recentFiles = settings.value("RecentFiles")
		if settings.value("MainWindow/Geometry"):
			self.restoreGeometry( QByteArray(settings.value("MainWindow/Geometry")) )
		if settings.value("MainWindow/State"):
			self.restoreState( QByteArray(settings.value("MainWindow/State")) )


		self.setWindowTitle("x01.MainWindow")

	def createAction(self, text, shortcut=None, icon=None, tip=None):
		action = QAction(text, self)
		if icon is not None:
			action.setIcon(icon)
		if shortcut is not None:
			action.setShortcut(shortcut)
		if tip is not None:
			action.setToolTip(tip)
		return action 
	def addActions(self, target, actions):
		for action in actions:
			if action is None:
				target.addSeparator()
			else:
				target.addAction(action)
	def closeEvent(self, e):
		if self.okToCountiue():
			settings = QSettings()
			settings.setValue("LastFile", self.filename)
			settings.setValue("RecentFiles", self.recentFiles)
			settings.setValue("MainWindow/Geometry", self.saveGeometry())
			settings.setValue("MainWindow/State", self.saveState())
		else:
			e.ignore()
	def okToCountiue(self):
		if self.movies.dirty:
			reply = QMessageBox.question(self, self.windowTitle(), "Save changes?", 
				QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
			if reply == QMessageBox.Yes:
				return self.fileSave()
			elif reply == QMessageBox.No:
				return True
			else:
				return False
		return True

	def updateTable(self, current=None):
		self.table.clear()
		self.table.setRowCount(len(self.movies))
		self.table.setColumnCount(5)
		self.table.setHorizontalHeaderLabels(["Title", "Year", "Minutes", "Acquired", "Notes"])
		self.table.setAlternatingRowColors(True)
		self.table.setEditTriggers(QTableWidget.NoEditTriggers)
		self.table.setSelectionBehavior(QTableWidget.SelectRows)
		self.table.setSelectionMode(QTableWidget.SingleSelection)

		selected = None
		for r, m in enumerate(self.movies):
			item = QTableWidgetItem(m.title)
			if current is not None and current == id(m):
				selected = item
			item.setData(Qt.UserRole, int(id(m)))
			self.table.setItem(r, 0, item)
			year = m.year
			if year != 1890:
				item = QTableWidgetItem("{0}".format(year))
				item.setTextAlignment(Qt.AlignCenter)
				self.table.setItem(r, 1, item)
			minutes = m.minutes
			if minutes != 0:
				item = QTableWidgetItem("{0}".format(minutes))
				item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
				self.table.setItem(r, 2, item)
			item = QTableWidgetItem(m.acquired.toString(Qt.ISODate))
			item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
			self.table.setItem(r, 3, item)
			notes = m.notes
			if len(notes) > 40:
				notes = notes[:39] + "..."
			self.table.setItem(r, 4, QTableWidgetItem(notes))
		self.table.resizeColumnsToContents()
		if selected is not None:
			selected.setSelected(True)
			self.table.setCurrentItem(selected)
			self.table.scrollToItem(selected)

	# file actions
	def fileNew(self): 
		if not self.okToCountiue():
			return 
		self.movies.clear()
		self.statusBar().clearMessage()
		self.updateTable()

	def fileOpen(self): 
		if not self.okToCountiue():
			return
		path = QFileInfo(self.movies.filename).path() if self.movies.filename is not None else "."
		filename, ext = QFileDialog.getOpenFileName(self, "Load Movie Data", path, 
			"Movie files ({0})".format(self.movies.formats()) )
		print(filename)
		if filename is not None:
			ok, msg = self.movies.load(filename)
			self.statusBar().showMessage(msg)
			self.updateTable()

	def fileSave(self): 
		if self.movies.filename is None:
			return self.fileSaveAs()
		else:
			ok, msg = self.movies.save()
			self.statusBar().showMessage(msg)
			return ok 

	def fileSaveAs(self): pass
	def fileImportDom(self):
		self.fileImport("dom")
	def fileImport(self, format="dom"):
		if not self.okToCountiue():
			return 
		path = QFileInfo(self.movies.filename).path() if self.movies.filename is not None else "."
		filename, ext = QFileDialog.getOpenFileName(self, "Import Movie Data", path, "Movie files (*.xml)")
		if filename is not None:
			if format == "dom":
				ok, msg = self.movies.importDom(filename)
			elif format == "sax":
				pass
			self.statusBar().showMessage(msg)
			self.updateTable()

	def fileExportXml(self):
		filename = self.movies.filename
		if filename is None:
			filename = "."
		else:
			i = filename.rindex(".")
			if i > 0:
				filename = filename[:i]
			filename += ".xml"
		filename, ext = QFileDialog.getSaveFileName(self, "Export Movie Data", filename, "Movie xml files(*.xml)")
		if filename is not None:
			if "." not in filename :
				filename += ".xml"
			ok, msg = self.movies.exportXml(filename)
			self.statusBar().showMessage(msg)

	def filePrint(self): pass

	# edit actions
	def editAdd(self):
		dlg = AddEditMovieDialog(self.movies, None, self)
		if dlg.exec_():
			self.updateTable(id(dlg.movie))
			
	def editEdit(self):pass

	# help actions
	def helpAbout(self):
		QMessageBox.about(self, self.windowTitle(),
			"""<b>{0}</b> 
			<p>version: {1}
			<p>This application use <b>Python {2}</b> - <b>PyQt {3}</b> on <b>{4}</b>"""
			.format( self.windowTitle(), "1.0.0", 
				platform.python_version(), PYQT_VERSION_STR, platform.system() )
		)
	def helpHelp(self): pass

		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	app.exec_()

