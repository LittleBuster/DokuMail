#!/usr/bin/python
# -*- coding: utf-8 -*-

import updateWnd
from PyQt5 import QtWidgets

class UpdateWnd(QtWidgets.QDialog):
	"""
	Class which connect Update Window interface
	in python app
	"""
	def __init__(self, parent=None):
		super(UpdateWnd, self).__init__()
		self.ui = updateWnd.Ui_UpdateWnd()
		self.ui.setupUi(self)