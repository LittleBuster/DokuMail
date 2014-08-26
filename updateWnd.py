# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateWnd.ui'
#
# Created: Wed Aug 20 13:20:49 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UpdateWnd(object):
    def setupUi(self, UpdateWnd):
        UpdateWnd.setObjectName("UpdateWnd")
        UpdateWnd.resize(719, 319)
        UpdateWnd.setMinimumSize(QtCore.QSize(719, 319))
        UpdateWnd.setMaximumSize(QtCore.QSize(719, 451))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/downloads.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UpdateWnd.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(UpdateWnd)
        self.label.setGeometry(QtCore.QRect(-280, -270, 1101, 801))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/fon.jpg"))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(UpdateWnd)
        self.label_3.setGeometry(QtCore.QRect(110, 5, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.lbFile = QtWidgets.QLabel(UpdateWnd)
        self.lbFile.setGeometry(QtCore.QRect(0, 250, 711, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lbFile.setFont(font)
        self.lbFile.setAlignment(QtCore.Qt.AlignCenter)
        self.lbFile.setObjectName("lbFile")
        self.label_4 = QtWidgets.QLabel(UpdateWnd)
        self.label_4.setGeometry(QtCore.QRect(250, 50, 231, 231))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/database-icon-219.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(UpdateWnd)
        QtCore.QMetaObject.connectSlotsByName(UpdateWnd)

    def retranslateUi(self, UpdateWnd):
        _translate = QtCore.QCoreApplication.translate
        UpdateWnd.setWindowTitle(_translate("UpdateWnd", "Загрузка"))
        self.label_3.setText(_translate("UpdateWnd", "<html><head/><body><p><span style=\" color:#00ffd5;\">Обновление файлов DokuMail</span></p></body></html>"))
        self.lbFile.setText(_translate("UpdateWnd", "<html><head/><body><p><span style=\" color:#00d2ff;\">Обновление файлов</span></p></body></html>"))

