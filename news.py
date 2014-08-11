#!/usr/bin/python
# -*- coding: utf-8 -*-

import newsWnd
import newsCurrentWnd
import newsBaloon
from PyQt5 import QtWidgets


class NewsWnd(QtWidgets.QDialog):
	"""
	Write news
	"""
	def __init__(self, parent=None):
		super(NewsWnd, self).__init__()
		self.ui = newsWnd.Ui_NewsWnd()
		self.ui.setupUi(self)
		self.ui.pbClose.clicked.connect(self.on_close)
		self.ui.teNews.selectionChanged.connect(self.on_clear_click)

		width = self.frameGeometry().width()
		height = self.frameGeometry().height()

		wid = QtWidgets.QDesktopWidget()
		screenWidth = wid.screen().width()
		screenHeight = wid.screen().height()

		self.setGeometry((screenWidth/2)-(width/2),(screenHeight/2)-(height/2),width,height)

	def on_close(self):
		self.close()

	def on_clear_click(self):
		if (self.ui.teNews.document().toPlainText() == "Напишите новость..."):
			self.ui.teNews.clear()


class NewsCurWnd(QtWidgets.QDialog):
	"""
	Show current news window
	"""
	def __init__(self, parent=None):
		super(NewsCurWnd, self).__init__()
		self.ui = newsCurrentWnd.Ui_CurNewsWnd()
		self.ui.setupUi(self)
		self.ui.pbClose.clicked.connect(self.on_close)

		width = self.frameGeometry().width()
		height = self.frameGeometry().height()

		wid = QtWidgets.QDesktopWidget()
		screenWidth = wid.screen().width()
		screenHeight = wid.screen().height()

		self.setGeometry((screenWidth/2)-(width/2),(screenHeight/2)-(height/2),width,height)

	def on_close(self):
		self.close()


class NewsBaloonWnd(QtWidgets.QDialog):
	"""
	If news not exists in local databse
	Then show tooltip with news header
	"""
	def __init__(self, parent=None):
		super(NewsBaloonWnd, self).__init__()
		self.ui = newsBaloon.Ui_NewsBaloon()
		self.ui.setupUi(self)

	def closeEvent(self, e):
		e.ignore()
		self.hide()