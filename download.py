# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloadWnd.ui'
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

class Ui_DownloadWnd(object):
    def setupUi(self, DownloadWnd):
        DownloadWnd.setObjectName(_fromUtf8("DownloadWnd"))
        DownloadWnd.resize(719, 426)
        DownloadWnd.setMinimumSize(QtCore.QSize(719, 426))
        DownloadWnd.setMaximumSize(QtCore.QSize(719, 426))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/downloads.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DownloadWnd.setWindowIcon(icon)
        self.label = QtGui.QLabel(DownloadWnd)
        self.label.setGeometry(QtCore.QRect(-210, -120, 941, 551))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/fon.jpg")))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(DownloadWnd)
        self.label_2.setGeometry(QtCore.QRect(186, 5, 48, 48))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/network_9488.png")))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(DownloadWnd)
        self.label_3.setGeometry(QtCore.QRect(240, 5, 281, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pbOpen = QtGui.QPushButton(DownloadWnd)
        self.pbOpen.setGeometry(QtCore.QRect(320, 372, 251, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbOpen.setFont(font)
        self.pbOpen.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.pbOpen.setIcon(icon)
        self.pbOpen.setIconSize(QtCore.QSize(24, 24))
        self.pbOpen.setObjectName(_fromUtf8("pbOpen"))
        self.pbClose = QtGui.QPushButton(DownloadWnd)
        self.pbClose.setGeometry(QtCore.QRect(160, 372, 151, 41))
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
        self.pb1 = QtGui.QProgressBar(DownloadWnd)
        self.pb1.setGeometry(QtCore.QRect(20, 310, 681, 23))
        self.pb1.setProperty("value", 24)
        self.pb1.setTextVisible(False)
        self.pb1.setObjectName(_fromUtf8("pb1"))
        self.pb2 = QtGui.QProgressBar(DownloadWnd)
        self.pb2.setGeometry(QtCore.QRect(20, 340, 681, 23))
        self.pb2.setStyleSheet(_fromUtf8(""))
        self.pb2.setProperty("value", 24)
        self.pb2.setTextVisible(False)
        self.pb2.setObjectName(_fromUtf8("pb2"))
        self.lbFile = QtGui.QLabel(DownloadWnd)
        self.lbFile.setGeometry(QtCore.QRect(20, 280, 681, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbFile.setFont(font)
        self.lbFile.setObjectName(_fromUtf8("lbFile"))
        self.label_4 = QtGui.QLabel(DownloadWnd)
        self.label_4.setGeometry(QtCore.QRect(240, 40, 261, 251))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("images/Downloads_Folder.png")))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lwFiles = QtGui.QListWidget(DownloadWnd)
        self.lwFiles.setGeometry(QtCore.QRect(20, 60, 681, 221))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lwFiles.setFont(font)
        self.lwFiles.setStyleSheet(_fromUtf8("QWidget {\n"
"    background-color: rgba(23, 115, 255, 137);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.lwFiles.setIconSize(QtCore.QSize(30, 30))
        self.lwFiles.setObjectName(_fromUtf8("lwFiles"))

        self.retranslateUi(DownloadWnd)
        QtCore.QMetaObject.connectSlotsByName(DownloadWnd)

    def retranslateUi(self, DownloadWnd):
        DownloadWnd.setWindowTitle(_translate("DownloadWnd", "Загрузка", None))
        self.label_3.setText(_translate("DownloadWnd", "<html><head/><body><p><span style=\" color:#00ffd5;\">Загрузка файлов</span></p></body></html>", None))
        self.pbOpen.setText(_translate("DownloadWnd", "Открыть загрузки", None))
        self.pbClose.setText(_translate("DownloadWnd", "Выход", None))
        self.lbFile.setText(_translate("DownloadWnd", "<html><head/><body><p><span style=\" color:#ffffff;\">TextLabel</span></p></body></html>", None))

