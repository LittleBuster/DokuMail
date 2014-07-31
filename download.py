#!/usr/bin/python
# -*- coding: utf-8 -*-

import downloadWnd
from PyQt5 import QtWidgets
import subprocess
import platform


class DownloadWnd(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super(DownloadWnd, self).__init__()
		self.ui = downloadWnd.Ui_DownloadWnd()
		self.ui.setupUi(self)
		self.ui.pbClose.clicked.connect(self.on_close)
		self.ui.pbOpen.clicked.connect(self.on_open_dir)

	def on_close(self):
		self.close()

	def on_open_dir(self):
		if not platform.system() == "Linux":
			subprocess.call("explorer downloads/", shell=True)
		else:
			subprocess.call("nautilus downloads/", shell=True)
		self.close()