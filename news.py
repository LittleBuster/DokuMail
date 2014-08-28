#!/usr/bin/python
# -*- coding: utf-8 -*-

import newsWnd
import newsCurrentWnd
import newsBaloon
from PyQt4 import QtCore
from PyQt4 import QtGui


class NewsWnd(QtGui.QDialog):
    """
    Write news
    """

    def __init__(self, parent=None):
        super(NewsWnd, self).__init__()
        self.ui = newsWnd.Ui_NewsWnd()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.pbClose, QtCore.SIGNAL("clicked()"), self.on_close)
        QtCore.QObject.connect(self.ui.teNews, QtCore.SIGNAL("selectionChanged()"), self.on_clear_click)

        width = self.frameGeometry().width()
        height = self.frameGeometry().height()

        wid = QtGui.QDesktopWidget()
        screenWidth = wid.screen().width()
        screenHeight = wid.screen().height()

        self.setGeometry((screenWidth / 2) - (width / 2), (screenHeight / 2) - (height / 2), width, height)

    def on_close(self):
        self.close()

    def on_clear_click(self):
        """
        Clear temporary string
        """
        if self.ui.teNews.document().toPlainText() == "Haпишите новость...":
            self.ui.teNews.clear()


class NewsCurWnd(QtGui.QWidget):
    """
    Show current news window
    """

    def __init__(self, parent=None):
        super(NewsCurWnd, self).__init__()
        self.ui = newsCurrentWnd.Ui_CurNewsWnd()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.pbClose, QtCore.SIGNAL("clicked()"), self.on_close)

        width = self.frameGeometry().width()
        height = self.frameGeometry().height()

        wid = QtGui.QDesktopWidget()
        screenWidth = wid.screen().width()
        screenHeight = wid.screen().height()

        self.setGeometry((screenWidth / 2) - (width / 2), (screenHeight / 2) - (height / 2), width, height)

    def on_close(self):
        self.close()


class NewsBaloonWnd(QtGui.QWidget):
    """
    If news not exists in local databse
    Then show tooltip with news header
    """
    hideBaloon = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(NewsBaloonWnd, self).__init__()
        self.ui = newsBaloon.Ui_NewsBaloon()
        self.ui.setupUi(self)

        width = self.frameGeometry().width()
        height = self.frameGeometry().height()

        wid = QtGui.QDesktopWidget()
        screenWidth = wid.screen().width()
        screenHeight = wid.screen().height()

        self.setGeometry((screenWidth / 2) - (width / 2), (screenHeight / 2) - (height / 2), width, height)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowStaysOnTopHint)

    def closeEvent(self, e):
        e.ignore()
        self.hide()
        self.hideBaloon.emit()