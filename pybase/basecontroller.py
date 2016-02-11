# -*- coding: utf-8 -*-

import base64
from PyQt4 import QtCore
from basedialog import *

class BaseController(QtCore.QObject):
    def __init__(self, view):
        super(BaseController, self).__init__()
        self.view = view
        self.view.setWindowTitle("Base64 converter")

        self.view.signal.textEdited.connect(self.encode)
        self.view.signal.baseEdited.connect(self.decode)

    def encode(self, text):
        self.view.updateBase(str(text).encode('base64'))

    def decode(self, base64):
        self.view.updateText(str(base64).decode('base64'))
