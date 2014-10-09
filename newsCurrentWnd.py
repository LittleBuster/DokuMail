# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newsCurrentWnd.ui'
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

class Ui_UpdateWnd(object):
    def setupUi(self, UpdateWnd):
        UpdateWnd.setObjectName(_fromUtf8("UpdateWnd"))
        UpdateWnd.resize(719, 319)
        UpdateWnd.setMinimumSize(QtCore.QSize(719, 319))
        UpdateWnd.setMaximumSize(QtCore.QSize(719, 451))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/downloads.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UpdateWnd.setWindowIcon(icon)
        self.label = QtGui.QLabel(UpdateWnd)
        self.label.setGeometry(QtCore.QRect(-280, -270, 1101, 801))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/fon.jpg")))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(UpdateWnd)
        self.label_3.setGeometry(QtCore.QRect(110, 5, 531, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lbFile = QtGui.QLabel(UpdateWnd)
        self.lbFile.setGeometry(QtCore.QRect(0, 250, 711, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lbFile.setFont(font)
        self.lbFile.setAlignment(QtCore.Qt.AlignCenter)
        self.lbFile.setObjectName(_fromUtf8("lbFile"))
        self.label_4 = QtGui.QLabel(UpdateWnd)
        self.label_4.setGeometry(QtCore.QRect(250, 50, 231, 231))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("images/database-icon-219.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(UpdateWnd)
        QtCore.QMetaObject.connectSlotsByName(UpdateWnd)

    def retranslateUi(self, UpdateWnd):
        UpdateWnd.setWindowTitle(_translate("UpdateWnd", "Загрузка", None))
        self.label_3.setText(_translate("UpdateWnd", "<html><head/><body><p><span style=\" color:#00ffd5;\">Обновление файлов DokuMail</span></p></body></html>", None))
        self.lbFile.setText(_translate("UpdateWnd", "<html><head/><body><p><span style=\" color:#00d2ff;\">Обновление файлов</span></p></body></html>", None))

