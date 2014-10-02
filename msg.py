#!/usr/bin/python
# -*- coding: utf-8 -*-

import msgWnd
import platform
from PyQt4 import QtGui
from PyQt4 import QtCore
from paths import AppPath
from wndparams import WndParams



class MsgWnd(QtGui.QDialog):
    """
    Show Message class
    """
    def __init__(self, parent=None):
        super(MsgWnd, self).__init__()
        self.ui = msgWnd.Ui_MsgWnd()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.pbClose, QtCore.SIGNAL("clicked()"), self.on_close)
        WndParams().on_screen_center(self)

        if  platform.system() == "Linux":
            app_path = AppPath().main()
            self.ui.label.setPixmap(QtGui.QPixmap( "".join((app_path, "images/fon.jpg")) ))
            self.ui.label_2.setPixmap(QtGui.QPixmap( "".join((app_path, "images/conv.ico")) ))
            self.ui.pbClose.setIcon(QtGui.QIcon( "".join((app_path, "images/exit.png")) ))

    def closeEvent(self, e):
        e.ignore()
        self.hide()

    def on_close(self):
        self.close()