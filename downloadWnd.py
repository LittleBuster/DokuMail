# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloadWnd.ui'
#
# Created: Sat Jul 26 18:04:26 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DownloadWnd(object):
    def setupUi(self, DownloadWnd):
        DownloadWnd.setObjectName("DownloadWnd")
        DownloadWnd.resize(719, 422)
        self.pb1 = QtWidgets.QProgressBar(DownloadWnd)
        self.pb1.setGeometry(QtCore.QRect(20, 330, 681, 23))
        self.pb1.setProperty("value", 24)
        self.pb1.setObjectName("pb1")
        self.pb2 = QtWidgets.QProgressBar(DownloadWnd)
        self.pb2.setGeometry(QtCore.QRect(20, 380, 681, 23))
        self.pb2.setStyleSheet("QProgressBar {\n"
"float: left;\n"
"  width: 0;\n"
"  height: 100%;\n"
"  font-size: 12px;\n"
"  line-height: 20px;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  background-color: #428bca;\n"
"  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, .15);\n"
"          box-shadow: inset 0 -1px 0 rgba(0, 0, 0, .15);\n"
"  -webkit-transition: width .6s ease;\n"
"       -o-transition: width .6s ease;\n"
"          transition: width .6s ease;\n"
"\n"
" background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);\n"
"  background-image:      -o-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);\n"
"  background-image:         linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);\n"
"}")
        self.pb2.setProperty("value", 24)
        self.pb2.setObjectName("pb2")
        self.lbFile = QtWidgets.QLabel(DownloadWnd)
        self.lbFile.setGeometry(QtCore.QRect(10, 80, 561, 171))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.lbFile.setFont(font)
        self.lbFile.setObjectName("lbFile")

        self.retranslateUi(DownloadWnd)
        QtCore.QMetaObject.connectSlotsByName(DownloadWnd)

    def retranslateUi(self, DownloadWnd):
        _translate = QtCore.QCoreApplication.translate
        DownloadWnd.setWindowTitle(_translate("DownloadWnd", "Form"))
        self.lbFile.setText(_translate("DownloadWnd", "TextLabel"))

