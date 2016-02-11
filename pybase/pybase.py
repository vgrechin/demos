#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from basedialog import *
from basecontroller import *

def main():
    app = QtGui.QApplication(sys.argv)
    view = BaseDialog()
    doc = BaseController(view)

    view.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
