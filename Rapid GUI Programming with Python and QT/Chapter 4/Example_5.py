from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TaxRate(QObject):
    rateChanged = pyqtSignal(float)

    def __init__(self):
        super(TaxRate, self).__init__()
        self.__rate = 17.5


    def rate(self):
        return self.__rate


    def setRate(self, rate):
        if rate != self.__rate:
            self.__rate = rate
            #self.emit(SIGNAL("rateChanged"), self.__rate)
            self.rateChanged.emit(self.__rate)

    

def funChanged(value):
    print "TaxRate changed to %.2f%%" % value


if __name__ == "__main__":
    vat = TaxRate()
    #vat.connect(vat, SIGNAL("rateChanged"), rateChanged)
    vat.rateChanged.connect(funChanged)
    vat.setRate(17.5)    # No change will occur (new rate is the same)
    vat.setRate(8.5)     # A change will occur (new rate is different)    