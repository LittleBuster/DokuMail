#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
from mariadb import MariaDB
from PyQt5 import QtGui, QtWidgets
from PyQt5 import QtCore, uic


class pObj(object):
	"""
	JSON temp class
	"""
	pass


class LoginWindow(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super(LoginWindow, self).__init__()
		uic.loadUi("loginWnd.ui", self)
		self.loginTmr = QtCore.QTimer()
		self.loginTmr.timeout.connect(self.on_autologin)
		self.pbLogin.clicked.connect(self.on_login)
		self.pbCancel.clicked.connect(self.on_cancel)
		self.lbBack.setPixmap(QtGui.QPixmap("images/ffupd.png"))

		if os.path.isfile("svpwd.dat"):
			self.load_passwd()

	def set_wnds(self, mw):
		self._mw = mw
		if not ((self.edLogin.text() == "") or (self.edPasswd.text() == "")):
			self.loginTmr.start(2000)

	def on_login(self):
		self.loginTmr.stop()
		state = False

		if (self.edLogin.text() == "") or (self.edPasswd.text() == ""):
			QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Введите логин или пароль!', QtWidgets.QMessageBox.Yes)
			return

		if (self.cbSave.checkState() == QtCore.Qt.Checked):
			self.save_passwd()

		mdb = MariaDB()
		if not mdb.connect(self._mw.MDBServer, self._mw.MDBUser, self._mw.MDBPasswd, "DokuMail"):
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtWidgets.QMessageBox.Yes)
			return
		state = mdb.check_login(self.edLogin.text(), self.edPasswd.text())
		mdb.close()

		if state == True:
			self.hide()
			self._mw.show()
			self._mw.init_app()
			self._mw.passwd = self.edPasswd.text()
			self._mw.user = self.edLogin.text()
		else:
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Неверный логин или пароль!', QtWidgets.QMessageBox.Yes)
						

	def save_passwd(self):
		f = open("svpwd.dat", "w")
		cfgPasswd = pObj()
		cfgPasswd.config = {}
		cfgPasswd.config["login"] = self.edLogin.text()
		cfgPasswd.config["passwd"] = self.edPasswd.text()
		json.dump(cfgPasswd.config, f)
		f.close()

	def load_passwd(self):
		try:
			f = open("svpwd.dat", "r")
			cfgPasswd = json.load(f)
			self.edLogin.setText( cfgPasswd["login"] )
			self.edPasswd.setText( cfgPasswd["passwd"] )
			f.close()
		except:
			self.edLogin.setText("")
			self.edPasswd.setText("")
			os.remove("svpwd.dat")

	def on_autologin(self):
		self.loginTmr.stop()
		self.on_login()

	def on_cancel(self):
		self.loginTmr.stop()
		self.edLogin.setText("")
		self.edPasswd.setText("")
