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

        self.previousstored1 = False
        self.previousstored2 = False

        self._table1 = numpy.zeros([self.SBconductor.maximum(), self.TWConductor.columnCount()])
        self._table2 = numpy.zeros([self.SBsubconductor.maximum(), self.TWSubconductor.columnCount()])

        self.TWConductor.cellChanged.connect(self.table1matrix)
        self.TWSubconductor.cellChanged.connect(self.table2matrix)

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
        self.changetablerow(1, 1) # Force table update
        pass

    def table1matrix(self):
        row = self.TWConductor.currentRow()
        col = self.TWConductor.currentColumn()
        value = self.TWConductor.item(row, col)
        if col >= 0 and row >= 0:
            try:
                value = value.text()
                if value != "":
                    value = float(value)
                else:
                    value = 0.
            except ValueError:
                # print("error: ", row, col, value)
                item = QtGui.QTableWidgetItem()
                item.setText("")
                self.TWConductor.setItem(row, col, item)
                return
            self._table1[row, col] = value
        return

    def table2matrix(self):
        row = self.TWSubconductor.currentRow()
        col = self.TWSubconductor.currentColumn()
        value = self.TWSubconductor.item(row, col)
        if col >= 0 and row >= 0:
            try:
                value = value.text()
                if value != "":
                    value = float(value)
                else:
                    value = 0.
            except ValueError:
                # print("error: ", row, col, value)
                item = QtGui.QTableWidgetItem()
                item.setText("")
                self.TWSubconductor.setItem(row, col, item)
                return
            self._table2[row, col] = value
        return

    def changetablerow(self, d1: int = 0, d2: int = 0):
        # TODO: Estimate the change and store values on reduction
        # TODO: add feature, on new line, copy coord of the after conductor
        if d1+d2 ==0:
            self.delta1 = self._row1 - self.SBconductor.value()
            self.delta2 = self._row2 - self.SBsubconductor.value()
        else:
            self.delta1, self.delta2 = d1, d2

        if self.delta1 != 0:
            # on change, update de value and the rows availables on the table
            self._row1 = self.SBconductor.value()
            self.TWConductor.setRowCount(self._row1)
            if self.delta1 > 0:
                # read matrix values and write on table
                for row in range(self._row1):
                    data = [0, 0]
                    for i, v in enumerate(self._table1[row, :]):
                        if v == 0.:
                            data[i] = ""
                        else:
                            data[i] = str(v)

                    item = QtGui.QTableWidgetItem()
                    item.setText(data[0])
                    self.TWConductor.setItem(row, 0, item)

                    item = QtGui.QTableWidgetItem()
                    item.setText(data[1])
                    self.TWConductor.setItem(row, 1, item)
        elif self._row2 != 0:
            self._row2 = self.SBsubconductor.value()
            self.TWSubconductor.setRowCount(self._row2)
            if self.delta2 > 0:
                # read matrix values and write on table
                for row in range(self._row2):
                    data = [0, 0]
                    for i, v in enumerate(self._table2[row, :]):
                        if v == 0.:
                            data[i] = ""
                        else:
                            data[i] = str(v)

                    item = QtGui.QTableWidgetItem()
                    item.setText(data[0])
                    self.TWSubconductor.setItem(row, 0, item)

                    item = QtGui.QTableWidgetItem()
                    item.setText(data[1])
                    self.TWSubconductor.setItem(row, 1, item)
        else:
            pass

    def cleardata1(self):
        self._table1[:] = 0
        return
    def cleardata2(self):
        self._table2[:] = 0
        return



if __name__ == "__main__":
    app = QApplication([])
form = ExampleApp()
form.show()
app.exec_()
