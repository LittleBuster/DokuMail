# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newsCurrentWnd.ui'
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

class Ui_CurNewsWnd(object):
    def setupUi(self, CurNewsWnd):
        CurNewsWnd.setObjectName(_fromUtf8("CurNewsWnd"))
        CurNewsWnd.resize(719, 451)
        CurNewsWnd.setMinimumSize(QtCore.QSize(719, 451))
        CurNewsWnd.setMaximumSize(QtCore.QSize(719, 451))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/news.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CurNewsWnd.setWindowIcon(icon)
        self.label = QtGui.QLabel(CurNewsWnd)
        self.label.setGeometry(QtCore.QRect(-210, -120, 941, 671))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/fon.jpg")))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(CurNewsWnd)
        self.label_2.setGeometry(QtCore.QRect(290, 200, 141, 141))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/news.ico")))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(CurNewsWnd)
        self.label_3.setGeometry(QtCore.QRect(290, 5, 151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pbClose = QtGui.QPushButton(CurNewsWnd)
        self.pbClose.setGeometry(QtCore.QRect(340, 400, 241, 41))
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
        self.lbFile = QtGui.QLabel(CurNewsWnd)
        self.lbFile.setGeometry(QtCore.QRect(20, 40, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbFile.setFont(font)
        self.lbFile.setObjectName(_fromUtf8("lbFile"))
        self.teNews = QtGui.QTextEdit(CurNewsWnd)
        self.teNews.setGeometry(QtCore.QRect(20, 160, 681, 231))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.teNews.setFont(font)
        self.teNews.setStyleSheet(_fromUtf8("QWidget {\n"
"    background-color: rgba(23, 115, 255, 137);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.teNews.setReadOnly(True)
        self.teNews.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.teNews.setObjectName(_fromUtf8("teNews"))
        self.lbFile_2 = QtGui.QLabel(CurNewsWnd)
        self.lbFile_2.setGeometry(QtCore.QRect(480, 40, 71, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbFile_2.setFont(font)
        self.lbFile_2.setObjectName(_fromUtf8("lbFile_2"))
        self.lbFrom = QtGui.QLabel(CurNewsWnd)
        self.lbFrom.setGeometry(QtCore.QRect(140, 40, 241, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbFrom.setFont(font)
        self.lbFrom.setObjectName(_fromUtf8("lbFrom"))
        self.lbTime = QtGui.QLabel(CurNewsWnd)
        self.lbTime.setGeometry(QtCore.QRect(560, 40, 161, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbTime.setFont(font)
        self.lbTime.setObjectName(_fromUtf8("lbTime"))
        self.leTitle = QtGui.QLineEdit(CurNewsWnd)
        self.leTitle.setGeometry(QtCore.QRect(20, 96, 531, 31))
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
        self.leTitle.setReadOnly(True)
        self.leTitle.setObjectName(_fromUtf8("leTitle"))
        self.label_21 = QtGui.QLabel(CurNewsWnd)
        self.label_21.setGeometry(QtCore.QRect(20, 73, 171, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(CurNewsWnd)
        self.label_22.setGeometry(QtCore.QRect(20, 130, 211, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.pbDeleteNews = QtGui.QPushButton(CurNewsWnd)
        self.pbDeleteNews.setGeometry(QtCore.QRect(130, 400, 201, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbDeleteNews.setFont(font)
        self.pbDeleteNews.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("images/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbDeleteNews.setIcon(icon2)
        self.pbDeleteNews.setIconSize(QtCore.QSize(24, 24))
        self.pbDeleteNews.setObjectName(_fromUtf8("pbDeleteNews"))

        self.retranslateUi(CurNewsWnd)
        QtCore.QMetaObject.connectSlotsByName(CurNewsWnd)

    def retranslateUi(self, CurNewsWnd):
        CurNewsWnd.setWindowTitle(_translate("CurNewsWnd", "Новость", None))
        self.label_3.setText(_translate("CurNewsWnd", "<html><head/><body><p><span style=\" color:#00ffd5;\">Новость</span></p></body></html>", None))
        self.pbClose.setText(_translate("CurNewsWnd", "Закрыть Новость", None))
        self.lbFile.setText(_translate("CurNewsWnd", "<html><head/><body><p><span style=\" color:#00dbff;\">От кого:</span></p></body></html>", None))
        self.teNews.setHtml(_translate("CurNewsWnd", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.lbFile_2.setText(_translate("CurNewsWnd", "<html><head/><body><p><span style=\" color:#00dbff;\">Дата:</span></p></body></html>", None))
        self.lbFrom.setText(_translate("CurNewsWnd", "<html><head/><body><p><span style=\" color:#ffffff;\">От кого:</span></p></body></html>", None))
        self.lbTime.setText(_translate("CurNewsWnd", "<html><head/><body><p><span style=\" color:#ffffff;\">22:23:23</span></p></body></html>", None))
        self.label_21.setText(_translate("CurNewsWnd", "<html><head/><body><p><span style=\" color:#00fffa;\">Заголовок:</span></p></body></html>", None))
        self.label_22.setText(_translate("CurNewsWnd", "<html><head/><body><p><span style=\" color:#00fffa;\">Подробное описание:</span></p></body></html>", None))
        self.pbDeleteNews.setText(_translate("CurNewsWnd", "Удалить Новость", None))

