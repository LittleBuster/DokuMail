# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msgWnd.ui'
#
# Created: Wed Aug 27 13:33:29 2014
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

class Ui_MsgWnd(object):
    def setupUi(self, MsgWnd):
        MsgWnd.setObjectName(_fromUtf8("MsgWnd"))
        MsgWnd.resize(719, 451)
        MsgWnd.setMinimumSize(QtCore.QSize(719, 451))
        MsgWnd.setMaximumSize(QtCore.QSize(719, 451))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/convert.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MsgWnd.setWindowIcon(icon)
        self.label = QtGui.QLabel(MsgWnd)
        self.label.setGeometry(QtCore.QRect(-210, -120, 941, 671))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/fon.jpg")))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(MsgWnd)
        self.label_2.setGeometry(QtCore.QRect(170, -4, 71, 48))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/conv.ico")))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(MsgWnd)
        self.label_3.setGeometry(QtCore.QRect(240, 5, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pbClose = QtGui.QPushButton(MsgWnd)
        self.pbClose.setGeometry(QtCore.QRect(230, 400, 251, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbClose.setFont(font)
        self.pbClose.setStyleSheet(_fromUtf8("QPushButton {\n"
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
"}"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbClose.setIcon(icon1)
        self.pbClose.setIconSize(QtCore.QSize(24, 24))
        self.pbClose.setObjectName(_fromUtf8("pbClose"))
        self.lbFile = QtGui.QLabel(MsgWnd)
        self.lbFile.setGeometry(QtCore.QRect(20, 50, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbFile.setFont(font)
        self.lbFile.setObjectName(_fromUtf8("lbFile"))
        self.teMsg = QtGui.QTextEdit(MsgWnd)
        self.teMsg.setGeometry(QtCore.QRect(20, 100, 681, 291))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.teMsg.setFont(font)
        self.teMsg.setStyleSheet(_fromUtf8("QWidget {\n"
"    background-color: rgba(23, 115, 255, 137);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.teMsg.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.teMsg.setObjectName(_fromUtf8("teMsg"))
        self.lbFile_2 = QtGui.QLabel(MsgWnd)
        self.lbFile_2.setGeometry(QtCore.QRect(490, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbFile_2.setFont(font)
        self.lbFile_2.setObjectName(_fromUtf8("lbFile_2"))
        self.lbFrom = QtGui.QLabel(MsgWnd)
        self.lbFrom.setGeometry(QtCore.QRect(140, 50, 241, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbFrom.setFont(font)
        self.lbFrom.setObjectName(_fromUtf8("lbFrom"))
        self.lbTime = QtGui.QLabel(MsgWnd)
        self.lbTime.setGeometry(QtCore.QRect(590, 50, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbTime.setFont(font)
        self.lbTime.setObjectName(_fromUtf8("lbTime"))

        self.retranslateUi(MsgWnd)
        QtCore.QMetaObject.connectSlotsByName(MsgWnd)

    def retranslateUi(self, MsgWnd):
        MsgWnd.setWindowTitle(_translate("MsgWnd", "Сообщение", None))
        self.label_3.setText(_translate("MsgWnd", "<html><head/><body><p><span style=\" color:#00ffd5;\">Новое сообщение</span></p></body></html>", None))
        self.pbClose.setText(_translate("MsgWnd", "Закрыть сообщение", None))
        self.lbFile.setText(_translate("MsgWnd", "<html><head/><body><p><span style=\" color:#00dbff;\">От кого:</span></p></body></html>", None))
        self.lbFile_2.setText(_translate("MsgWnd", "<html><head/><body><p><span style=\" color:#00dbff;\">Время:</span></p></body></html>", None))
        self.lbFrom.setText(_translate("MsgWnd", "<html><head/><body><p><span style=\" color:#ffffff;\">От кого:</span></p></body></html>", None))
        self.lbTime.setText(_translate("MsgWnd", "<html><head/><body><p><span style=\" color:#ffffff;\">22:23:23</span></p></body></html>", None))

