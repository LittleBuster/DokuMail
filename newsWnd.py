# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newsWnd.ui'
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

class Ui_NewsWnd(object):
    def setupUi(self, NewsWnd):
        NewsWnd.setObjectName(_fromUtf8("NewsWnd"))
        NewsWnd.resize(719, 451)
        NewsWnd.setMinimumSize(QtCore.QSize(718, 451))
        NewsWnd.setMaximumSize(QtCore.QSize(719, 451))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/filenew_8842.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NewsWnd.setWindowIcon(icon)
        self.label = QtGui.QLabel(NewsWnd)
        self.label.setGeometry(QtCore.QRect(-210, -120, 941, 671))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/fon.jpg")))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(NewsWnd)
        self.label_2.setGeometry(QtCore.QRect(290, 190, 121, 121))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/news.ico")))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(NewsWnd)
        self.label_3.setGeometry(QtCore.QRect(210, 0, 311, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pbClose = QtGui.QPushButton(NewsWnd)
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
        self.teNews = QtGui.QTextEdit(NewsWnd)
        self.teNews.setGeometry(QtCore.QRect(20, 140, 681, 251))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.teNews.setFont(font)
        self.teNews.setStyleSheet(_fromUtf8("QTextEdit {\n"
"    background-color: rgba(23, 115, 255, 137);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.teNews.setObjectName(_fromUtf8("teNews"))
        self.pbSendNews = QtGui.QPushButton(NewsWnd)
        self.pbSendNews.setGeometry(QtCore.QRect(310, 400, 241, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbSendNews.setFont(font)
        self.pbSendNews.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.pbSendNews.setIcon(icon2)
        self.pbSendNews.setIconSize(QtCore.QSize(24, 24))
        self.pbSendNews.setObjectName(_fromUtf8("pbSendNews"))
        self.label_21 = QtGui.QLabel(NewsWnd)
        self.label_21.setGeometry(QtCore.QRect(20, 57, 171, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.leTitle = QtGui.QLineEdit(NewsWnd)
        self.leTitle.setGeometry(QtCore.QRect(20, 80, 531, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(17)
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
        self.leTitle.setObjectName(_fromUtf8("leTitle"))
        self.label_22 = QtGui.QLabel(NewsWnd)
        self.label_22.setGeometry(QtCore.QRect(20, 114, 211, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))

        self.retranslateUi(NewsWnd)
        QtCore.QMetaObject.connectSlotsByName(NewsWnd)

    def retranslateUi(self, NewsWnd):
        NewsWnd.setWindowTitle(_translate("NewsWnd", "Написать новость", None))
        self.label_3.setText(_translate("NewsWnd", "<html><head/><body><p><span style=\" color:#00ffd5;\">Написать новость</span></p></body></html>", None))
        self.pbClose.setText(_translate("NewsWnd", "Закрыть", None))
        self.teNews.setHtml(_translate("NewsWnd", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Haпишите новость...</span></p></body></html>", None))
        self.pbSendNews.setText(_translate("NewsWnd", "Отправить новость", None))
        self.label_21.setText(_translate("NewsWnd", "<html><head/><body><p><span style=\" color:#00fffa;\">Заголовок:</span></p></body></html>", None))
        self.label_22.setText(_translate("NewsWnd", "<html><head/><body><p><span style=\" color:#00fffa;\">Подробное описание:</span></p></body></html>", None))

