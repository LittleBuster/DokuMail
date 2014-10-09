# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taskWnd.ui'
#
# Created: Fri Oct 10 02:30:32 2014
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

class Ui_TaskWnd(object):
    def setupUi(self, TaskWnd):
        TaskWnd.setObjectName(_fromUtf8("TaskWnd"))
        TaskWnd.resize(719, 451)
        TaskWnd.setMinimumSize(QtCore.QSize(719, 451))
        TaskWnd.setMaximumSize(QtCore.QSize(719, 451))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/filenew_8842.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TaskWnd.setWindowIcon(icon)
        self.label = QtGui.QLabel(TaskWnd)
        self.label.setGeometry(QtCore.QRect(-210, -120, 941, 671))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/fon.jpg")))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(TaskWnd)
        self.label_2.setGeometry(QtCore.QRect(290, 150, 121, 121))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/filenew_8842.ico")))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(TaskWnd)
        self.label_3.setGeometry(QtCore.QRect(250, 0, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pbClose = QtGui.QPushButton(TaskWnd)
        self.pbClose.setGeometry(QtCore.QRect(160, 400, 141, 41))
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
        self.teMsg = QtGui.QTextEdit(TaskWnd)
        self.teMsg.setGeometry(QtCore.QRect(20, 50, 681, 341))
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
        self.teMsg.setObjectName(_fromUtf8("teMsg"))
        self.pbSendTask = QtGui.QPushButton(TaskWnd)
        self.pbSendTask.setGeometry(QtCore.QRect(310, 400, 241, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbSendTask.setFont(font)
        self.pbSendTask.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("images/cloud.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbSendTask.setIcon(icon2)
        self.pbSendTask.setIconSize(QtCore.QSize(24, 24))
        self.pbSendTask.setObjectName(_fromUtf8("pbSendTask"))

        self.retranslateUi(TaskWnd)
        QtCore.QMetaObject.connectSlotsByName(TaskWnd)

    def retranslateUi(self, TaskWnd):
        TaskWnd.setWindowTitle(_translate("TaskWnd", "Новая заявка", None))
        self.label_3.setText(_translate("TaskWnd", "<html><head/><body><p><span style=\" color:#00ffd5;\">Новая заявка</span></p></body></html>", None))
        self.pbClose.setText(_translate("TaskWnd", "Закрыть", None))
        self.teMsg.setHtml(_translate("TaskWnd", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:22pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Опишите проблему...</p></body></html>", None))
        self.pbSendTask.setText(_translate("TaskWnd", "Отправить заявку", None))

