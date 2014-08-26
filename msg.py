#!/usr/bin/python
# -*- coding: utf-8 -*-

import msgWnd
from PyQt5 import QtWidgets


class MsgWnd(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MsgWnd, self).__init__()
        self.ui = msgWnd.Ui_MsgWnd()
        self.ui.setupUi(self)
        self.ui.pbClose.clicked.connect(self.on_close)

        width = self.frameGeometry().width()
        height = self.frameGeometry().height()

        wid = QtWidgets.QDesktopWidget()
        screenWidth = wid.screen().width()
        screenHeight = wid.screen().height()

        self.setGeometry((screenWidth / 2) - (width / 2), (screenHeight / 2) - (height / 2), width, height)

    def closeEvent(self, e):
        e.ignore()
        self.hide()

    def on_close(self):
        self.close()