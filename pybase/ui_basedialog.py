# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basedialog.ui'
#
# Created: Thu Feb 11 23:19:45 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BaseDialog(object):
    def setupUi(self, BaseDialog):
        BaseDialog.setObjectName(_fromUtf8("BaseDialog"))
        BaseDialog.resize(423, 98)
        self.verticalLayout = QtGui.QVBoxLayout(BaseDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frameBase = QtGui.QFrame(BaseDialog)
        self.frameBase.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameBase.setFrameShadow(QtGui.QFrame.Raised)
        self.frameBase.setObjectName(_fromUtf8("frameBase"))
        self.gridLayout = QtGui.QGridLayout(self.frameBase)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelText = QtGui.QLabel(self.frameBase)
        self.labelText.setObjectName(_fromUtf8("labelText"))
        self.gridLayout.addWidget(self.labelText, 0, 0, 1, 1)
        self.lineEditText = QtGui.QLineEdit(self.frameBase)
        self.lineEditText.setObjectName(_fromUtf8("lineEditText"))
        self.gridLayout.addWidget(self.lineEditText, 0, 1, 1, 1)
        self.labelBase64 = QtGui.QLabel(self.frameBase)
        self.labelBase64.setObjectName(_fromUtf8("labelBase64"))
        self.gridLayout.addWidget(self.labelBase64, 1, 0, 1, 1)
        self.lineEditBase64 = QtGui.QLineEdit(self.frameBase)
        self.lineEditBase64.setObjectName(_fromUtf8("lineEditBase64"))
        self.gridLayout.addWidget(self.lineEditBase64, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frameBase)

        self.retranslateUi(BaseDialog)
        QtCore.QMetaObject.connectSlotsByName(BaseDialog)

    def retranslateUi(self, BaseDialog):
        BaseDialog.setWindowTitle(_translate("BaseDialog", "Base64", None))
        self.labelText.setText(_translate("BaseDialog", "Text", None))
        self.labelBase64.setText(_translate("BaseDialog", "Base64", None))

