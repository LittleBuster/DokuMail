#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
	def __init__(self, mw, icon, parent=None):
		QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)

		self._mw = mw

		menu = QtWidgets.QMenu(parent)
		
		shAction = menu.addAction("Показать")
		shAction.setIcon(QtGui.QIcon("images/cmp.ico"))
		shAction.triggered.connect(self.show_main)

		shAction2 = menu.addAction("О программе")
		shAction2.setIcon(QtGui.QIcon("images/elena8d89.png"))
		shAction2.triggered.connect(self.show_about)

		shAction3 = menu.addAction("Выход")
		shAction3.setIcon(QtGui.QIcon("images/exit.png"))
		shAction3.triggered.connect(self.close_app)

		self.setContextMenu(menu)
		self.activated.connect(self.on_active)

	def on_active(self, reason):
		"""
		If 1 click
		"""
		if reason == 3:
			self._mw.show()

	def show_main(self):
		self._mw.show()

	def show_about(self):
		self._mw.show()
		self._mw.ui.stackedWidget.setCurrentIndex(5)

	def close_app(self):
		w = QtWidgets.QWidget()
		w.setWindowIcon(QtGui.QIcon("images/exit.png"))
		result = QtWidgets.QMessageBox.question(w, 'Закрытие', 'Вы действительно хотите выйти из программы?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
		if result == QtWidgets.QMessageBox.Yes:
			sys.exit()
