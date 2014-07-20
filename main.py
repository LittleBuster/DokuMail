#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from send import *
from compress import *
from crypt import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtWidgets
from tray import SystemTrayIcon
from mariadb import MariaDB
from tcpclient import TcpClient


class MainWindow(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__()
		uic.loadUi("mainWnd.ui", self)

		self.MDBServer = str("")
		self.MDBUser = str("")
		self.MDBPasswd = str("")
		self.TCPServer = str("")
		self.TCPPort = 0

		self.user = str("")
		self.passwd = str("")

		self.pbMinimize.clicked.connect(self.minimize_app)
		self.tr = SystemTrayIcon(self, QtGui.QIcon("images/cmp.ico"))
		self.tr.show()
		
		self.pbSendMsg.clicked.connect(self.on_send_msg)
		self.pbSendAllMsg.clicked.connect(self.on_sendall_msg)
		self.lwUsers.itemClicked.connect(self.lwusers_item_clicked)
		self.pbClearMsg.clicked.connect(self.on_clear_msg_clicked)
		self.pbSendFiles.clicked.connect(self.on_sendfiles_clicked)
		self.pbAddFile.clicked.connect(self.on_add_file)
		self.pbClearFiles.clicked.connect(self.on_clear_files)
		self.pbDeleteFile.clicked.connect(self.on_delete_file)
		self.pbSendAllFiles.clicked.connect(self.on_sendall_files)

		self.pbNews.clicked.connect(self.on_news_clicked)
		self.pbMessages.clicked.connect(self.on_messages_clicked)		
		self.pbFiles.clicked.connect(self.on_files_clicked)				
		self.pbTasks.clicked.connect(self.on_tasks_clicked)
		self.pbSettings.clicked.connect(self.on_settings_clicked)
		self.pbAbout.clicked.connect(self.on_about_clicked)

		self.send_files = SendFiles()

	def on_delete_file(self):
		QtWidgets.QMessageBox.information(self, 'Ошибка', 'В разработке!', QtWidgets.QMessageBox.Yes)

	def on_sendall_files(self):
		QtWidgets.QMessageBox.information(self, 'Ошибка', 'В разработке!', QtWidgets.QMessageBox.Yes)

	def on_news_clicked(self):
		QtWidgets.QMessageBox.information(self, 'Ошибка', 'Раздел в разработке!', QtWidgets.QMessageBox.Yes)

	def on_tasks_clicked(self):
		QtWidgets.QMessageBox.information(self, 'Ошибка', 'Раздел в разработке!', QtWidgets.QMessageBox.Yes)

	def on_settings_clicked(self):
		QtWidgets.QMessageBox.information(self, 'Ошибка', 'Раздел в разработке!', QtWidgets.QMessageBox.Yes)

	def on_about_clicked(self):
		QtWidgets.QMessageBox.information(self, 'About', 'Created by Denisov Foundation (c) 2014', QtWidgets.QMessageBox.Yes)

	def on_messages_clicked(self):
		self.stackedWidget.setCurrentIndex(1)

	def on_files_clicked(self):
		self.stackedWidget.setCurrentIndex(2)

	def on_clear_msg_clicked(self):
		self.teMsg.clear()

	def lwusers_item_clicked(self, item):
		self.lbAlias.setText( str(item.text()) )

	def init_app(self):
		mdb = MariaDB()
		if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "DokuMail"):
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtWidgets.QMessageBox.Yes)
			return
		aliases = mdb.get_alias_list()
		mdb.close()

		i = 0
		for alias in aliases:
			item = QtWidgets.QListWidgetItem()
			item.setIcon(QtGui.QIcon("images/cmp.ico"))
			item.setText(alias)
			self.lwUsers.insertItem(i, item)
			i = i+1

	def save_config(self):
		f = open("config.dat", "wb")
		cfg = self.MDBServer + "$" + self.MDBUser + "$" + self.MDBPassword + "$" + self.TCPServer + "$" + self.TCPPort
		f.write(cfg.encode('utf-8'))
		f.close()

	def load_config(self):
		if not os.path.isfile("config.dat"):
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Отсутствует файл конфигураций!', QtWidgets.QMessageBox.Yes)
			sys.exit()
			return
		try:
			f = open("config.dat", "rb")
			cfg = f.readline().decode("utf-8").split("$")
			f.close()
			self.MDBServer = cfg[0]
			self.MDBUser = cfg[1]
			self.MDBPasswd = cfg[2]
			self.TCPServer = cfg[3]
			self.TCPPort = int(cfg[4])
		except:
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка чтения конфигурационного файла!', QtWidgets.QMessageBox.Yes)

	def on_send_msg(self):
		send_msg(self, self.teMsg.document().toPlainText(), False, self.passwd, self.lbAlias.text())

	def on_sendall_msg(self):
		send_msg(self, self.teMsg.document().toPlainText(), True, self.passwd, None)

	def on_sendfiles_clicked(self):
		flist = list()
		items = self.lwFiles.count()

		if items == 0:
			QtWidgets.QMessageBox.warning(self, 'Error', 'Добавьте файлы для передачи', QtWidgets.QMessageBox.Yes)
			return

		for i in range(items):
				flist.append(self.lwFiles.item(i).text())

		self.send_files.send(self, flist, self.lbAlias.text())

	def minimize_app(self):
		self.hide()

	def on_clear_files(self):
		self.lwFiles.clear()

	def on_add_file(self):
		newfn = str("")
		filenames = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open file', 'C:/')
		fl = str(filenames[0]).split("[")[1].split("]")[0].split(",")

		items = self.lwFiles.count()
		for f in fl:
			try:
				newfn = f.split("'")[1].split("'")[0]
			except:
				break

			flag = False
			for i in range(items):
					fname = self.lwFiles.item(i).text()
					if fname == newfn:
						QtWidgets.QMessageBox.warning(self, 'Error', 'Файл "' + newfn + '" уже добавлен в очередь передачи', QtWidgets.QMessageBox.Yes)
						flag = True
						break

			if not flag:
				item = QtWidgets.QListWidgetItem()
				item.setIcon(QtGui.QIcon("images/filenew_8842.ico"))
				item.setText(newfn)
				self.lwFiles.insertItem(0, item)