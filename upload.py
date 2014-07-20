#!/usr/bin/python
# -*- coding: utf-8 -*-

import uploadWnd
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtWidgets


class UploadWindow(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super(UploadWindow, self).__init__()
		self.ui = uploadWnd.Ui_Form()
		self.ui.setupUi(self)