from PyQt5.QtCore import QFile, QFileInfo, QIODevice,QTextStream
from PyQt5.QtXml import (QDomDocument, QDomNode, QXmlDefaultHandler,
                         QXmlInputSource, QXmlSimpleReader)


import datetime
CODEC = "UTF-8"

NEWPARA = chr(0x2029)
NEWLINE = chr(0x2028)
def encodedNewlines(text):
    return text.replace("\n\n", NEWPARA).replace("\n", NEWLINE)

def decodedNewlines(text):
    return text.replace(NEWPARA, "\n\n").replace(NEWLINE, "\n")

class Movie(object):
    UNKNOWNYEAR = 1890
    UNKNOWNMINUTES = 0
    def __init__(self, title=None, year=UNKNOWNYEAR,
                 minutes=UNKNOWNMINUTES, acquired=None, notes=None):
        self.title = title
        self.year = year
        self.minutes = minutes
        self.acquired = (acquired if acquired is not None
                                  else datetime.date.today())
        self.notes = notes
class MovieContainer(object):

    def __init__(self,fname,movies):
        self.__fname = fname
        self.__movies = movies        

    def exportXml(self, fname):
        error = None
        fh = None
        try:
            fh = QFile(fname)
            if not fh.open(QIODevice.WriteOnly):
                raise IOError(str(fh.errorString()))
            stream = QTextStream(fh)
            stream.setCodec(CODEC)
            stream << ("<?xml version='1.0' encoding='{0}'?>\n"
                       "<!DOCTYPE MOVIES>\n"
                       "<MOVIES VERSION='1.0'>\n".format(CODEC))
            stream << ("<MOVIE YEAR='{0}' MINUTES='{1}' "
                       "ACQUIRED='{2}'>\n".format(movie.year,
                       movie.minutes,
                       movie.acquired)) \
                   << "<TITLE>" << movie.title \
                   << "</TITLE>\n<NOTES>"
            if movie.notes:
                stream << "\n" << encodedNewlines(movie.notes)
            stream << "\n</NOTES>\n</MOVIE>\n"
            stream << "</MOVIES>\n"
        except EnvironmentError as e:
            error = "Failed to export: {0}".format(e)
        finally:
            if fh is not None:
                fh.close()
            if error is not None:
                print(error)
            print("Exported 1 movie records to {0}".format(
                    QFileInfo(fname).fileName()))


    def importDOM(self, fname):
        dom = QDomDocument()
        error = None
        fh = None
        try:
            fh = QFile(fname)
            if not fh.open(QIODevice.ReadOnly):
                raise IOError(str(fh.errorString()))
            if not dom.setContent(fh):
                raise ValueError("could not parse XML")
        except (IOError, OSError, ValueError) as e:
            error = "Failed to import: {0}".format(e)
        finally:
            if fh is not None:
                fh.close()
            if error is not None:
                print(error)
        try:
            self.populateFromDOM(dom)
        except ValueError as e:
            print("Failed to import: {0}".format(e))
        self.__fname = ""
        print("Imported  movie records from {0}".format(
                    QFileInfo(fname).fileName()))


    def populateFromDOM(self, dom):
        root = dom.documentElement()
        if root.tagName().lower() != "MOVIES".lower():
            raise ValueError("not a Movies XML file")
        node = root.firstChild()
        while not node.isNull():
            if node.toElement().tagName().lower() == "MOVIE".lower():
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
        year = int(element.attribute("YEAR".lower()))
        #print("test")
        minutes = int(element.attribute("MINUTES".lower()))
        ymd = element.attribute("ACQUIRED".lower()).split("-")

        if len(ymd) != 3:
            raise ValueError("invalid acquired date {0}".format(
                    str(element.attribute("ACQUIRED".lower()))))
        acquired = datetime.date(int(ymd[0]), int(ymd[1]),
                                int(ymd[2]))
        title = notes = None
        node = element.firstChild()
        while title is None or notes is None:
            if node.isNull():
                raise ValueError("missing title or notes")
            if node.toElement().tagName().lower() == "TITLE".lower():
                title = getText(node)
            elif node.toElement().tagName().lower() == "NOTES".lower():
                notes = getText(node)
            node = node.nextSibling()
        if not title:
            raise ValueError("missing title")
        #self.add(Movie(title,year, minutes, acquired,notes))
        print(title, year, minutes, acquired,decodedNewlines(notes))


    def importSAX(self, fname):

        error = None
        fh = None
        try:
            handler = SaxMovieHandler(self)
            parser = QXmlSimpleReader()
            parser.setContentHandler(handler)
            parser.setErrorHandler(handler)
            fh = QFile(fname)
            input = QXmlInputSource(fh)
            if not parser.parse(input):
                raise ValueError(handler.error)
        except (IOError, OSError, ValueError) as e:
            error = "Failed to import: {0}".format(e)
        finally:
            if fh is not None:
                fh.close()
            if error is not None:
                print(error)
            self.__fname = ""
            print("Imported 1 movie records from {0}".format(
                    QFileInfo(fname).fileName()))



class SaxMovieHandler(QXmlDefaultHandler):

    def __init__(self, movies):
        super(SaxMovieHandler, self).__init__()
        self.movies = movies
        self.text = ""
        self.error = None


    def clear(self):
        self.year = None
        self.minutes = None
        self.acquired = None
        self.title = None
        self.notes = None


    def startElement(self, namespaceURI, localName, qName, attributes):
        if qName == "MOVIE":
            self.clear()
            self.year = int(attributes.value("YEAR"))
            self.minutes = int(attributes.value("MINUTES"))
            ymd = attributes.value("ACQUIRED").split("-")
            if len(ymd) != 3:
                raise ValueError("invalid acquired date {0}".format(
                        str(attributes.value("ACQUIRED"))))
            self.acquired = datetime.date(int(ymd[0]),
                    int(ymd[1]), int(ymd[2]))
        elif qName in ("TITLE", "NOTES"):
            self.text = ""
        return True


    def characters(self, text):
        self.text += text
        return True


    def endElement(self, namespaceURI, localName, qName):
        if qName == "MOVIE":
            if (self.year is None or self.minutes is None or
                self.acquired is None or self.title is None or
                self.notes is None or not self.title):
                raise ValueError("incomplete movie record")
            print(self.title, self.year,
                    self.minutes, self.acquired,
                    decodedNewlines(self.notes))

        elif qName == "TITLE":
            self.title = self.text.strip()
        elif qName == "NOTES":
            self.notes = self.text.strip()
        return True


    def fatalError(self, exception):
        self.error = "parse error at line {0} column {1}: {2}".format(
                exception.lineNumber(), exception.columnNumber(),
                exception.message())
        return False


if __name__ == "__main__":

    textdata=[["God save world",1989,45,None,"HELLO WORLD"]]
    fname="export.1.xml"
    for data in textdata:
        movie=Movie(data[0],data[1],data[2],data[3],data[4])
        moviecontainer=MovieContainer(fname, movie)
        #moviecontainer.exportXml(fname)
        moviecontainer.importDOM(fname)
        #moviecontainer.importSAX(fname)