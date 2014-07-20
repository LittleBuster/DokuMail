#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtWidgets


class UploadWindow(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super(UploadWindow, self).__init__()
		uic.loadUi("uploadWnd.ui", self)