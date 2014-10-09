# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWnd.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(613, 340)
        Form.setMinimumSize(QtCore.QSize(613, 340))
        Form.setMaximumSize(QtCore.QSize(613, 340))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/network-receive.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.lbBack = QtGui.QLabel(Form)
        self.lbBack.setGeometry(QtCore.QRect(-20, -40, 661, 391))
        self.lbBack.setText(_fromUtf8(""))
        self.lbBack.setPixmap(QtGui.QPixmap(_fromUtf8("images/fon3.png")))
        self.lbBack.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbBack.setObjectName(_fromUtf8("lbBack"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 20, 601, 121))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(248, 120, 111, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pbLogin = QtGui.QPushButton(Form)
        self.pbLogin.setGeometry(QtCore.QRect(80, 280, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbLogin.setFont(font)
        self.pbLogin.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/login.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbLogin.setIcon(icon1)
        self.pbLogin.setIconSize(QtCore.QSize(24, 24))
        self.pbLogin.setObjectName(_fromUtf8("pbLogin"))
        self.edLogin = QtGui.QLineEdit(Form)
        self.edLogin.setGeometry(QtCore.QRect(140, 165, 321, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.edLogin.setFont(font)
        self.edLogin.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    background-color: rgba(23, 115, 255, 137);\n"
"    border-width: 1px;\n"
"color:rgb(255, 255, 255);\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.edLogin.setText(_fromUtf8(""))
        self.edLogin.setObjectName(_fromUtf8("edLogin"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(240, 245, 191, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.edPasswd = QtGui.QLineEdit(Form)
        self.edPasswd.setGeometry(QtCore.QRect(140, 205, 321, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.edPasswd.setFont(font)
        self.edPasswd.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    background-color: rgba(23, 115, 255, 137);\n"
"    border-width: 1px;\n"
"color:rgb(255, 255, 255);\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.edPasswd.setText(_fromUtf8(""))
        self.edPasswd.setEchoMode(QtGui.QLineEdit.Password)
        self.edPasswd.setObjectName(_fromUtf8("edPasswd"))
        self.cbSave = QtGui.QCheckBox(Form)
        self.cbSave.setGeometry(QtCore.QRect(210, 245, 21, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        self.cbSave.setFont(font)
        self.cbSave.setText(_fromUtf8(""))
        self.cbSave.setChecked(True)
        self.cbSave.setObjectName(_fromUtf8("cbSave"))
        self.pbCancel = QtGui.QPushButton(Form)
        self.pbCancel.setGeometry(QtCore.QRect(300, 280, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbCancel.setFont(font)
        self.pbCancel.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("images/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCancel.setIcon(icon2)
        self.pbCancel.setIconSize(QtCore.QSize(24, 24))
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 10, 241, 47))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/logo.png")))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Система Обмена Данными", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:48pt; color:#00ffc8;\">DokuMail</span></p></body></html>", None))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Логин:</span></p></body></html>", None))
        self.pbLogin.setText(_translate("Form", "Вход", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Запомнить пароль</span></p></body></html>", None))
        self.pbCancel.setText(_translate("Form", "Отмена", None))

