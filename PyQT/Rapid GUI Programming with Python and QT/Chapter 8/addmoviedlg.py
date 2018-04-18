from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_addmoviedlg import Ui_AddEditMovieDlg
from moviedata import *

class AddEditMovieDialog(QDialog, Ui_AddEditMovieDlg):
	def __init__(self, movies, movie=None, parent=None):
		super(AddEditMovieDialog, self).__init__(parent)

		self.setupUi(self)

		self.movies = movies
		self.movie = movie 
		self.acquiredDateEdit.setDisplayFormat("ddd MMM d, yyyy")
		if movie is not None:
			self.titleLineEdit.setText(movie.title)
			self.yearSpinBox.setValue(movie.year)
			self.minutesSpinBox.setValue(movie.minutes)
			self.acquiredDateEdit.setDate(movie.acquired)
			self.acquiredDateEdit.setEnabled(False)
			self.notesTextEdit.setPlainText(movie.notes)
			self.notesTextEdit.setFocus()
			self.buttonBox.button(QDialogButtonBox.Ok).setText("&Accept")
			self.setWindowTitle("Edit Movie")
		else:
			today = QDate.currentDate()
			self.acquiredDateEdit.setDateRange(today.addDays(-5), today)
			self.acquiredDateEdit.setDate(today)
			self.titleLineEdit.setFocus()

		self.titleLineEdit.textEdited.connect(self.titleEdited)
		self.titleEdited("")

	def titleEdited(self, e):
		self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(
			self.titleLineEdit.text() != "")

	def accept(self):
		title = self.titleLineEdit.text()
		year = self.yearSpinBox.value()
		minutes = self.minutesSpinBox.value()
		notes = self.notesTextEdit.toPlainText()
		if self.movie is None:
			acquired = self.acquiredDateEdit.date()
			self.movie = Movie(title, year, minutes, acquired, notes)
			self.movies.add(self.movie)
		else:
			self.movies.updateMovies(self.movie, title, year, minutes, notes)
		QDialog.accept(self)
		