#!/usr/bin/python
# -*- coding: utf-8 -*-

import taskWnd
from PyQt5 import QtWidgets


class TaskWnd(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super(TaskWnd, self).__init__()
		self.ui = taskWnd.Ui_TaskWnd()
		self.ui.setupUi(self)
		self.ui.pbClose.clicked.connect(self.on_close)
		self.ui.teMsg.selectionChanged.connect(self.on_clear_click)

	def on_close(self):
		self.close()

	def on_clear_click(self):
		if (self.ui.teMsg.document().toPlainText() == "Опишите проблему..."):
			self.ui.teMsg.clear()