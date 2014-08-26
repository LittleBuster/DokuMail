# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'watchWnd.ui'
#
# Created: Wed Aug 27 00:46:40 2014
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

class Ui_WatchWindow(object):
    def setupUi(self, WatchWindow):
        WatchWindow.setObjectName(_fromUtf8("WatchWindow"))
        WatchWindow.resize(653, 253)
        self.tw1 = QtGui.QTableWidget(WatchWindow)
        self.tw1.setGeometry(QtCore.QRect(10, 10, 631, 231))
        self.tw1.setStyleSheet(_fromUtf8(""))
        self.tw1.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tw1.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tw1.setRowCount(0)
        self.tw1.setColumnCount(5)
        self.tw1.setObjectName(_fromUtf8("tw1"))
        self.tw1.horizontalHeader().setCascadingSectionResizes(True)
        self.tw1.horizontalHeader().setDefaultSectionSize(300)
        self.tw1.horizontalHeader().setHighlightSections(True)
        self.tw1.horizontalHeader().setStretchLastSection(True)
        self.tw1.verticalHeader().setVisible(False)
        self.tw1.verticalHeader().setCascadingSectionResizes(True)
        self.tw1.verticalHeader().setStretchLastSection(False)

        self.retranslateUi(WatchWindow)
        QtCore.QMetaObject.connectSlotsByName(WatchWindow)

    def retranslateUi(self, WatchWindow):
        WatchWindow.setWindowTitle(_translate("WatchWindow", "Form", None))

