# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msgWnd.ui'
#
# Created: Thu Aug  7 19:20:07 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MsgWnd(object):
    def setupUi(self, MsgWnd):
        MsgWnd.setObjectName("MsgWnd")
        MsgWnd.resize(719, 451)
        MsgWnd.setMinimumSize(QtCore.QSize(719, 451))
        MsgWnd.setMaximumSize(QtCore.QSize(719, 451))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/convert.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MsgWnd.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(MsgWnd)
        self.label.setGeometry(QtCore.QRect(-210, -120, 941, 671))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/fon.jpg"))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MsgWnd)
        self.label_2.setGeometry(QtCore.QRect(170, -4, 71, 48))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/conv.ico"))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MsgWnd)
        self.label_3.setGeometry(QtCore.QRect(240, 5, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.pbClose = QtWidgets.QPushButton(MsgWnd)
        self.pbClose.setGeometry(QtCore.QRect(230, 400, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbClose.setFont(font)
        self.pbClose.setStyleSheet("QPushButton {\n"
"    background-color:qlineargradient(spread:reflect, x1:0.515, y1:1, x2:0.528, y2:0, stop:0 rgba(0, 143, 250, 255), stop:0.655502 rgba(0, 29, 203, 255), stop:1 rgba(190, 255, 255, 255));\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 7px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:qlineargradient(spread:reflect, x1:0.515, y1:1, x2:0.528, y2:0, stop:0 rgba(0, 143, 250, 255), stop:0.655502 rgba(82, 100, 203, 255), stop:1 rgba(190, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:qlineargradient(spread:reflect, x1:0.515, y1:1, x2:0.528, y2:0, stop:0 rgba(0, 143, 250, 255), stop:0.596154 rgba(85, 250, 255, 255), stop:1 rgba(190, 255, 255, 255));\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbClose.setIcon(icon1)
        self.pbClose.setIconSize(QtCore.QSize(24, 24))
        self.pbClose.setObjectName("pbClose")
        self.lbFile = QtWidgets.QLabel(MsgWnd)
        self.lbFile.setGeometry(QtCore.QRect(20, 50, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbFile.setFont(font)
        self.lbFile.setObjectName("lbFile")
        self.teMsg = QtWidgets.QTextEdit(MsgWnd)
        self.teMsg.setGeometry(QtCore.QRect(20, 100, 681, 291))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.teMsg.setFont(font)
        self.teMsg.setStyleSheet("QWidget {\n"
"    background-color: rgba(23, 115, 255, 137);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}")
        self.teMsg.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.teMsg.setObjectName("teMsg")
        self.lbFile_2 = QtWidgets.QLabel(MsgWnd)
        self.lbFile_2.setGeometry(QtCore.QRect(490, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbFile_2.setFont(font)
        self.lbFile_2.setObjectName("lbFile_2")
        self.lbFrom = QtWidgets.QLabel(MsgWnd)
        self.lbFrom.setGeometry(QtCore.QRect(140, 50, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbFrom.setFont(font)
        self.lbFrom.setObjectName("lbFrom")
        self.lbTime = QtWidgets.QLabel(MsgWnd)
        self.lbTime.setGeometry(QtCore.QRect(590, 50, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbTime.setFont(font)
        self.lbTime.setObjectName("lbTime")

        self.retranslateUi(MsgWnd)
        QtCore.QMetaObject.connectSlotsByName(MsgWnd)

    def retranslateUi(self, MsgWnd):
        _translate = QtCore.QCoreApplication.translate
        MsgWnd.setWindowTitle(_translate("MsgWnd", "Сообщение"))
        self.label_3.setText(_translate("MsgWnd", "<html><head/><body><p><span style=\" color:#00ffd5;\">Новое сообщение</span></p></body></html>"))
        self.pbClose.setText(_translate("MsgWnd", "Закрыть сообщение"))
        self.lbFile.setText(_translate("MsgWnd", "<html><head/><body><p><span style=\" color:#00dbff;\">От кого:</span></p></body></html>"))
        self.lbFile_2.setText(_translate("MsgWnd", "<html><head/><body><p><span style=\" color:#00dbff;\">Время:</span></p></body></html>"))
        self.lbFrom.setText(_translate("MsgWnd", "<html><head/><body><p><span style=\" color:#ffffff;\">От кого:</span></p></body></html>"))
        self.lbTime.setText(_translate("MsgWnd", "<html><head/><body><p><span style=\" color:#ffffff;\">22:23:23</span></p></body></html>"))

