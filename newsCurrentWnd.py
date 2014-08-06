# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newsCurrentWnd.ui'
#
# Created: Wed Aug  6 16:42:28 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CurNewsWnd(object):
    def setupUi(self, CurNewsWnd):
        CurNewsWnd.setObjectName("CurNewsWnd")
        CurNewsWnd.resize(719, 451)
        CurNewsWnd.setMinimumSize(QtCore.QSize(719, 451))
        CurNewsWnd.setMaximumSize(QtCore.QSize(719, 451))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/news.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CurNewsWnd.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(CurNewsWnd)
        self.label.setGeometry(QtCore.QRect(-210, -120, 941, 671))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/fon.jpg"))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(CurNewsWnd)
        self.label_2.setGeometry(QtCore.QRect(290, 200, 141, 141))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/news.ico"))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(CurNewsWnd)
        self.label_3.setGeometry(QtCore.QRect(290, 5, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.pbClose = QtWidgets.QPushButton(CurNewsWnd)
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
        self.lbFile = QtWidgets.QLabel(CurNewsWnd)
        self.lbFile.setGeometry(QtCore.QRect(20, 40, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbFile.setFont(font)
        self.lbFile.setObjectName("lbFile")
        self.teNews = QtWidgets.QTextEdit(CurNewsWnd)
        self.teNews.setGeometry(QtCore.QRect(20, 160, 681, 231))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.teNews.setFont(font)
        self.teNews.setStyleSheet("QWidget {\n"
"    background-color: rgba(23, 115, 255, 137);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}")
        self.teNews.setReadOnly(True)
        self.teNews.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.teNews.setObjectName("teNews")
        self.lbFile_2 = QtWidgets.QLabel(CurNewsWnd)
        self.lbFile_2.setGeometry(QtCore.QRect(470, 40, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbFile_2.setFont(font)
        self.lbFile_2.setObjectName("lbFile_2")
        self.lbFrom = QtWidgets.QLabel(CurNewsWnd)
        self.lbFrom.setGeometry(QtCore.QRect(140, 40, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbFrom.setFont(font)
        self.lbFrom.setObjectName("lbFrom")
        self.lbTime = QtWidgets.QLabel(CurNewsWnd)
        self.lbTime.setGeometry(QtCore.QRect(550, 40, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbTime.setFont(font)
        self.lbTime.setObjectName("lbTime")
        self.leTitle = QtWidgets.QLineEdit(CurNewsWnd)
        self.leTitle.setGeometry(QtCore.QRect(20, 96, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.leTitle.setFont(font)
        self.leTitle.setStyleSheet("QLineEdit {\n"
"    background-color: rgba(23, 115, 255, 137);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}")
        self.leTitle.setText("")
        self.leTitle.setReadOnly(True)
        self.leTitle.setObjectName("leTitle")
        self.label_21 = QtWidgets.QLabel(CurNewsWnd)
        self.label_21.setGeometry(QtCore.QRect(20, 73, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(CurNewsWnd)
        self.label_22.setGeometry(QtCore.QRect(20, 130, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")

        self.retranslateUi(CurNewsWnd)
        QtCore.QMetaObject.connectSlotsByName(CurNewsWnd)

    def retranslateUi(self, CurNewsWnd):
        _translate = QtCore.QCoreApplication.translate
        CurNewsWnd.setWindowTitle(_translate("CurNewsWnd", "Новость"))
        self.label_3.setText(_translate("CurNewsWnd", "<html><head/><body><p><span style=\" color:#00ffd5;\">Новость</span></p></body></html>"))
        self.pbClose.setText(_translate("CurNewsWnd", "Закрыть Новость"))
        self.lbFile.setText(_translate("CurNewsWnd", "<html><head/><body><p><span style=\" color:#00dbff;\">От кого:</span></p></body></html>"))
        self.lbFile_2.setText(_translate("CurNewsWnd", "<html><head/><body><p><span style=\" color:#00dbff;\">Дата:</span></p></body></html>"))
        self.lbFrom.setText(_translate("CurNewsWnd", "<html><head/><body><p><span style=\" color:#ffffff;\">От кого:</span></p></body></html>"))
        self.lbTime.setText(_translate("CurNewsWnd", "<html><head/><body><p><span style=\" color:#ffffff;\">22:23:23</span></p></body></html>"))
        self.label_21.setText(_translate("CurNewsWnd", "<html><head/><body><p><span style=\" color:#00fffa;\">Заголовок:</span></p></body></html>"))
        self.label_22.setText(_translate("CurNewsWnd", "<html><head/><body><p><span style=\" color:#00fffa;\">Подробное описание:</span></p></body></html>"))

