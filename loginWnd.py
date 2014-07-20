# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWnd.ui'
#
# Created: Wed Jul 23 22:17:43 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(613, 340)
        self.lbBack = QtWidgets.QLabel(Form)
        self.lbBack.setGeometry(QtCore.QRect(0, 0, 613, 340))
        self.lbBack.setText("")
        self.lbBack.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbBack.setObjectName("lbBack")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, -20, 601, 121))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 601, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(248, 110, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pbLogin = QtWidgets.QPushButton(Form)
        self.pbLogin.setGeometry(QtCore.QRect(80, 280, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbLogin.setFont(font)
        self.pbLogin.setStyleSheet("QPushButton {\n"
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
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbLogin.setIcon(icon)
        self.pbLogin.setIconSize(QtCore.QSize(24, 24))
        self.pbLogin.setObjectName("pbLogin")
        self.edLogin = QtWidgets.QLineEdit(Form)
        self.edLogin.setGeometry(QtCore.QRect(140, 150, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.edLogin.setFont(font)
        self.edLogin.setObjectName("edLogin")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(240, 249, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.edPasswd = QtWidgets.QLineEdit(Form)
        self.edPasswd.setGeometry(QtCore.QRect(140, 203, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.edPasswd.setFont(font)
        self.edPasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edPasswd.setObjectName("edPasswd")
        self.cbSave = QtWidgets.QCheckBox(Form)
        self.cbSave.setGeometry(QtCore.QRect(210, 250, 21, 22))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.cbSave.setFont(font)
        self.cbSave.setText("")
        self.cbSave.setChecked(True)
        self.cbSave.setObjectName("cbSave")
        self.pbCancel = QtWidgets.QPushButton(Form)
        self.pbCancel.setGeometry(QtCore.QRect(300, 280, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbCancel.setFont(font)
        self.pbCancel.setStyleSheet("QPushButton {\n"
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
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCancel.setIcon(icon1)
        self.pbCancel.setIconSize(QtCore.QSize(24, 24))
        self.pbCancel.setObjectName("pbCancel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Система Обмена Данными"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:72pt; color:#00ffc8;\">DokuMail</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; color:#00ffc8;\">Универсальная Система Обмена Данными</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Логин:</span></p></body></html>"))
        self.pbLogin.setText(_translate("Form", "Вход"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Запомнить пароль</span></p></body></html>"))
        self.pbCancel.setText(_translate("Form", "Отмена"))

