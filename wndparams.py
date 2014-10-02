#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui


class WndParams():
    """
    Singleton class for set windows location parameters
    """

    def new(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance

    def on_screen_center(self, wnd):
        width = wnd.frameGeometry().width()
        height = wnd.frameGeometry().height()

        wid = QtGui.QDesktopWidget()
        screenWidth = wid.screen().width()
        screenHeight = wid.screen().height()

        wnd.setGeometry((screenWidth / 2) - (width / 2), (screenHeight / 2) - (height / 2), width, height)