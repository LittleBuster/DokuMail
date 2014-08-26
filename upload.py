#!/usr/bin/python
# -*- coding: utf-8 -*-

import uploadWnd
from PyQt5 import QtCore
from PyQt5 import QtWidgets


class UploadWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(UploadWindow, self).__init__()
        self.ui = uploadWnd.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint)

        width = self.frameGeometry().width()
        height = self.frameGeometry().height()

        wid = QtWidgets.QDesktopWidget()
        screenWidth = wid.screen().width()
        screenHeight = wid.screen().height()

        self.setGeometry((screenWidth / 2) - (width / 2), (screenHeight / 2) - (height / 2), width, height)

    def closeEvent(self, e):
        e.ignore()