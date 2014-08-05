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

	def on_close(self):
		self.close()