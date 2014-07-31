#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json
from send import *
from compress import *
from crypt import *
from PyQt5 import QtCore, Qt
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtWidgets
from tray import SystemTrayIcon
from mariadb import MariaDB
from tcpclient import TcpClient
import mainWnd
from recieve import Recieve


class pObj(object):
	"""
	JSON temp class
	"""
	pass


class MainWindow(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__()
		self.ui = mainWnd.Ui_Form()
		self.ui.setupUi(self)

		self.MDBServer = str("")
		self.MDBUser = str("")
		self.MDBPasswd = str("")
		self.TCPServer = str("")
		self.TCPPort = 0

		self.user = str("")
		self.passwd = str("")

		self.ui.pbMinimize.clicked.connect(self.minimize_app)
		self.tr = SystemTrayIcon(self, QtGui.QIcon("images/cmp.ico"))
		self.tr.show()

		self.ui.cbTaskType.addItem("Microsoft Office")
		self.ui.cbTaskType.addItem("Интернет")
		self.ui.cbTaskType.addItem("Принтер")
		
		self.ui.pbSendMsg.clicked.connect(self.on_send_msg)
		self.ui.pbSendAllMsg.clicked.connect(self.on_sendall_msg)
		self.ui.lwUsers.itemClicked.connect(self.lwusers_item_clicked)
		self.ui.pbClearMsg.clicked.connect(self.on_clear_msg_clicked)
		self.ui.pbSendFiles.clicked.connect(self.on_sendfiles_clicked)
		self.ui.pbAddFile.clicked.connect(self.on_add_file)
		self.ui.pbClearFiles.clicked.connect(self.on_clear_files)
		self.ui.pbDeleteFile.clicked.connect(self.on_delete_file)

		self.ui.pbNews.clicked.connect(self.on_news_clicked)
		self.ui.pbMessages.clicked.connect(self.on_messages_clicked)		
		self.ui.pbFiles.clicked.connect(self.on_files_clicked)				
		self.ui.pbTasks.clicked.connect(self.on_tasks_clicked)
		self.ui.pbSettings.clicked.connect(self.on_settings_clicked)
		self.ui.pbAbout.clicked.connect(self.on_about_clicked)

		"""
		ti1 = QtWidgets.QTableWidgetItem("lolita")
		ti2 = QtWidgets.QTableWidgetItem("pkkkkkkkkkkkkkkkkkkkkkkkkkkkkipec")

		self.tw1.setItem(0,0,ti1)
		self.tw1.setItem(0,1,ti2)
		lst = list()
		lst.append("hfjsdhf")
		lst.append("lolofffffffffffffffffffffffffffffl")
		lst.append("ddfsd")
		self.tw1.setHorizontalHeaderLabels(lst)

		self.tw1.horizontalHeader().resizeSection(0, 10)
		"""

		self.getTmr = QtCore.QTimer()
		self.getTmr.timeout.connect(self.on_get_data)

		self.send_files = SendFiles()
		self.recieve = Recieve()
		self.recieve.downloadComplete.connect(self.on_download_complete)

	def on_get_data(self):
		self.getTmr.stop()

		client = TcpClient()
		if not client.check_status(self.TCPServer, self.TCPPort):
			self.ui.lbStatus.setText("<html><head/><body><p><span style='color:#ff0000;'>Оффлайн</span></p></body></html>")
			self.getTmr.start(5000)
			return
		else:
			client.close()
			self.ui.lbStatus.setText("<html><head/><body><p><span style='color:#00ff0b;'>Онлайн</span></p></body></html>")

		f = False
		mdb = MariaDB()
		if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "DokuMail"):
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtWidgets.QMessageBox.Yes)
			return

		if mdb.check_update(self.user):
			f = True
			mdb.close()
			self.recieve.set_configs(self.TCPServer, self.TCPPort, self.user, self.passwd, True)	
			self.recieve.start()
			return

		if mdb.check_files(self.user):
			f = True
			mdb.close()
			self.recieve.set_configs(self.TCPServer, self.TCPPort, self.user, self.passwd, False)	
			self.recieve.start()
			return
		
		if not f:
			self.getTmr.start(5000)

	def on_download_complete(self, update):
		if not update:
			self.getTmr.start(5000)
		else:
			QtWidgets.QMessageBox.information(self, 'Ошибка', 'Обновление завершено', QtWidgets.QMessageBox.Yes)
			sys.exit()

	def on_delete_file(self):
		try:
			self.ui.lwFiles.removeItemWidget( self.ui.lwFiles.takeItem( self.ui.lwFiles.row(self.ui.lwFiles.selectedItems()[0]) ) )
		except:
			QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Выделите файл!', QtWidgets.QMessageBox.Yes)

	def on_news_clicked(self):
		QtWidgets.QMessageBox.information(self, 'Ошибка', 'Раздел в разработке!', QtWidgets.QMessageBox.Yes)

	def on_tasks_clicked(self):
		QtWidgets.QMessageBox.information(self, 'Ошибка', 'Раздел в разработке!', QtWidgets.QMessageBox.Yes)

	def on_settings_clicked(self):
		QtWidgets.QMessageBox.information(self, 'Ошибка', 'Раздел в разработке!', QtWidgets.QMessageBox.Yes)

	def on_about_clicked(self):
		QtWidgets.QMessageBox.information(self, 'About', 'Created by Denisov Foundation (c) 2014', QtWidgets.QMessageBox.Yes)

	def on_messages_clicked(self):
		self.ui.stackedWidget.setCurrentIndex(1)

	def on_files_clicked(self):
		self.ui.stackedWidget.setCurrentIndex(2)

	def on_clear_msg_clicked(self):
		self.ui.teMsg.clear()

	def lwusers_item_clicked(self, item):
		self.ui.lbAlias.setText( str(item.text()) )

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
			self.ui.lwUsers.insertItem(i, item)
			i = i+1

		self.getTmr.start(5000)

	def save_config(self):
		f = open("config.dat", "w")
		cfg = pObj()
		cfg.config = {}
		cfg.config["mdbserver"] = "94.232.48.110"#self.MDBServer
		cfg.config["mdbuser"] = "doku"#self.MDBUser
		cfg.config["mdbpasswd"] = "School184"#self.MDBPassword
		cfg.config["tcpserver"] = "94.232.48.110"#self.TCPServer
		cfg.config["tcpport"] = 5000#self.TCPPort
		json.dump(cfg.config, f)
		f.close()

	def load_config(self):
		if not os.path.isfile("config.dat"):
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Отсутствует файл конфигураций!', QtWidgets.QMessageBox.Yes)
			sys.exit()
			return
		try:
			f = open("config.dat", "r")
			cfg = json.load(f)

			self.MDBServer = cfg["mdbserver"]
			self.MDBUser = cfg["mdbuser"]
			self.MDBPasswd = cfg["mdbpasswd"]
			self.TCPServer = cfg["tcpserver"]
			self.TCPPort = cfg["tcpport"]
			f.close()
		except:
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка чтения конфигурационного файла!', QtWidgets.QMessageBox.Yes)

	def on_send_msg(self):
		send_msg(self, self.ui.teMsg.document().toPlainText(), False, self.passwd, self.ui.lbAlias.text())

	def on_sendall_msg(self):
		send_msg(self, self.ui.teMsg.document().toPlainText(), True, self.passwd, None)

	def on_sendfiles_clicked(self):
		flist = list()
		items = self.ui.lwFiles.count()

		if items == 0:
			QtWidgets.QMessageBox.warning(self, 'Error', 'Добавьте файлы для передачи', QtWidgets.QMessageBox.Yes)
			return

		for i in range(items):
				flist.append(self.ui.lwFiles.item(i).text())

		self.send_files.send(self, flist, self.ui.lbAlias.text())

	def minimize_app(self):
		self.hide()

	def on_clear_files(self):
		self.ui.lwFiles.clear()

	def on_add_file(self):
		newfn = str("")
		filenames = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open file', 'C:/')
		fl = str(filenames[0]).split("[")[1].split("]")[0].split(",")

		items = self.ui.lwFiles.count()
		for f in fl:
			try:
				newfn = f.split("'")[1].split("'")[0]
			except:
				break

			flag = False
			for i in range(items):
					fname = self.ui.lwFiles.item(i).text()
					if fname == newfn:
						QtWidgets.QMessageBox.warning(self, 'Error', 'Файл "' + newfn + '" уже добавлен в очередь передачи', QtWidgets.QMessageBox.Yes)
						flag = True
						break

			if not flag:
				item = QtWidgets.QListWidgetItem()
				item.setIcon(QtGui.QIcon("images/filenew_8842.ico"))
				item.setText(newfn)
				self.ui.lwFiles.insertItem(0, item)