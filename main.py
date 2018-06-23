#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import utils as ut

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication

import convertedUI, numpy


class ExampleApp(QtGui.QMainWindow, convertedUI.Ui_Form):
    # Constructor
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

        self._row1 = self.SBconductor.value()
        self._row2 = self.SBsubconductor.value()
        self.delta1 = 0
        self.delta2 = 0

        self.previousstored1=False
        self.previousstored2 = False

        self._table1 = numpy.zeros([self.SBconductor.maximum(), self.TWConductor.columnCount()])
        self._table2 = numpy.zeros([self.SBsubconductor.maximum(), self.TWSubconductor.columnCount()])

        self.SBconductor.valueChanged.connect(self.changetablerow)
        self.SBsubconductor.valueChanged.connect(self.changetablerow)

        self.PBShowCond.released.connect(self.showCondcuctors)
        self.clcTW1.released.connect(self.cleardata1)
        self.clcTW2.released.connect(self.cleardata2)

        return

    def keyPressEvent(self, event):
        # Override this method to detect the keyDown
        if event.key() == QtCore.Qt.Key_Return:
            self.calcule()
        event.accept()

    def toggleEnable(self):
        return
        return True

    def calcule(self):
        return True

    def showCondcuctors(self):
        pass

    def changetablerow(self):
        # TODO: Estimate the change and store values on reduction
        # TODO: add feature, on new line, copy coord of the after conductor
        self.delta1 = self._row1 - self.SBconductor.value()
        self.delta2 = self._row2 - self.SBsubconductor.value()
        if self.delta1 != 0:
            # on change, update de value and the rows availables on the table
            self._row1 = self.SBconductor.value()
            self.TWConductor.setRowCount(self._row1)
        elif self._row2 != 0:
            self._row2 = self.SBsubconductor.value()
            self.TWSubconductor.setRowCount(self._row2)
        else:
            pass

    def cleardata1(self):
        pass
    def cleardata2(self):
        pass



if __name__ == "__main__":
    app = QApplication([])
form = ExampleApp()
form.show()
app.exec_()
