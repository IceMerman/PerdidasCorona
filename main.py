#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication

import convertedUI


class ExampleApp(QtGui.QMainWindow, convertedUI.Ui_Form):
    # Attribs

    # Constructor
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        
        #self.btnSolve.released.connect(self.calcule)
        #self.cbTestData.released.connect(self.toggleEnable)
        return

    def keyPressEvent(self, event):
        # Override this method to detect the keyDown
        if event.key() == QtCore.Qt.Key_Return:
            self.calcule()
        event.accept()

    def toggleEnable(self):
        return True

    def calcule(self):
        return True


if __name__ == "__main__":
    app = QApplication([])
form = ExampleApp()
form.show()
app.exec_()
