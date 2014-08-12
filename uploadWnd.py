# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uploadWnd.ui'
#
# Created: Tue Aug 12 16:58:50 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(747, 225)
        Form.setMinimumSize(QtCore.QSize(747, 225))
        Form.setMaximumSize(QtCore.QSize(747, 225))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/cloud.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 747, 225))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/isend.png"))
        self.label.setObjectName("label")
        self.pB = QtWidgets.QProgressBar(Form)
        self.pB.setGeometry(QtCore.QRect(10, 198, 726, 19))
        self.pB.setProperty("value", 24)
        self.pB.setTextVisible(False)
        self.pB.setOrientation(QtCore.Qt.Horizontal)
        self.pB.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.pB.setObjectName("pB")
        self.lbAct = QtWidgets.QLabel(Form)
        self.lbAct.setGeometry(QtCore.QRect(10, 50, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbAct.setFont(font)
        self.lbAct.setObjectName("lbAct")
        self.lbFile = QtWidgets.QLabel(Form)
        self.lbFile.setGeometry(QtCore.QRect(10, 90, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbFile.setFont(font)
        self.lbFile.setObjectName("lbFile")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Отправка"))
        self.lbAct.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#00d4ff;\">sfdfsdf</span></p></body></html>"))
        self.lbFile.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">sfdfsdf</span></p></body></html>"))

