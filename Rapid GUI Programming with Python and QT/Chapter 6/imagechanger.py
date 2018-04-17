import os
import platform
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *

import helpform
import newimagedlg
import resources_rc

#ImagePath = os.path.dirname(os.path.abspath(__file__)) + "/images/"
__version__ = "1.0.0"

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)

		self.image = QImage()
		self.dirty = False
		self.filename = None 
		self.mirroredvertically = False
		self.mirroredhorizontally = False 

		self.imageLabel = QLabel()
		self.imageLabel.setMinimumSize(200,200)
		self.imageLabel.setAlignment(Qt.AlignCenter)
		self.imageLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
		self.setCentralWidget(self.imageLabel)

		self.listWidget = QListWidget()
		self.logDockWidget = QDockWidget("Log", self)
		self.logDockWidget.setObjectName("LogDockWidget")
		self.logDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
		self.logDockWidget.setWidget(self.listWidget)
		self.addDockWidget(Qt.RightDockWidgetArea, self.logDockWidget)

		self.printer = None
		
		self.sizeLabel = QLabel()
		self.sizeLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
		status = self.statusBar()
		status.setSizeGripEnabled(False)
		status.addPermanentWidget(self.sizeLabel)
		status.showMessage("Ready")

		fileNewAction = self.createAction("&New", self.fileNew, 
			QKeySequence.New, "filenew", "Create a image file")
		fileOpenAction = self.createAction("&Open", self.fileOpen, 
			QKeySequence.Open, "fileopen", "Open a exist image file")
		fileSaveAction = self.createAction("&Save", self.fileSave,
			QKeySequence.Save, "filesave", "Save the image")
		fileSaveAsAction = self.createAction("Save &as", self.fileSaveAs,
			icon="filesaveas", tip="Save image using a new filename")
		filePrintAction = self.createAction("&Print", self.filePrint, 
			QKeySequence.Print, "fileprint", "Print the image")
		fileQuitAction = self.createAction("&Quit", self.close,
			"Ctrl+Q", "filequit", "Close the application")
		
		self.fileMenu = self.menuBar().addMenu("&File")
		self.fileMenuActions = (fileNewAction, fileOpenAction, 
			fileSaveAction, fileSaveAsAction, None, filePrintAction, fileQuitAction)
		

		editInvertAction = self.createAction("&Invert", self.editInvert,
			"Ctrl+I", "editinvert", "Invert the image's color", True, "toggled")
		editSwapRedAndBlueAction = self.createAction("Sw&ap red and blue", self.editSwapRedAndBlue,
			"Ctrl+A", "editswap", "Swap image's red and blue", True, "toggled")
		editZoomAction = self.createAction("&Zoom", self.editZoom,
			"Alt+Z", "editzoom", "Zoom the image")
		
		mirrorGroup = QActionGroup(self)
		editUnMirrorAction = self.createAction("&Unmirror", self.editUnMirror,
			"Ctrl+U", "editunmirror", "Unmirror the image", True, "toggled")
		editUnMirrorAction.setChecked(True)
		mirrorGroup.addAction(editUnMirrorAction)
		editMirrorHorizontalAction = self.createAction("Mirror &horizontally", self.editMirrorHorizontal,
			"Ctrl+H", "editmirrorhoriz", "Horizontal mirror the image", True, "toggled")
		mirrorGroup.addAction(editMirrorHorizontalAction)
		editMirrorVerticalAction = self.createAction("Mirror &Vertically", self.editMirrorVertical,
			"Ctrl+V", "editmirrorvert", "Vertiacl mirror the image", True, "toggled")
		mirrorGroup.addAction(editMirrorVerticalAction)
		
		editMenu = self.menuBar().addMenu("&Edit")
		self.addActions(editMenu, (editInvertAction, editSwapRedAndBlueAction, editZoomAction))
		mirrorMenu = editMenu.addMenu(QIcon(":/editmirror.png"), "&Mirror")
		self.addActions( mirrorMenu, (editUnMirrorAction, editMirrorHorizontalAction,
			editMirrorVerticalAction) )
		
		helpHelpAction = self.createAction("&Help", self.helpHelp, QKeySequence.HelpContents)
		helpLogAction = self.createAction("Log", self.helpLog)
		helpAboutAction = self.createAction("&About image changer", self.helpAbout)
		helpMenu = self.menuBar().addMenu("&Help")
		self.addActions(helpMenu, (helpHelpAction, helpLogAction, helpAboutAction))

		fileToolbar = self.addToolBar("File")
		fileToolbar.setObjectName("FileToolBar")
		self.addActions(fileToolbar, (fileNewAction, fileOpenAction, 
			fileSaveAction, fileSaveAsAction))
		editToolbar = self.addToolBar("Edit")
		editToolbar.setObjectName("EditToolBar")
		self.addActions(editToolbar, (editInvertAction, editSwapRedAndBlueAction, 
			editUnMirrorAction, editMirrorHorizontalAction, editMirrorVerticalAction))
		self.zoomSpinBox = QSpinBox()
		self.zoomSpinBox.setRange(1,400)
		self.zoomSpinBox.setSuffix(" %")
		self.zoomSpinBox.setValue(100)
		self.zoomSpinBox.setToolTip("Zoom the image")
		self.zoomSpinBox.setFocusPolicy(Qt.NoFocus)
		self.zoomSpinBox.valueChanged.connect(self.showImage)
		editToolbar.addWidget(self.zoomSpinBox)

		self.addActions(self.imageLabel, (editInvertAction, editSwapRedAndBlueAction,
			editUnMirrorAction, editMirrorHorizontalAction, editMirrorVerticalAction))
		self.resetableActions = ( (editInvertAction, False), 
			(editSwapRedAndBlueAction, False), (editUnMirrorAction, False) )

		settings = QSettings()
		self.recentFiles = []
		if settings.value("RecentFiles"):
			self.recentFiles = settings.value("RecentFiles")
		if settings.value("MainWindow/Geometry"):
			self.restoreGeometry( QByteArray(settings.value("MainWindow/Geometry")) )
		if settings.value("MainWindow/State"):
			self.restoreState( QByteArray(settings.value("MainWindow/State")) )

		self.updateFileMenu()

		self.setWindowTitle("Image changer")
		QTimer.singleShot(0, self.loadInitialFile)

	def createAction(self, text, slot=None, shortcut=None, icon=None,
					tip=None, checkable=False, signal="triggered"):
		action = QAction(text, self)
		actSignal = None
		if signal == "triggered":
			actSignal = action.triggered
		elif signal == "toggled":
			actSignal = action.toggled
		elif signal == "changed":
			actSignal = action.changed 
		elif signal == "hovered":
			actSignal = action.hovered
		else:
			actSignal = action.triggered

		if icon is not None:
			action.setIcon(QIcon(":/{0}.png".format(icon)))
		if shortcut is not None:
			action.setShortcut(shortcut)
		if tip is not None:
			action.setToolTip(tip)
		if slot is not None:
			actSignal.connect(slot)
		if checkable:
			action.setCheckable(True)
		return action 

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
		if self.dirty:
			reply = QMessageBox.question(self, "Image changer", "Save changes?", 
				QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
			if reply == QMessageBox.Yes:
				return self.fileSave()
			elif reply == QMessageBox.No:
				return True
			else:
				return False
		return True

	# file actions
	def fileNew(self): 
		if not self.okToCountiue():
			return 
		dialog = newimagedlg.NewImageDlg(self)
		if dialog.exec_():
			self.addRecentFile(self.filename)
			self.image = QImage()
			for action, check in self.resetableActions:
				action.setChecked(check)
			self.image = dialog.image()
			self.filename = None 
			self.dirty = True 
			self.showImage()
			self.sizeLabel.setText("{0} X {1}"
				.format(self.image.width(), self.image.height()))
			self.updateStatus("Create new image")

	def fileOpen(self): 
		if not self.okToCountiue():
			return
		dir = os.path.dirname(self.filename if self.filename is not None else ".")
		formats = ["*.{0}".format(format.data().decode("ascii").lower()) 
			for format in QImageReader.supportedImageFormats()]
		fname, ext = QFileDialog.getOpenFileName( self, "Image Changer - Choose Image", dir,
			"Image files {0}".format(" ".join(formats)) ) 
		if fname:
			self.loadFile(fname=fname)

	def fileSave(self): 
		if self.image.isNull():
			return True 
		if self.filename is None:
			return self.fileSaveAs()
		else:
			if self.image.save(self.filename, None):
				self.updateStatus("Save as {0}".format(self.filename))
				self.dirty = False
				return True
			else:
				self.updateStatus("Failed to save {0}".format(self.filename))
				return False

	def fileSaveAs(self): 
		if self.image.isNull():
			return True
		fname = self.filename if self.filename is not None else "."
		formats = ( ["*.{0}".format(format.data().decode("ascii").lower()) 
			for format in QImageWriter.supportedImageFormats()] )
		fname, ext = QFileDialog.getSaveFileName( self, "Image Chnager", fname, 
			"Image files ({0})".format(" ".join(formats)) ) 
		if fname:
			if "." not in fname:
				fname += ".png"
			self.addRecentFile(fname)
			self.filename = fname 
			return self.fileSave()
		return False 

	def filePrint(self): 
		if self.image.isNull():
			return 
		if self.printer is None:
			self.printer = QPrinter(QPrinter.HighResolution)
			self.printer.setPageSize(QPrinter.Letter)
		dlg = QPrintDialog(self.printer, self)
		if dlg.exec_():
			painter = QPainter(self.printer)
			rect = painter.viewport()
			size = self.image.size()
			size.scale(rect.size(), Qt.KeepAspectRatio)
			painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
			painter.drawImage(rect, self.image, rect)

	# edit actions
	def editInvert(self, on):
		if self.image.isNull():
			return 
		self.image.invertPixels()
		self.showImage()
		self.dirty = True
		self.updateStatus("Inverted" if on else "Uninverted")

	def editSwapRedAndBlue(self, on):
		if self.image.isNull():
			return 
		self.image = self.image.rgbSwapped()
		self.showImage()
		self.dirty = True 
		self.updateStatus("Swaped Red and Blue" if on else "Unswap red and blue")

	def editZoom(self): 
		if self.image.isNull():
			return 
		percent, ok = QInputDialog.getInt(self, "Image Changer - Zoom",
			"Percent:", self.zoomSpinBox.value(), 1, 400)
		if ok:
			self.zoomSpinBox.setValue(percent)

	def editUnMirror(self, on):
		if self.image.isNull():
			return 
		if self.mirroredhorizontally:
			self.editMirrorHorizontal(False)
		if self.mirroredvertically:
			self.editMirrorVertical(False)

	def editMirrorHorizontal(self, on):
		if self.image.isNull():
			return 
		self.image = self.image.mirrored(True, False)
		self.showImage()
		self.mirroredhorizontally = not self.mirroredhorizontally
		self.dirty = True 
		self.updateStatus("Mirror horizontally" if on else "Unmirror horizontally")

	def editMirrorVertical(self, on):
		if self.image.isNull():
			return 
		self.image = self.image.mirrored(False, True)
		self.showImage()
		self.mirroredvertically = not self.mirroredvertically
		self.dirty = True 
		self.updateStatus("Mirror vertically" if on else "Unmirror vertically")

	# help actions
	def helpAbout(self):
		QMessageBox.about(self, "About Image Changer",
			"""<b>Image Changer</b> v {0}
			<p>This application can be used to perform
			simple image manipulations.
			<p>Python {1} - Qt {2} - PyQt {3} on {4}"""
			.format( __version__, platform.python_version(),
				QT_VERSION_STR, PYQT_VERSION_STR,
				platform.system() )
		)

	def helpLog(self):
		if self.logDockWidget.isHidden():
			self.logDockWidget.show()
		
	def helpHelp(self):
		help = helpform.HelpForm("index.html", self)
		help.show()

	# others
	def showImage(self, percent=None):
		if self.image.isNull():
			return 
		if percent is None:
			percent = self.zoomSpinBox.value()
		factor = percent / 100
		width = self.image.width() * factor
		height = self.image.height() * factor
		image = self.image.scaled(width, height, Qt.KeepAspectRatio)
		self.imageLabel.setPixmap(QPixmap.fromImage(image))

	def loadInitialFile(self):
		settings = QSettings()
		if settings.value("LastFile"):
			fname = settings.value("LastFile")
			if fname and QFile.exists(fname):
				self.loadFile(fname=fname)

	def loadFile(self, trigger=False, fname=None):
		if fname is None:
			action = self.sender()
			if isinstance(action, QAction):
				fname = str(action.data())
				if fname in self.recentFiles:
					self.recentFiles.remove(fname)
				self.recentFiles.insert(0,fname)
				#print(fname)
				if not self.okToCountiue():
					return 
			else:
				return 
		if fname:
			self.filename = None 
			image = QImage(fname)
			if image.isNull():
				message = "Failed to read {0}".format(fname)
			else:
				self.addRecentFile(fname)
				self.image = QImage()
				for action, check in self.resetableActions:
					action.setChecked(check)
				self.image = image
				self.filename = fname
				self.showImage()
				self.dirty = False
				self.sizeLabel.setText("{0} X {1}".format(image.width(), image.height()))
				message = "Load {0}".format(os.path.basename(fname))
			self.updateStatus(message)
			self.updateFileMenu()

	def addRecentFile(self, fname):
		if fname is None:
			return 
		if fname not in self.recentFiles:
			self.recentFiles.insert(0, fname)
			if len(self.recentFiles) > 9:
				self.recentFiles = self.recentFiles[:9]

	def updateStatus(self, message):
		self.statusBar().showMessage(message)
		self.listWidget.addItem(message)
		if self.filename is not None:
			self.setWindowTitle( "Image Changeer - {0}[*]"
				.format(os.path.basename(self.filename)) )
		elif not self.image.isNull():
			self.setWindowTitle("Image Changer - Unnamed[*]")
		else:
			self.setWindowTitle("Image Changer[*]")
		self.setWindowModified(self.dirty)

	def updateFileMenu(self):
		self.fileMenu.clear()
		self.addActions(self.fileMenu, self.fileMenuActions[:-1])
		recentFiles = []
		for fname in self.recentFiles:
			if QFile.exists(fname):
				recentFiles.append(fname)
		if recentFiles:
			self.fileMenu.addSeparator()
			for i, fname in enumerate(recentFiles):
				action = QAction(QIcon(":/icon.png"), 
					"&{0} {1}".format(i+1, QFileInfo(fname).fileName()), self)	
				action.setData(fname)
				action.triggered.connect(self.loadFile)
				self.fileMenu.addAction(action)
		self.fileMenu.addSeparator()
		self.fileMenu.addAction(self.fileMenuActions[-1])

	def addActions(self, target, actions):
		for action in actions:
			if action is None:
				target.addSeparator()
			else:
				target.addAction(action)


		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	app.exec_()

