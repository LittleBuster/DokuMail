#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import getpass
import taskWnd
import platform
from PyQt4 import QtGui


class TaskWnd(QtGui.QDialog):
    def __init__(self, parent=None):
        super(TaskWnd, self).__init__()
        self.ui = taskWnd.Ui_TaskWnd()
        self.ui.setupUi(self)
        self.ui.pbClose.clicked.connect(self.on_close)
        self.ui.teMsg.selectionChanged.connect(self.on_clear_click)

        width = self.frameGeometry().width()
        height = self.frameGeometry().height()

        wid = QtGui.QDesktopWidget()
        screenWidth = wid.screen().width()
        screenHeight = wid.screen().height()

        self.setGeometry((screenWidth / 2) - (width / 2), (screenHeight / 2) - (height / 2), width, height)

        self.app_path = ""
        if  platform.system() == "Linux":
            self.app_path = os.path.join("/home", getpass.getuser(), ".doku/")
            self.ui.label.setPixmap(QtGui.QPixmap( "".join((self.app_path, "images/fon.jpg")) ))
            self.ui.label_2.setPixmap(QtGui.QPixmap( "".join((self.app_path, "images/filenew_8842.ico")) ))
            self.ui.pbClose.setIcon(QtGui.QIcon( "".join((self.app_path, "images/exit.png")) ))
            self.ui.pbSendTask.setIcon(QtGui.QIcon( "".join((self.app_path, "images/cloud.png")) ))

    def on_close(self):
        self.close()

    def on_clear_click(self):
        if (self.ui.teMsg.document().toPlainText() == "Опишите проблему..."):
            self.ui.teMsg.clear()