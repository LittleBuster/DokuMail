#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import platform
import subprocess
import downloadWnd
from PyQt4 import QtGui
from PyQt4 import QtCore
from paths import AppPath
from wndparams import WndParams


class DownloadWnd(QtGui.QWidget):
    """
    Class which connect Download Window interface
    in python app
    """

    def __init__(self, parent=None):
        super(DownloadWnd, self).__init__()
        self.ui = downloadWnd.Ui_DownloadWnd()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pbClose, QtCore.SIGNAL("clicked()"), self.on_close)
        QtCore.QObject.connect(self.ui.pbOpen, QtCore.SIGNAL("clicked()"), self.on_downloads)

        WndParams().on_screen_center(self)

        self.app_path = AppPath().main()

        if  platform.system() == "Linux":
            self.ui.label.setPixmap(QtGui.QPixmap( "".join((self.app_path, "images/fon.jpg")) ))
            self.ui.label_2.setPixmap(QtGui.QPixmap( "".join((self.app_path, "images/network_9488.png")) ))
            self.ui.label_4.setPixmap(QtGui.QPixmap( "".join((self.app_path, "images/Downloads_Folder.png")) ))
            self.ui.pbClose.setIcon(QtGui.QIcon( "".join((self.app_path, "images/exit.png")) ))
            self.ui.pbOpen.setIcon(QtGui.QIcon( "".join((self.app_path, "images/downloads.png")) ))

    def on_close(self):
        self.hide()
        self.ui.lwFiles.clear()

    def on_downloads(self):
        self.hide()
        self.ui.lwFiles.clear()

        if platform.system() == "Linux":
            f = open("".join((self.app_path, "wmanagers.cfg")), "r")
            managers = f.readline().split(',')
            f.close()

            for mngr in managers:
                if os.path.exists("".join(("/usr/bin/", mngr))):
                    subprocess.call("".join((mngr, " ",AppPath().home(), "downloads/")), shell=True)
                    break
        else:
            import win32api
            win32api.ShellExecute(0, 'open', 'downloads', '', '', 1)

    def closeEvent(self, e):
        e.ignore()
        self.hide()
        self.ui.lwFiles.clear()