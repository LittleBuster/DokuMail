# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uploadWnd.ui'
#
# Created: Wed Oct  1 13:10:51 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(747, 225)
        Form.setMinimumSize(QtCore.QSize(747, 225))
        Form.setMaximumSize(QtCore.QSize(747, 225))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/cloud.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 747, 225))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/isend.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.pB = QtGui.QProgressBar(Form)
        self.pB.setGeometry(QtCore.QRect(10, 198, 726, 19))
        self.pB.setProperty("value", 24)
        self.pB.setTextVisible(False)
        self.pB.setOrientation(QtCore.Qt.Horizontal)
        self.pB.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.pB.setObjectName(_fromUtf8("pB"))
        self.lbAct = QtGui.QLabel(Form)
        self.lbAct.setGeometry(QtCore.QRect(10, 50, 321, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbAct.setFont(font)
        self.lbAct.setObjectName(_fromUtf8("lbAct"))
        self.lbFile = QtGui.QLabel(Form)
        self.lbFile.setGeometry(QtCore.QRect(10, 90, 461, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbFile.setFont(font)
        self.lbFile.setObjectName(_fromUtf8("lbFile"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Отправка", None))
        self.lbAct.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#00d4ff;\">sfdfsdf</span></p></body></html>", None))
        self.lbFile.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">sfdfsdf</span></p></body></html>", None))

