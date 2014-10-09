# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWnd.ui'
#
# Created: Fri Oct 10 02:10:28 2014
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
        Form.resize(897, 507)
        Form.setMinimumSize(QtCore.QSize(897, 507))
        Form.setMaximumSize(QtCore.QSize(897, 507))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/network-receive.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 891, 501))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/fon2.png")))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 60, 878, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.widget.setPalette(palette)
        self.widget.setStyleSheet(_fromUtf8("QWidget {\n"
"    background-color: rgba(0, 14, 255, 117);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 10px;\n"
"    min-width: 80px;\n"
"}"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.pbNews = QtGui.QPushButton(self.widget)
        self.pbNews.setGeometry(QtCore.QRect(10, 10, 160, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbNews.setFont(font)
        self.pbNews.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/news.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbNews.setIcon(icon1)
        self.pbNews.setIconSize(QtCore.QSize(20, 20))
        self.pbNews.setObjectName(_fromUtf8("pbNews"))
        self.pbAbout = QtGui.QPushButton(self.widget)
        self.pbAbout.setGeometry(QtCore.QRect(540, 50, 160, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbAbout.setFont(font)
        self.pbAbout.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("images/elena8d89.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAbout.setIcon(icon2)
        self.pbAbout.setIconSize(QtCore.QSize(20, 20))
        self.pbAbout.setObjectName(_fromUtf8("pbAbout"))
        self.pbMessages = QtGui.QPushButton(self.widget)
        self.pbMessages.setGeometry(QtCore.QRect(180, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbMessages.setFont(font)
        self.pbMessages.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("images/Email.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbMessages.setIcon(icon3)
        self.pbMessages.setIconSize(QtCore.QSize(20, 20))
        self.pbMessages.setObjectName(_fromUtf8("pbMessages"))
        self.pbFiles = QtGui.QPushButton(self.widget)
        self.pbFiles.setGeometry(QtCore.QRect(370, 10, 160, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbFiles.setFont(font)
        self.pbFiles.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("images/filenew.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbFiles.setIcon(icon4)
        self.pbFiles.setIconSize(QtCore.QSize(20, 20))
        self.pbFiles.setObjectName(_fromUtf8("pbFiles"))
        self.pbTasks = QtGui.QPushButton(self.widget)
        self.pbTasks.setGeometry(QtCore.QRect(540, 10, 160, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbTasks.setFont(font)
        self.pbTasks.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("images/filenew_8842.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbTasks.setIcon(icon5)
        self.pbTasks.setIconSize(QtCore.QSize(20, 20))
        self.pbTasks.setObjectName(_fromUtf8("pbTasks"))
        self.pbSettings = QtGui.QPushButton(self.widget)
        self.pbSettings.setGeometry(QtCore.QRect(710, 10, 160, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbSettings.setFont(font)
        self.pbSettings.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("images/settings.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbSettings.setIcon(icon6)
        self.pbSettings.setIconSize(QtCore.QSize(20, 20))
        self.pbSettings.setObjectName(_fromUtf8("pbSettings"))
        self.pbRelogin = QtGui.QPushButton(self.widget)
        self.pbRelogin.setGeometry(QtCore.QRect(710, 50, 160, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbRelogin.setFont(font)
        self.pbRelogin.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("images/touser.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbRelogin.setIcon(icon7)
        self.pbRelogin.setIconSize(QtCore.QSize(20, 20))
        self.pbRelogin.setObjectName(_fromUtf8("pbRelogin"))
        self.pbDownloads = QtGui.QPushButton(self.widget)
        self.pbDownloads.setGeometry(QtCore.QRect(370, 50, 160, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbDownloads.setFont(font)
        self.pbDownloads.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("images/downloads.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbDownloads.setIcon(icon8)
        self.pbDownloads.setIconSize(QtCore.QSize(20, 20))
        self.pbDownloads.setObjectName(_fromUtf8("pbDownloads"))
        self.widget_3 = QtGui.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(667, 160, 221, 285))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.widget_3.setPalette(palette)
        self.widget_3.setStyleSheet(_fromUtf8("QWidget#widget_3 {\n"
"    background-color: rgba(0, 14, 255, 117);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 10px;\n"
"    min-width: 80px;\n"
"}"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.lbAlias = QtGui.QLabel(self.widget_3)
        self.lbAlias.setGeometry(QtCore.QRect(60, 246, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbAlias.setFont(font)
        self.lbAlias.setStyleSheet(_fromUtf8("QWidget {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-width: 0px;\n"
"};"))
        self.lbAlias.setText(_fromUtf8(""))
        self.lbAlias.setObjectName(_fromUtf8("lbAlias"))
        self.lwUsers = QtGui.QListWidget(self.widget_3)
        self.lwUsers.setGeometry(QtCore.QRect(10, 30, 201, 211))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lwUsers.setFont(font)
        self.lwUsers.setStyleSheet(_fromUtf8("QWidget {\n"
"    background-color: rgba(23, 115, 255, 137);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.lwUsers.setIconSize(QtCore.QSize(32, 32))
        self.lwUsers.setObjectName(_fromUtf8("lwUsers"))
        self.label_7 = QtGui.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(26, 6, 171, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lbCurUser = QtGui.QLabel(self.widget_3)
        self.lbCurUser.setGeometry(QtCore.QRect(20, 246, 31, 31))
        self.lbCurUser.setText(_fromUtf8(""))
        self.lbCurUser.setPixmap(QtGui.QPixmap(_fromUtf8("images/user.ico")))
        self.lbCurUser.setObjectName(_fromUtf8("lbCurUser"))
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(10, 160, 651, 341))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.widget_2.setPalette(palette)
        self.widget_2.setStyleSheet(_fromUtf8("QWidget#widget_2 {\n"
"    background-color: rgba(0, 14, 255, 117);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 10px;\n"
"    min-width: 80px;\n"
"}"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.stackedWidget = QtGui.QStackedWidget(self.widget_2)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 651, 341))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 255, 89, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 255, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 255, 89, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 255, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 255, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 255, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.stackedWidget.setPalette(palette)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.lwNews = QtGui.QListWidget(self.page)
        self.lwNews.setGeometry(QtCore.QRect(10, 70, 631, 261))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lwNews.setFont(font)
        self.lwNews.setStyleSheet(_fromUtf8("QWidget {\n"
"    background-color: rgba(23, 115, 255, 137);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.lwNews.setIconSize(QtCore.QSize(32, 32))
        self.lwNews.setObjectName(_fromUtf8("lwNews"))
        self.label_16 = QtGui.QLabel(self.page)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 651, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.pbCreateNews = QtGui.QPushButton(self.page)
        self.pbCreateNews.setGeometry(QtCore.QRect(420, 30, 221, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbCreateNews.setFont(font)
        self.pbCreateNews.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.pbCreateNews.setIcon(icon1)
        self.pbCreateNews.setIconSize(QtCore.QSize(20, 20))
        self.pbCreateNews.setObjectName(_fromUtf8("pbCreateNews"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.pbSendMsg = QtGui.QPushButton(self.page_2)
        self.pbSendMsg.setGeometry(QtCore.QRect(10, 290, 200, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbSendMsg.setFont(font)
        self.pbSendMsg.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("images/cloud.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbSendMsg.setIcon(icon9)
        self.pbSendMsg.setIconSize(QtCore.QSize(24, 24))
        self.pbSendMsg.setObjectName(_fromUtf8("pbSendMsg"))
        self.label_4 = QtGui.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 651, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.teMsg = QtGui.QTextEdit(self.page_2)
        self.teMsg.setGeometry(QtCore.QRect(10, 30, 631, 211))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.teMsg.setFont(font)
        self.teMsg.setStyleSheet(_fromUtf8("QWidget {\n"
"    background-color: rgba(255, 255, 255, 71);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"    min-width: 80px;\n"
"}"))
        self.teMsg.setObjectName(_fromUtf8("teMsg"))
        self.pbClearMsg = QtGui.QPushButton(self.page_2)
        self.pbClearMsg.setGeometry(QtCore.QRect(228, 290, 200, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbClearMsg.setFont(font)
        self.pbClearMsg.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("images/recycle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbClearMsg.setIcon(icon10)
        self.pbClearMsg.setIconSize(QtCore.QSize(24, 24))
        self.pbClearMsg.setObjectName(_fromUtf8("pbClearMsg"))
        self.pbSendAllMsg = QtGui.QPushButton(self.page_2)
        self.pbSendAllMsg.setGeometry(QtCore.QRect(442, 290, 200, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbSendAllMsg.setFont(font)
        self.pbSendAllMsg.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("images/users.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbSendAllMsg.setIcon(icon11)
        self.pbSendAllMsg.setIconSize(QtCore.QSize(24, 24))
        self.pbSendAllMsg.setObjectName(_fromUtf8("pbSendAllMsg"))
        self.pbOutgoing = QtGui.QPushButton(self.page_2)
        self.pbOutgoing.setGeometry(QtCore.QRect(340, 250, 221, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbOutgoing.setFont(font)
        self.pbOutgoing.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.pbOutgoing.setIcon(icon1)
        self.pbOutgoing.setIconSize(QtCore.QSize(20, 20))
        self.pbOutgoing.setObjectName(_fromUtf8("pbOutgoing"))
        self.pbIncoming = QtGui.QPushButton(self.page_2)
        self.pbIncoming.setGeometry(QtCore.QRect(110, 250, 221, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbIncoming.setFont(font)
        self.pbIncoming.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.pbIncoming.setIcon(icon1)
        self.pbIncoming.setIconSize(QtCore.QSize(20, 20))
        self.pbIncoming.setObjectName(_fromUtf8("pbIncoming"))
        self.stackedWidget.addWidget(self.page_2)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.pbDeleteFile = QtGui.QPushButton(self.page_6)
        self.pbDeleteFile.setGeometry(QtCore.QRect(10, 290, 200, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbDeleteFile.setFont(font)
        self.pbDeleteFile.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("images/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbDeleteFile.setIcon(icon12)
        self.pbDeleteFile.setIconSize(QtCore.QSize(24, 24))
        self.pbDeleteFile.setObjectName(_fromUtf8("pbDeleteFile"))
        self.label_8 = QtGui.QLabel(self.page_6)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 651, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.pbAddFile = QtGui.QPushButton(self.page_6)
        self.pbAddFile.setGeometry(QtCore.QRect(10, 240, 200, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbAddFile.setFont(font)
        self.pbAddFile.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("images/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAddFile.setIcon(icon13)
        self.pbAddFile.setIconSize(QtCore.QSize(24, 24))
        self.pbAddFile.setObjectName(_fromUtf8("pbAddFile"))
        self.pbClearFiles = QtGui.QPushButton(self.page_6)
        self.pbClearFiles.setGeometry(QtCore.QRect(228, 290, 200, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbClearFiles.setFont(font)
        self.pbClearFiles.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.pbClearFiles.setIcon(icon10)
        self.pbClearFiles.setIconSize(QtCore.QSize(24, 24))
        self.pbClearFiles.setObjectName(_fromUtf8("pbClearFiles"))
        self.pbSendFiles = QtGui.QPushButton(self.page_6)
        self.pbSendFiles.setGeometry(QtCore.QRect(442, 290, 200, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbSendFiles.setFont(font)
        self.pbSendFiles.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.pbSendFiles.setIcon(icon9)
        self.pbSendFiles.setIconSize(QtCore.QSize(24, 24))
        self.pbSendFiles.setObjectName(_fromUtf8("pbSendFiles"))
        self.lwFiles = QtGui.QListWidget(self.page_6)
        self.lwFiles.setGeometry(QtCore.QRect(10, 30, 631, 201))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lwFiles.setFont(font)
        self.lwFiles.setStyleSheet(_fromUtf8("QWidget {\n"
"    background-color: rgba(255, 255, 255, 71);\n"
"    color: rgb(0, 239, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.lwFiles.setIconSize(QtCore.QSize(30, 30))
        self.lwFiles.setObjectName(_fromUtf8("lwFiles"))
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtGui.QWidget()
        self.page_7.setObjectName(_fromUtf8("page_7"))
        self.label_10 = QtGui.QLabel(self.page_7)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 651, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.page_7)
        self.label_11.setGeometry(QtCore.QRect(10, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.tw1 = QtGui.QTableWidget(self.page_7)
        self.tw1.setGeometry(QtCore.QRect(10, 100, 631, 231))
        self.tw1.setStyleSheet(_fromUtf8(""))
        self.tw1.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tw1.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tw1.setRowCount(0)
        self.tw1.setColumnCount(4)
        self.tw1.setObjectName(_fromUtf8("tw1"))
        self.tw1.horizontalHeader().setCascadingSectionResizes(True)
        self.tw1.horizontalHeader().setDefaultSectionSize(300)
        self.tw1.horizontalHeader().setHighlightSections(True)
        self.tw1.horizontalHeader().setStretchLastSection(True)
        self.tw1.verticalHeader().setVisible(False)
        self.tw1.verticalHeader().setCascadingSectionResizes(True)
        self.tw1.verticalHeader().setStretchLastSection(False)
        self.cbTaskType = QtGui.QComboBox(self.page_7)
        self.cbTaskType.setGeometry(QtCore.QRect(10, 60, 211, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cbTaskType.setFont(font)
        self.cbTaskType.setObjectName(_fromUtf8("cbTaskType"))
        self.cbTaskDiff = QtGui.QComboBox(self.page_7)
        self.cbTaskDiff.setGeometry(QtCore.QRect(230, 60, 211, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cbTaskDiff.setFont(font)
        self.cbTaskDiff.setObjectName(_fromUtf8("cbTaskDiff"))
        self.label_12 = QtGui.QLabel(self.page_7)
        self.label_12.setGeometry(QtCore.QRect(230, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.pbCreateTask = QtGui.QPushButton(self.page_7)
        self.pbCreateTask.setGeometry(QtCore.QRect(450, 60, 191, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbCreateTask.setFont(font)
        self.pbCreateTask.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.pbCreateTask.setIcon(icon5)
        self.pbCreateTask.setIconSize(QtCore.QSize(20, 20))
        self.pbCreateTask.setObjectName(_fromUtf8("pbCreateTask"))
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtGui.QWidget()
        self.page_8.setObjectName(_fromUtf8("page_8"))
        self.leTcpServer = QtGui.QLineEdit(self.page_8)
        self.leTcpServer.setGeometry(QtCore.QRect(80, 80, 211, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.leTcpServer.setFont(font)
        self.leTcpServer.setStyleSheet(_fromUtf8("QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 71);\n"
"    border-width: 1px;\n"
"color:rgb(255, 255, 255);\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.leTcpServer.setObjectName(_fromUtf8("leTcpServer"))
        self.label_14 = QtGui.QLabel(self.page_8)
        self.label_14.setGeometry(QtCore.QRect(80, 57, 171, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.page_8)
        self.label_15.setGeometry(QtCore.QRect(80, 116, 171, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.leTcpPort = QtGui.QLineEdit(self.page_8)
        self.leTcpPort.setGeometry(QtCore.QRect(80, 140, 211, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.leTcpPort.setFont(font)
        self.leTcpPort.setStyleSheet(_fromUtf8("QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 71);\n"
"    border-width: 1px;\n"
"color:rgb(255, 255, 255);\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.leTcpPort.setObjectName(_fromUtf8("leTcpPort"))
        self.label_17 = QtGui.QLabel(self.page_8)
        self.label_17.setGeometry(QtCore.QRect(350, 57, 171, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.leMDBUser = QtGui.QLineEdit(self.page_8)
        self.leMDBUser.setGeometry(QtCore.QRect(350, 140, 211, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.leMDBUser.setFont(font)
        self.leMDBUser.setStyleSheet(_fromUtf8("QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 71);\n"
"    border-width: 1px;\n"
"color:rgb(255, 255, 255);\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.leMDBUser.setObjectName(_fromUtf8("leMDBUser"))
        self.leMDBServer = QtGui.QLineEdit(self.page_8)
        self.leMDBServer.setGeometry(QtCore.QRect(350, 80, 211, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.leMDBServer.setFont(font)
        self.leMDBServer.setStyleSheet(_fromUtf8("QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 71);\n"
"    border-width: 1px;\n"
"color:rgb(255, 255, 255);\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.leMDBServer.setObjectName(_fromUtf8("leMDBServer"))
        self.leMDBPasswd = QtGui.QLineEdit(self.page_8)
        self.leMDBPasswd.setGeometry(QtCore.QRect(350, 200, 211, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.leMDBPasswd.setFont(font)
        self.leMDBPasswd.setStyleSheet(_fromUtf8("QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 71);\n"
"    border-width: 1px;\n"
"color:rgb(255, 255, 255);\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.leMDBPasswd.setEchoMode(QtGui.QLineEdit.Password)
        self.leMDBPasswd.setObjectName(_fromUtf8("leMDBPasswd"))
        self.label_20 = QtGui.QLabel(self.page_8)
        self.label_20.setGeometry(QtCore.QRect(350, 177, 171, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.page_8)
        self.label_21.setGeometry(QtCore.QRect(350, 117, 171, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.page_8)
        self.label_22.setGeometry(QtCore.QRect(30, 0, 611, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.page_8)
        self.label_23.setGeometry(QtCore.QRect(110, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(self.page_8)
        self.label_24.setGeometry(QtCore.QRect(380, 20, 151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.pbSetConfig = QtGui.QPushButton(self.page_8)
        self.pbSetConfig.setGeometry(QtCore.QRect(220, 250, 200, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbSetConfig.setFont(font)
        self.pbSetConfig.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.pbSetConfig.setIcon(icon6)
        self.pbSetConfig.setIconSize(QtCore.QSize(24, 24))
        self.pbSetConfig.setObjectName(_fromUtf8("pbSetConfig"))
        self.stackedWidget.addWidget(self.page_8)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.label_18 = QtGui.QLabel(self.page_3)
        self.label_18.setGeometry(QtCore.QRect(320, 0, 221, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.lbAbout = QtGui.QLabel(self.page_3)
        self.lbAbout.setGeometry(QtCore.QRect(10, 60, 171, 251))
        self.lbAbout.setText(_fromUtf8(""))
        self.lbAbout.setPixmap(QtGui.QPixmap(_fromUtf8("images/about.png")))
        self.lbAbout.setObjectName(_fromUtf8("lbAbout"))
        self.textEdit = QtGui.QTextEdit(self.page_3)
        self.textEdit.setGeometry(QtCore.QRect(190, 50, 451, 281))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(_fromUtf8("QWidget {\n"
"    background-color: rgba(23, 115, 255, 137);\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.pbClearHistory = QtGui.QPushButton(self.page_4)
        self.pbClearHistory.setGeometry(QtCore.QRect(140, 290, 200, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbClearHistory.setFont(font)
        self.pbClearHistory.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.pbClearHistory.setIcon(icon10)
        self.pbClearHistory.setIconSize(QtCore.QSize(24, 24))
        self.pbClearHistory.setObjectName(_fromUtf8("pbClearHistory"))
        self.pbCloseHistory = QtGui.QPushButton(self.page_4)
        self.pbCloseHistory.setGeometry(QtCore.QRect(350, 290, 200, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbCloseHistory.setFont(font)
        self.pbCloseHistory.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("images/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCloseHistory.setIcon(icon14)
        self.pbCloseHistory.setIconSize(QtCore.QSize(24, 24))
        self.pbCloseHistory.setObjectName(_fromUtf8("pbCloseHistory"))
        self.label_19 = QtGui.QLabel(self.page_4)
        self.label_19.setGeometry(QtCore.QRect(0, 0, 651, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.lwHistory = QtGui.QListWidget(self.page_4)
        self.lwHistory.setGeometry(QtCore.QRect(10, 30, 631, 251))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lwHistory.setFont(font)
        self.lwHistory.setStyleSheet(_fromUtf8("QWidget {\n"
"    background-color: rgba(23, 115, 255, 137);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.lwHistory.setIconSize(QtCore.QSize(32, 32))
        self.lwHistory.setObjectName(_fromUtf8("lwHistory"))
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.stackedWidget.addWidget(self.page_5)
        self.widget_4 = QtGui.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(667, 450, 221, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 14, 255, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.widget_4.setPalette(palette)
        self.widget_4.setStyleSheet(_fromUtf8("QWidget {\n"
"    background-color: rgba(0, 14, 255, 117);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 10px;\n"
"    min-width: 80px;\n"
"}"))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.pbMinimize = QtGui.QPushButton(self.widget_4)
        self.pbMinimize.setGeometry(QtCore.QRect(10, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbMinimize.setFont(font)
        self.pbMinimize.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color:qlineargradient(spread:reflect, x1:0.515, y1:1, x2:0.528, y2:0, stop:0 rgba(0, 143, 250, 255), stop:0.655502 rgba(0, 29, 203, 255), stop:1 rgba(190, 255, 255, 255));\n"
"    color:rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
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
        self.pbMinimize.setObjectName(_fromUtf8("pbMinimize"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(240, 0, 221, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, -3, 64, 51))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("images/conv.ico")))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(420, 5, 501, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_13 = QtGui.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(20, 5, 141, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lbStatus = QtGui.QLabel(Form)
        self.lbStatus.setGeometry(QtCore.QRect(10, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbStatus.setFont(font)
        self.lbStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lbStatus.setObjectName(_fromUtf8("lbStatus"))

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Doku", None))
        self.pbNews.setText(_translate("Form", "Новости", None))
        self.pbAbout.setText(_translate("Form", "О программе", None))
        self.pbMessages.setText(_translate("Form", "Сообщения", None))
        self.pbFiles.setText(_translate("Form", "Файлы", None))
        self.pbTasks.setText(_translate("Form", "Заявки", None))
        self.pbSettings.setText(_translate("Form", "Настройки", None))
        self.pbRelogin.setText(_translate("Form", "Выйти", None))
        self.pbDownloads.setText(_translate("Form", "Загрузки", None))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#00e9ff;\">Список пользователей</span></p></body></html>", None))
        self.label_16.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Новости учреждения</span></p></body></html>", None))
        self.pbCreateNews.setText(_translate("Form", "Написать новость", None))
        self.pbSendMsg.setText(_translate("Form", "Отправить", None))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Отправить сообщение</span></p></body></html>", None))
        self.pbClearMsg.setText(_translate("Form", "Очистить", None))
        self.pbSendAllMsg.setText(_translate("Form", "Отправить всем", None))
        self.pbOutgoing.setText(_translate("Form", "Исходящие", None))
        self.pbIncoming.setText(_translate("Form", "Входящие", None))
        self.pbDeleteFile.setText(_translate("Form", "Удалить файл", None))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Отправить файлы</span></p></body></html>", None))
        self.pbAddFile.setText(_translate("Form", "Добавить файл", None))
        self.pbClearFiles.setText(_translate("Form", "Очистить", None))
        self.pbSendFiles.setText(_translate("Form", "Отправить", None))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Заявка на починку/обслуживание ПК системному администратору:</span></p></body></html>", None))
        self.label_11.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#00f8ff;\">Тип проблемы:</span></p></body></html>", None))
        self.label_12.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#00f8ff;\">Срочность:</span></p></body></html>", None))
        self.pbCreateTask.setText(_translate("Form", "Подать заявку", None))
        self.label_14.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#00fffa;\">Server Address:</span></p></body></html>", None))
        self.label_15.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#00fffa;\">Server Port:</span></p></body></html>", None))
        self.label_17.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#00fffa;\">Server Address:</span></p></body></html>", None))
        self.label_20.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#00fffa;\">Server Password:</span></p></body></html>", None))
        self.label_21.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#00fffa;\">Server Login:</span></p></body></html>", None))
        self.label_22.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Конфигурации:</span></p></body></html>", None))
        self.label_23.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">TCP Server:</span></p></body></html>", None))
        self.label_24.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">MariaDB Server:</span></p></body></html>", None))
        self.pbSetConfig.setText(_translate("Form", "Применить", None))
        self.label_18.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#00ffd8;\">DokuMail</span></p></body></html>", None))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-weight:400; color:#ffffff;\">Система обмена данными DokuMail написана мной с целью обеспечить обмен документами и сообщениями между сотрудниками малых и средних организаций, а также сотрудниками учебных учреждений. Высокая скорость локальной сети позволяет в мгновение ока передавать какие-либо документы. Больше не нужно искать папку сотрудника или учителя, которому нужно отправить файл, среди большого количества непонятных сетевых папок. Достаточно просто выбрать кабинет в который нужно отправить файл и нажать на кнопку &quot;Отправить&quot;. Также не стоит беспокоиться о защите данных, каждый файл и сообщение перед передачей по сети шифруется самым современным на сегодняшний день алгоритмом симметричного шифрования и сжимается алгоритмом, использующимся в онлайн-играх, где передаётся огромное количество трафика по сети. Злоумышленник перехватив сообщение, никогда не сможет расшифровать его. Сообщение или файл доставляется именно тому человеку, которому он предназначен.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-weight:400; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-weight:400; color:#ffffff;\">По вопросам и предложениям обращаться DenisovS21@gmail.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-weight:400; color:#ffffff;\">Denisov Sergey 2014</span></p></body></html>", None))
        self.pbClearHistory.setText(_translate("Form", "Очистить", None))
        self.pbCloseHistory.setText(_translate("Form", "Закрыть", None))
        self.label_19.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">История</span></p></body></html>", None))
        self.pbMinimize.setText(_translate("Form", "Свернуть программу", None))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#00ffd8;\">DokuMail</span></p></body></html>", None))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#00e9ff;\">Быстрая и защищённая внутрикорпоративная почта </span></p><p align=\"center\"><span style=\" color:#00e9ff;\">для малых, средних организаций и учебных учреждений</span></p></body></html>", None))
        self.label_13.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#00e9ff;\">Статус сервера:</span></p></body></html>", None))
        self.lbStatus.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#f5ff00;\">Соединение...</span></p></body></html>", None))

