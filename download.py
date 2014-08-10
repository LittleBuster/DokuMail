#!/usr/bin/python
# -*- coding: utf-8 -*-

import downloadWnd
from PyQt5 import QtWidgets
import subprocess
import platform


class DownloadWnd(QtWidgets.QDialog):
	"""
	Class which connect Download Window interface
	in python app
	"""
	def __init__(self, parent=None):
		super(DownloadWnd, self).__init__()
		self.ui = downloadWnd.Ui_DownloadWnd()
		self.ui.setupUi(self)
		self.ui.pbClose.clicked.connect(self.on_close)
		self.ui.pbOpen.clicked.connect(self.on_open_dir)

	def on_close(self):
		self.close()

	def on_open_dir(self):
		"""
		Open local folder for downloads
		"""
		if platform.system() == "Linux":
			subprocess.call("nautilus downloads/", shell=True)
		else:
			import win32api
			win32api.ShellExecute(0, 'open', 'downloads', '', '', 1)
		self.close()
