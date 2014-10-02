#!/usr/bin/python
# -*- coding: utf-8 -*-

import taskWnd
import platform
from PyQt4 import QtGui
from paths import AppPath
from wndparams import WndParams


class TaskWnd(QtGui.QDialog):
    def __init__(self, parent=None):
        super(TaskWnd, self).__init__()
        self.ui = taskWnd.Ui_TaskWnd()
        self.ui.setupUi(self)
        self.ui.pbClose.clicked.connect(self.on_close)
        self.ui.teMsg.selectionChanged.connect(self.on_clear_click)
        WndParams().on_screen_center(self)

        if  platform.system() == "Linux":
            app_path = AppPath().main()
            self.ui.label.setPixmap(QtGui.QPixmap( "".join((app_path, "images/fon.jpg")) ))
            self.ui.label_2.setPixmap(QtGui.QPixmap( "".join((app_path, "images/filenew_8842.ico")) ))
            self.ui.pbClose.setIcon(QtGui.QIcon( "".join((app_path, "images/exit.png")) ))
            self.ui.pbSendTask.setIcon(QtGui.QIcon( "".join((app_path, "images/cloud.png")) ))

    def on_close(self):
        self.close()

    def on_clear_click(self):
        if (self.ui.teMsg.document().toPlainText() == "Опишите проблему..."):
            self.ui.teMsg.clear()