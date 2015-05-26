from PyQt4 import QtCore
from common import *
from maindialog import *
from circlescene import *

class Controller(QtCore.QObject):
    def __init__(self, view):
        super(Controller, self).__init__()
        self.view = view
        self.view.setScene(scene = CircleScene(self.view))
        self.view.signal.calculated.connect(self.calculate)

    def calculate(self, radius):
        self.view.update(
              Common.circumference(radius)
            , Common.circle_area(radius))
