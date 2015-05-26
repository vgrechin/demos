#! /usr/bin/python

import sys
from PyQt4 import QtGui, QtCore
from circlescene import *
from ui_maindialog import *

class MainDialog(QtGui.QDialog):

    class Signal(QtCore.QObject):
        calculated = QtCore.pyqtSignal('qreal', name = "calculated")

    def __init__(self):
        super(MainDialog, self).__init__()
        self.ui = Ui_MainDialog()
        self.ui.setupUi(self)
        self.signal = MainDialog.Signal()

        self.ui.pbutCalculate.pressed.connect(self.calculate)
        self.ui.pbutReset.pressed.connect(self.reset)

    def setScene(self, scene):
        self.ui.gviewCircle.setScene(scene)

    def calculate(self):
        radius = self.ui.dsboxRadius.value()
        diameter = self.ui.dsboxDiameter.value()
        if radius and diameter:
            messageBox = QtGui.QMessageBox(QtGui.QMessageBox.Warning
                , "Ambiguous dimension"
                , "You must enter either the radius or the diameter, not both")
            messageBox.exec_()
        elif diameter:
            self.signal.calculated.emit(diameter / 2)
        else:
            self.signal.calculated.emit(radius)

    def reset(self):
        self.ui.dsboxRadius.setValue(0)
        self.ui.dsboxDiameter.setValue(0)
        self.ui.dsboxCircuit.setValue(0)
        self.ui.dsboxArea.setValue(0)

    def update(self, circuit, area):
        self.ui.dsboxCircuit.setValue(circuit)
        self.ui.dsboxArea.setValue(area)
