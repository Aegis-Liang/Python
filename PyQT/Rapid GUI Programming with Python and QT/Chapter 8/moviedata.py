import bisect
import codecs
import gzip
import pickle
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtXml import *

class Movie(object):
	def __init__(self, title=None, year=1890, minutes=0, acquired=None, notes=None):
		self.title = title
		self.year = year
		self.minutes = minutes
		self.acquired = acquired if acquired is not None else QDate.currentDate()
		self.notes = notes 

class MovieContainer(object):
	MagicNumber = 0x3051E
	FileVersion = 100

	def __init__(self):
		self.filename=None 
		self.movies = []
		self.movieDict = {}
		self.dirty = False

	def key(self, title, year):
		title = str(title).lower()
		if title.startswith("a "):
			title = title[2:]
		elif title.startswith("an "):
			title = title[3:]
		elif title.startswith("the "):
			title = title[4:]
		parts = title.split(" ", 1)
		if parts[0].isdigit():
			title = "{0:08d}".format(int(parts[0]))
			if len(parts) > 1:
				title += parts[1]
		return "{0}\t{1}".format(title.replace(" ", ""), year)

	def clear(self, clearFilename=True):
		self.movies = []
		self.movieFromId = {}
		if clearFilename:
			self.filename = ""
		self.dirty = False

	def movieAtIndex(self, i):
		return self.movies[i][1]

	def add(self, movie):
		if id(movie) in self.movieDict:
			return False 
		key = self.key(movie.title, movie.year)
		bisect.insort_left(self.movies, [key, movie])
		self.movieDict[id(movie)] = movie
		self.dirty = True 
		return True 

	def delete(self, movie):
		if id(movie) not in self.movieDict:
			return False
		key = self.key(movie.title, movie.year)
		i = bisect.bisect_left(self.movies, [key, movie])
		del self.movies[i]
		del self.movieDict[id(movie)]
		self.dirty = True
		return True

	def updateMovies(self, movie, title, year, minutes=None, notes=None):
		if minutes is not None:
			movie.minutes = minutes
		if notes is not None:
			movie.notes = notes 
		if title != movie.title or year != movie.year:
			key = self.key(movie.title, movie.year)
			i = bisect.bisect_left(self.movies, [key,movie])
			self.movies[i][0] = self.key(title,year)
			movie.title = title
			movie.year = year
			self.movies.sort()
		self.dirty = True

	def __iter__(self):
		for pair in iter(self.movies):
			yield pair[1]

	def __len__(self):
		return len(self.movies)

	@staticmethod
	def formats():
		return "*.mpb *mqb *mpt *mqt"

	def save(self, filename=None):
		if filename is not None:
			self.filename = filename
		if self.filename.endswith(".mqb"):
			return self.saveQDataStream()
		elif self.filename.endswith(".mpb"):
			return self.savePickle()
		elif self.filename.endswith(".mqt"):
			return self.saveQTextStream()
		elif self.filename.endswith(".mpt"):
			return self.saveText()
		return False, "Save failed: invalid file extension."

	def load(self, filename=None):
		if filename is not None:
			self.filename = filename
		if self.filename.endswith(".mqb"):
			return self.loadQDataStream()
		elif self.filename.endswith(".mpb"):
			return self.loadPickle()
		elif self.filename.endswith(".mqt"):
			return self.loadQTextStream()
		elif self.filename.endswith(".mpt"):
			return self.loadText()
		return False, "Load failed: invalid file extension."

	def saveQDataStream(self):
		error = None
		fh = None
		try:
			fh = QFile(self.filename)
			if not fh.open(QIODevice.WriteOnly):
				raise IOError(fh.errorString())
			stream = QDataStream(fh)
			stream.writeInt32(MovieContainer.MagicNumber)
			stream.writeInt32(MovieContainer.FileVersion)
			stream.setVersion(QDataStream.Qt_5_9)
			for k, m in self.movies:
				
				#stream << QByteArray(m.title)
				stream.writeQString(str(m.title))
				#print(m.title + " ***Save")
				stream.writeInt16(m.year)
				stream.writeInt16(m.minutes)
				stream.writeQString(m.acquired.toString(Qt.ISODate))
				stream.writeQString(str(m.notes))
				#stream << m.acquired << m.notes 
				#print(m.acquired)
		except EnvironmentError as e:
			error = "Failed to save:{0}".format(e)
		finally:
			if fh is not None:
				fh.close()
			if error is not None:
				return False, error 
			self.dirty = False
			return True, "Save {0} movie records to {1}".format(
				len(self.movies), QFileInfo(self.filename).fileName() )

	def savePickle(self):
		error = None 
		fh = None 
		try:
			fh = gzip.open(self.filename, "wb")
			pickle.dump(self.movies, fh, 2)
		except EnvironmentError as e:
			error = "Failed to save: {0}".format(e)
		finally:
			if fh is not None:
				fh.close()
			if error is not None:
				return False, error 
			self.dirty = False
			return True, "Save {0} movie records to {1}".format(
				len(self.movies), QFileInfo(self.filename).fileName())

	def saveQTextStream(self):
		error = None
		fh = None
		try:
			fh = QFile(self.filename)
			if not fh.open(QIODevice.WriteOnly):
				raise IOError(fh.errorString())
			stream = QTextStream(fh)
			stream.setCodec("utf-8")
			for k, m in self.movies:
				stream << "{{MOVIE}}" << m.title << "\n" \
					<< m.year << " " << m.minutes << " " << m.acquired.toString(Qt.ISODate) \
					<< "\n{{NOTES}}"
				if m.notes is not None:
					stream << "\n" << m.notes 
				stream << "\n{{ENDMOVIE}}\n"
		except EnvironmentError as e:
			error = "Failed to save: {0}".format(e)
		finally:
			if fh is not None:
				fh.close()
			if error is not None:
				return False, error 
			self.dirty = False
			return True, "Save {0} movie records to {1}".format(
				len(self.movies), QFileInfo(self.filename).fileName())

	def saveText(self):
		error = None
		fh = None 
		try:
			fh = codecs.open(self.filename, "w", "utf-8")
			for k, m in self.movies:
				fh.write("{{MOVIE}}")
				fh.write("{0}\n".format(m.title))
				fh.write("{0} {1} {2}\n".format(m.year, m.minutes, m.acquired.toString(Qt.ISODate)))
				fh.write("{{NOTES}}")
				if m.notes is not None:
					fh.write("\n{0}".format(m.notes))
				fh.write("\n{{ENDMOVIE}}\n")
		except EnvironmentError as e:
			error = "Save failed: {0}".format(e)
		finally:
			if fh is not None:
				fh.close()
			if error is not None:
				return False, error 
			self.dirty = False
			return True, "Save {0} movie records to {1}".format(len(self.movies),
				QFileInfo(self.filename).fileName() )

	def loadQDataStream(self):
		error = None
		fh = None
		try:
			fh = QFile(self.filename)
			if not fh.open(QIODevice.ReadOnly):
				raise IOError(fh.errorString())
			stream = QDataStream(fh)
			magic = stream.readInt32()
			if magic != MovieContainer.MagicNumber:
				raise IOError("Unrecognized file type")
			version = stream.readInt32()
			if version < MovieContainer.FileVersion:
				raise IOError("Old and unreadable file format")
			elif version > MovieContainer.FileVersion:
				raise IOError("New and unreadable file format")
			stream.setVersion(QDataStream.Qt_5_9)
			self.clear(False)
			while not stream.atEnd():
				title = stream.readQString()
				year = stream.readInt16()
				minutes = stream.readInt16()
				acs = stream.readQString()
				parts = acs.split("-")
				acquired = QDate(int(parts[0]), int(parts[1]), int(parts[2]))
				notes = stream.readQString()
				self.add(Movie(title, year, minutes, acquired, notes))
		except EnvironmentError as e:
			error = "Load file failed: {0}".format(e)
		finally:
			if fh is not None:
				fh.close()
			if error is not None:
				return False, error 
			self.dirty = False
			return True, "Load {0} movies from {1}".format(len(self.movies), 
				QFileInfo(self.filename).fileName() )

	def loadPickle(self):
		error = None
		fh = None
		try:
			fh = gzip.open(self.filename, "rb")
			self.clear(False)
			self.movies = pickle.load(fh)
			for k, m in self.movies:
				self.movieDict[id(m)] = m
		except EnvironmentError as e:
			error = "Load failed: {0}".format(e)
		finally:
			if fh is not None:
				fh.close()
			if error is not None:
				return False, error
			self.dirty = False
			return True, "Load {0} movies from {1}".format(len(self.movies), 
				QFileInfo(self.filename).fileName() )

	def loadQTextStream(self):
		error = None
		fh = None
		lineNr = 0
		try:
			fh = QFile(self.filename)
			if not fh.open(QIODevice.ReadOnly):
				raise IOError(fh.errorString())
			stream = QTextStream(fh)
			stream.setCodec("utf-8")
			self.clear(False)
			while not stream.atEnd():
				title = year = minutes = acquired = notes = None 
				line = stream.readLine()
				lineNr += 1
				if not line.startswith("{{MOVIE}}"):
					raise ValueError("No movie records found")
				else:
					title = line[len("{{MOVIE}}"):].strip() #).trimmed()
				if stream.atEnd():
					raise ValueError("premature end of file")
				line = stream.readLine()
				lineNr += 1
				parts = line.split(" ")
				if len(parts) != 3:
					raise ValueError("Invalid numeric data")
				year = int(parts[0])
				minutes = int(parts[1])
				ymd = parts[2].split("-")
				if len(ymd) != 3:
					raise ValueError("Invalid acquired data")
				acquired = QDate(int(ymd[0]), int(ymd[1]), int(ymd[2]))
				if stream.atEnd():
					raise ValueError("Premature end of file")
				line = stream.readLine()
				lineNr += 1
				if line != "{{NOTES}}":
					raise ValueError("notes exception")
				notes = ""
				while not stream.atEnd():
					line = stream.readLine()
					lineNr += 1
					if line == "{{ENDMOVIE}}":
						if title is None or year is None or minutes is None or acquired is None or notes is None:
							raise ValueError("Incomplete record")
						self.add(Movie(title, year, minutes, acquired, notes))
						break
					else:
						notes += line + "\n"
				else:
					raise ValueError("missing endmovie marker")
		except (IOError, OSError, ValueError) as e:
			error  = "Error line: {0}, load error: {1}".format(lineNr, e)
		finally:
			if fh is not None:
				fh.close()
			if error is not None:
				return False, error
			self.dirty = False
			return True, "Load {0} movies from {1}".format(len(self.movies),
				QFileInfo(self.filename).fileName() )

	def loadText(self):
		error = None
		fh = None
		lineNr = 0
		try:
			fh = codecs.open(self.filename, "r", "utf-8")
			self.clear(False)
			while True:
				title = year = minutes = acquired = notes = None 
				line = fh.readline()
				if not line:
					break 
				lineNr += 1
				if not line.startswith("{{MOVIE}}"):
					raise ValueError("No movie found")
				else:
					title = line[len("{{MOVIE}}"):].strip()
				line = fh.readline()
				if not line:
					raise ValueError("Premature end of file")
				lineNr += 1
				parts = line.split(" ")
				if len(parts) != 3:
					raise ValueError("Invalid numeric data")
				year = int(parts[0])
				minutes = int(parts[1])
				ymd = parts[2].split("-")
				
				if len(ymd) != 3:
					raise ValueError("Invalid acquired data")
				acquired = QDate(int(ymd[0]), int(ymd[1]), int(ymd[2]))
				line = fh.readline()
				if not line:
					raise ValueError("Premature end of file")
				lineNr += 1
				if line != "{{NOTES}}\n":
					raise ValueError("notes exception")
				notes = ""
				while True:
					line = fh.readline()
					if not line:
						raise ValueError("missing endmovie marker")
					lineNr += 1
					if line == "{{ENDMOVIE}}\n":
						if title is None or year is None or minutes is None or acquired is None or notes is None:
							raise ValueError("Incomplete record")
						self.add(Movie(title, year, minutes, acquired, notes))
						break
					else:
						notes += line 
		except (IOError, OSError, ValueError) as e:
			error = "Load failed line: {0} error: {1}".format(lineNr, e)
		finally:
			if fh is not None:
				fh.close()
			if error is not None:
				return False, error
			self.dirty = False
			return True, "Load {0} movies from {1}".format(len(self.movies), 
				QFileInfo(self.filename).fileName() )
		
	def exportXml(self, filename):
		error = None
		fh = None
		try:
			fh = QFile(filename)
			if not fh.open(QIODevice.WriteOnly):
				raise IOError(fh.errorString())
			stream = QTextStream(fh)
			stream.setCodec("utf-8")
			stream << ("<?xml version='1.0' encoding='{0}' ?>\n"
				"<!DOCTYPE movies>\n"
				"<movies version='1.0'>\n".format("utf-8"))
			for k, m in self.movies:
				stream << ("  <movie year='{0}' minutes='{1}' acquired='{2}'>\n".format(
					m.year, m.minutes, m.acquired.toString(Qt.ISODate))) \
					<< "    <title>" << m.title << "</title>\n    <notes>"
				if m.notes is not None:
					stream << "\n" << m.notes 
				stream << "\n    </notes>\n  </movie>\n"
			stream << "</movies>\n"
		except EnvironmentError as e:
			error = "Failed to export: {0}".format(e)
		finally:
			if fh is not None:
				fh.close()
			if error is not None:
				return False, error 
			self.dirty = False
			return True, "Export {0} movies to {1}".format(len(self.movies),
				QFileInfo(filename).fileName() )

	def importDom(self, filename):
		doc = QDomDocument()
		error = None
		fh = None 
		try:
			fh = QFile(filename)
			if not fh.open(QIODevice.ReadOnly):
				raise IOError(fh.errorString())
			if not doc.setContent(fh):
				raise ValueError("could not parse xml")
		except (IOError, OSError, ValueError) as e:
			error = "Failed to import: {0}".format(e)
		finally:
			if fh is not None:
				fh.close()
			if error is not None:
				return False, error
		
		try:
			self.populateFromDom(doc)
		except ValueError as e:
			return False, "Failed to import: {0}".format(e)
		self.filename = ""
		self.dirty = True
		return True, "Import {0} movie records from {1}".format(len(self.movies), 
			QFileInfo(filename).fileName() )

	def populateFromDom(self, doc):
		root = doc.documentElement()
		if root.tagName() != "movies":
			raise ValueError("not a movies xml file")
		self.clear(False)
		node = root.firstChild()
		while not node.isNull():
			if node.toElement().tagName() == "movie":
				self.readMovieNode(node.toElement())
			node = node.nextSibling()

	def readMovieNode(self, element):
		def getText(node):
			child = node.firstChild()
			text = ""
			while not child.isNull():
				if child.nodeType() == QDomNode.TextNode:
					text += child.toText().data()
				child = child.nextSibling()
			return text.strip()

		year = int(element.attribute("year"))
		minutes = int(element.attribute("minutes"))
		ymd= element.attribute("acquired").split("-")
		if len(ymd) != 3:
			raise ValueError("invalid acquired date {0}".format(element.attribute("acquired")))
		acquired = QDate(int(ymd[0]), int(ymd[1]), int(ymd[2]))
		title = notes= None
		node = element.firstChild()
		while title is None or notes is None:
			if node.isNull():
				raise ValueError("missing title or notes")
			if node.toElement().tagName() == "title":
				title = getText(node)
			elif node.toElement().tagName() == "notes":
				notes = getText(node)
			node = node.nextSibling()
		if title is None:
			raise ValueError("missing title")
		print(title, year, minutes, acquired, notes)
		self.add(Movie(title, year, minutes, acquired, notes))



	@staticmethod
	def test(): 
		print("test")
		'''c = MovieContainer()
		c.load("save.mpb")
		ok, message = c.importDom("export.xml")
		print(message)
		
		ok, info = c.load("save.mqb")
		c.exportXml("export.xml")

		print(info)
		$for m in c:
			print(m.title)
		ok, info = c.save("save.mqb")
		print("Save" + info)

		year = 2017
		title = "an 52045 test elleo"
		movie = Movie(title, year)
		movie2 = Movie("the test one", 2018)
		container = MovieContainer()
		container.add(movie)
		container.add(movie2)
		print(container.key(title,year))
		print(container.key("the test one",2018))
		for k,m in container.movieDict.items():
			print("key:{0}, value:{1}".format(k,m.title))
		for m in container.movies:
			k = m[0]
			v = m[1]
			print("key:{0}, value:{1}".format(k,v.title)) 
		container.save("save.mqb")
		container.save("save.mpb")
		container.save("save.mqt")
		container.save("save.mpt") '''


if __name__ == "__main__":
	MovieContainer.test()
