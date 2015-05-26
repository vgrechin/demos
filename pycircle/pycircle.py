#! /usr/bin/python

import sys
from PyQt4 import QtGui, QtCore
from maindialog import *
from controller import *

def main():

    app = QtGui.QApplication(sys.argv)
    view = MainDialog()

    doc = Controller(view)

    view.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
