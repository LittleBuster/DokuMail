#!/usr/bin/python
# -*- coding: utf-8 -*-
import downloadWnd
from PyQt5 import QtWidgets


class DownloadWnd(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super(DownloadWnd, self).__init__()
		self.ui = downloadWnd.Ui_DownloadWnd()
		self.ui.setupUi(self)