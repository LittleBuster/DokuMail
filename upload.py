#!/usr/bin/python
# -*- coding: utf-8 -*-

import platform
import uploadWnd
from PyQt4 import QtGui
from PyQt4 import QtCore
from paths import AppPath
from wndparams import WndParams


class UploadWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(UploadWindow, self).__init__()
        self.ui = uploadWnd.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint)

        WndParams().on_screen_center(self)

        if  platform.system() == "Linux":
            app_path = AppPath().main()
            self.ui.label.setPixmap(QtGui.QPixmap( "".join((app_path, "images/isend.png")) ))

    def closeEvent(self, e):
        e.ignore()