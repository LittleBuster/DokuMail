# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newsBaloon.ui'
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

class Ui_NewsBaloon(object):
    def setupUi(self, NewsBaloon):
        NewsBaloon.setObjectName(_fromUtf8("NewsBaloon"))
        NewsBaloon.resize(560, 141)
        NewsBaloon.setMinimumSize(QtCore.QSize(560, 141))
        NewsBaloon.setMaximumSize(QtCore.QSize(560, 141))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/news.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NewsBaloon.setWindowIcon(icon)
        self.label = QtGui.QLabel(NewsBaloon)
        self.label.setGeometry(QtCore.QRect(-80, -80, 751, 261))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/baloon.png")))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(NewsBaloon)
        self.label_3.setGeometry(QtCore.QRect(220, 0, 151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.leTitle = QtGui.QLineEdit(NewsBaloon)
        self.leTitle.setGeometry(QtCore.QRect(20, 60, 531, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.leTitle.setFont(font)
        self.leTitle.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    background-color: rgba(23, 115, 255, 137);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.leTitle.setText(_fromUtf8(""))
        self.leTitle.setReadOnly(True)
        self.leTitle.setObjectName(_fromUtf8("leTitle"))
        self.label_21 = QtGui.QLabel(NewsBaloon)
        self.label_21.setGeometry(QtCore.QRect(20, 37, 111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.pbRead = QtGui.QPushButton(NewsBaloon)
        self.pbRead.setGeometry(QtCore.QRect(170, 100, 381, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbRead.setFont(font)
        self.pbRead.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color:qlineargradient(spread:reflect, x1:0.515, y1:1, x2:0.528, y2:0, stop:0 rgba(0, 143, 250, 255), stop:0.655502 rgba(0, 29, 203, 255), stop:1 rgba(190, 255, 255, 255));\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 10px;\n"
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
        self.pbRead.setIcon(icon)
        self.pbRead.setIconSize(QtCore.QSize(20, 20))
        self.pbRead.setObjectName(_fromUtf8("pbRead"))
        self.pbClose = QtGui.QPushButton(NewsBaloon)
        self.pbClose.setGeometry(QtCore.QRect(20, 100, 141, 31))
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
"     border-radius: 10px;\n"
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
        self.pbClose.setIconSize(QtCore.QSize(20, 20))
        self.pbClose.setObjectName(_fromUtf8("pbClose"))

        self.retranslateUi(NewsBaloon)
        QtCore.QMetaObject.connectSlotsByName(NewsBaloon)

    def retranslateUi(self, NewsBaloon):
        NewsBaloon.setWindowTitle(_translate("NewsBaloon", "Новость", None))
        self.label_3.setText(_translate("NewsBaloon", "<html><head/><body><p><span style=\" color:#00ff5f;\">Новость</span></p></body></html>", None))
        self.label_21.setText(_translate("NewsBaloon", "<html><head/><body><p><span style=\" color:#00fffa;\">Заголовок:</span></p></body></html>", None))
        self.pbRead.setText(_translate("NewsBaloon", "Читать новость", None))
        self.pbClose.setText(_translate("NewsBaloon", "Закрыть", None))

