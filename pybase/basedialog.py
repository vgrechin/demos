# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from ui_basedialog import *

class BaseDialog(QtGui.QDialog):
    class Signal(QtCore.QObject):
        textEdited = QtCore.pyqtSignal('QString', name = 'textEdited')
        baseEdited = QtCore.pyqtSignal('QString', name = 'baseEdited')

    def __init__(self):
        super(BaseDialog, self).__init__()
        self.ui = Ui_BaseDialog()
        self.ui.setupUi(self)
        self.signal = BaseDialog.Signal()

        self.ui.lineEditText.textEdited.connect(self.signal.textEdited)
        self.ui.lineEditBase64.textEdited.connect(self.signal.baseEdited)

    def updateText(self, text):
        self.ui.lineEditText.setText(text)

    def updateBase(self, base64):
        self.ui.lineEditBase64.setText(base64)
