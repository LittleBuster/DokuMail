#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json
import sqlite3
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
import datetime
from task import TaskWnd
from recieve import Recieve, RecieveMsg
from news import NewsWnd, NewsCurWnd, NewsBaloonWnd


class pObj(object):
	"""
	JSON temp class
	"""
	pass


class MainWindow(QtWidgets.QDialog):
	__MDBServer = str
	__MDBUser = str
	__MDBPasswd = str
	__TCPServer = str
	__TCPPort = int

	def __init__(self, parent=None):
		super(MainWindow, self).__init__()
		self.ui = mainWnd.Ui_Form()
		self.ui.setupUi(self)

		self.user = str
		self.passwd = str
		self.news_count = 0

		self.ui.pbMinimize.clicked.connect(self.minimize_app)
		self.tr = SystemTrayIcon(self, QtGui.QIcon("images/cmp.ico"))
		self.tr.show()		
		
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
		self.ui.pbCreateTask.clicked.connect(self.on_create_task)

		"""
		Task List
		"""

		self.ui.cbTaskType.addItem("")
		self.ui.cbTaskType.addItem("Microsoft Office")
		self.ui.cbTaskType.addItem("Интернет")
		self.ui.cbTaskType.addItem("Принтер")
		self.ui.cbTaskType.addItem("Антивирус")
		self.ui.cbTaskType.addItem("Другое")
		self.ui.cbTaskDiff.addItem("Низкая")
		self.ui.cbTaskDiff.addItem("Средняя")
		self.ui.cbTaskDiff.addItem("Высокая")

		lst = list()
		lst.append("№")
		lst.append("Тип проблемы")
		lst.append("Дата")
		lst.append("Решение")
		self.ui.tw1.setHorizontalHeaderLabels(lst)
		self.ui.tw1.horizontalHeader().resizeSection(0, 30)
		self.ui.tw1.horizontalHeader().resizeSection(1, 350)
		self.ui.tw1.horizontalHeader().resizeSection(2, 100)
		""""""
		
		self.getTmr = QtCore.QTimer()
		self.getTmr.timeout.connect(self.on_get_data)
		self.newsTmr = QtCore.QTimer()
		self.getTmr.timeout.connect(self.check_news)

		self.send_files = SendFiles()
		self.recieve = Recieve()
		self.taskWnd = TaskWnd()
		self.newsWnd = NewsWnd()
		self.newsCurWnd = NewsCurWnd()
		self.recieveMsg = RecieveMsg()
		self.newsBaloon = NewsBaloonWnd()
		self.recieveMsg.msgComplete.connect(self.on_msg_complete)
		self.recieve.downloadComplete.connect(self.on_download_complete)		
		self.taskWnd.ui.pbSendTask.clicked.connect(self.on_send_task)
		self.ui.pbSetConfig.clicked.connect(self.on_set_config)
		self.ui.pbCreateNews.clicked.connect(self.on_create_news)
		self.newsWnd.ui.pbSendNews.clicked.connect(self.on_send_news)
		self.ui.lwNews.itemClicked.connect(self.on_lwnews_clicked)
		self.newsBaloon.ui.pbRead.clicked.connect(self.on_read_news)
		self.newsBaloon.ui.pbClose.clicked.connect(self.on_baloon_close)

	"""
	Properties for configs
	"""
	def setTcpServer(self, server):
		self.__TCPServer = server
		self.ui.leTcpServer.setText(server)

	def getTcpServer(self):
		return self.__TCPServer

	def setTcpPort(self, port):
		self.__TCPPort = port
		self.ui.leTcpPort.setText( str(port) )

	def getTcpPort(self):
		return self.__TCPPort

	def setMDBServer(self, server):
		self.__MDBServer = server
		self.ui.leMDBServer.setText(server)

	def getMDBServer(self):
		return self.__MDBServer

	def setMDBUser(self, user):
		self.__MDBUser = user
		self.ui.leMDBUser.setText(user)

	def getMDBUser(self):
		return self.__MDBUser

	def setMDBPasswd(self, passwd):
		self.__MDBPasswd = passwd
		self.ui.leMDBPasswd.setText(passwd)

	def getMDBPasswd(self):
		return self.__MDBPasswd

	TCPServer = property(getTcpServer, setTcpServer)
	TCPPort = property(getTcpPort, setTcpPort)
	MDBServer = property(getMDBServer, setMDBServer)
	MDBUser = property(getMDBUser, setMDBUser)
	MDBPasswd = property(getMDBPasswd, setMDBPasswd)	

	""""""	

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

		if (mdb.check_messages(self.user) and (not self.recieveMsg.get_msg_status())):
			f = True
			mdb.close()			
			self.recieveMsg.set_configs(self.TCPServer, self.TCPPort, self.user, self.passwd)	
			self.recieveMsg.start()
			return
		
		if not f:
			self.getTmr.start(5000)

	def on_msg_complete(self):
		self.getTmr.start(5000)

	def on_download_complete(self, update):
		if not update:
			self.getTmr.start(5000)
		else:
			QtWidgets.QMessageBox.information(self, 'Complete', 'Обновление завершено', QtWidgets.QMessageBox.Yes)
			sys.exit()

	def on_create_news(self):		
		mdb = MariaDB()
		if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "DokuMail"):
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtWidgets.QMessageBox.Yes)
			return
		if mdb.is_admin( self.user ):
			self.newsWnd.show()
		else:
			QtWidgets.QMessageBox.warning(self, 'Error', 'У вас нет прав на создание новостей!', QtWidgets.QMessageBox.Yes)
		mdb.close()

	def on_send_news(self):
		if self.newsWnd.ui.leTitle.text() == "":
			QtWidgets.QMessageBox.warning(self.newsWnd, 'Error', 'Введите заголовок новости!', QtWidgets.QMessageBox.Yes)
			return

		if self.newsWnd.ui.teNews.document().toPlainText() == "" or self.newsWnd.ui.teNews.document().toPlainText() == "Напишите новость...":
			QtWidgets.QMessageBox.warning(self.newsWnd, 'Error', 'Введите текст новости!', QtWidgets.QMessageBox.Yes)
			return

		mdb = MariaDB()
		if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "DokuMail"):
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtWidgets.QMessageBox.Yes)
			return
		date = datetime.date.today()
		if mdb.send_news( mdb.get_alias_by_user(self.user), self.newsWnd.ui.teNews.document().toPlainText(), self.newsWnd.ui.leTitle.text(), str(date) ):
			self.newsWnd.close()
			QtWidgets.QMessageBox.information(self, 'Complete', 'Новость успешно добавлена!', QtWidgets.QMessageBox.Yes)
		else:
			QtWidgets.QMessageBox.critical(self, 'Error', 'Ошибка добавления новости', QtWidgets.QMessageBox.Yes)
		mdb.close()

	def check_news(self):
		con = sqlite3.connect('news.db')
		cur = con.cursor()

		try:
			cur.execute('CREATE TABLE news(id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(512), date VARCHAR(20))')
			con.commit()
		except:
			pass	
		
		mdb = MariaDB()
		if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "DokuMail"):
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtWidgets.QMessageBox.Yes)
			return
		news_list = mdb.check_news()

		l = len(news_list)
		if l != self.news_count:
			self.news_count = l

			self.ui.lwNews.clear()
			for news in news_list:

				cur.execute("SELECT * FROM news WHERE title='" + news["title"] + "' and date='" + news["date"] + "'")
				if len(cur.fetchall()) == 0:
					cur.execute("INSERT INTO news(title, date) VALUES('" + news["title"] + "', '" + news["date"] + "')")
					con.commit()

					"""
					Show tooltip
					"""
					if not mdb.is_admin(self.user):
						rect = self.newsBaloon.geometry()
						rect.setY(0)
						self.newsBaloon.setGeometry(rect)
						self.newsBaloon.ui.leTitle.setText("[" + news["date"] + "]" + news["title"])
						self.newsBaloon.show()

				item = QtWidgets.QListWidgetItem()
				item.setIcon(QtGui.QIcon("images/news.ico"))
				item.setText("[" + news["date"] + "]" + news["title"])
				self.ui.lwNews.insertItem(0, item)
		mdb.close()
		con.close()

	def on_read_news(self):
		item = QtWidgets.QListWidgetItem()
		item.setText(self.newsBaloon.ui.leTitle.text())
		self.newsBaloon.close()
		self.on_lwnews_clicked(item)

	def on_baloon_close(self):
		self.newsBaloon.close()
		con = sqlite3.connect('news.db')
		cur = con.cursor()
		title = self.newsBaloon.ui.leTitle.text().split("]")[1]
		date = self.newsBaloon.ui.leTitle.text().split("[")[1].split("]")[0]

		cur.execute("DELETE FROM news WHERE title='" + title + "' and date='" + date + "'")
		con.commit()
		con.close()

	def on_send_task(self):
		mdb = MariaDB()
		if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "DokuMail"):
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtWidgets.QMessageBox.Yes)
			return

		date = datetime.date.today()
		if mdb.create_task(self.user, self.taskWnd.ui.teMsg.document().toPlainText(), self.ui.cbTaskType.currentText(), date, self.ui.cbTaskDiff.currentText(), "Нет"):
			self.taskWnd.ui.teMsg.clear()
			self.taskWnd.close()
			self.check_tasks()
			QtWidgets.QMessageBox.information(self, 'Complete', 'Заявка зарегистрирована', QtWidgets.QMessageBox.Yes)
		else:
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка при регистрации заявки', QtWidgets.QMessageBox.Yes)
		mdb.close()

	def on_create_task(self):
		if self.ui.cbTaskType.currentText() != "":
			self.taskWnd.show()
		else:
			QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Выберите тип проблемы!', QtWidgets.QMessageBox.Yes)

	def check_tasks(self):
		self.ui.tw1.setRowCount(0)
		mdb = MariaDB()
		if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "DokuMail"):
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtWidgets.QMessageBox.Yes)
			return
		taskList = mdb.get_task_list(self.user)
	
		for task in taskList:
			self.ui.tw1.setRowCount(self.ui.tw1.rowCount() + 1)
			item = QtWidgets.QTableWidgetItem(task["id"])
			self.ui.tw1.setItem(self.ui.tw1.rowCount() - 1, 0, item)
			item = QtWidgets.QTableWidgetItem(task["type"])
			self.ui.tw1.setItem(self.ui.tw1.rowCount() - 1, 1, item)
			item = QtWidgets.QTableWidgetItem(task["date"])
			self.ui.tw1.setItem(self.ui.tw1.rowCount() - 1, 2, item)
			item = QtWidgets.QTableWidgetItem(task["status"])
			self.ui.tw1.setItem(self.ui.tw1.rowCount() - 1, 3, item)
		mdb.close()

	def on_set_config(self):
		result = QtWidgets.QMessageBox.question(self, 'Configs', 'Применить изменения?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
		if result == QtWidgets.QMessageBox.Yes:
			self.TCPServer = self.ui.leTcpServer.text()
			try:
				self.TCPPort = int(self.ui.leTcpPort.text())
			except:
				QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Неверный номер порта!', QtWidgets.QMessageBox.Yes)
			self.MDBServer = self.ui.leMDBServer.text()
			self.MDBUser = self.ui.leMDBUser.text()
			self.MDBPasswd = self.ui.leMDBPasswd.text()
			self.save_config()

	def on_delete_file(self):
		try:
			self.ui.lwFiles.removeItemWidget( self.ui.lwFiles.takeItem( self.ui.lwFiles.row(self.ui.lwFiles.selectedItems()[0]) ) )
		except:
			QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Выделите файл!', QtWidgets.QMessageBox.Yes)

	def on_news_clicked(self):
		self.ui.stackedWidget.setCurrentIndex(0)

	def on_tasks_clicked(self):
		self.ui.stackedWidget.setCurrentIndex(3)

	def on_settings_clicked(self):
		self.ui.stackedWidget.setCurrentIndex(4)

	def on_about_clicked(self):
		QtWidgets.QMessageBox.information(self, 'About', 'Created by Denisov Foundation (c) 2014', QtWidgets.QMessageBox.Yes)

	def on_messages_clicked(self):
		self.ui.stackedWidget.setCurrentIndex(1)

	def on_files_clicked(self):
		self.ui.stackedWidget.setCurrentIndex(2)

	def on_clear_msg_clicked(self):
		self.ui.teMsg.clear()

	def on_lwnews_clicked(self, item):
		title = str(item.text()).split("]")[1]
		mdb = MariaDB()
		if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "DokuMail"):
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtWidgets.QMessageBox.Yes)
			return
		news = mdb.get_news( title )
		self.newsCurWnd.ui.lbFrom.setText("<html><head/><body><p><span style='color:#ffffff;'>" + news["user"] + "</span></p></body></html>")
		self.newsCurWnd.ui.lbTime.setText("<html><head/><body><p><span style='color:#ffffff;'>" + news["date"] + "</span></p></body></html>")
		self.newsCurWnd.ui.teNews.setPlainText(news["news"])
		self.newsCurWnd.ui.leTitle.setText(news["title"])
		self.newsCurWnd.show()
		mdb.close()		

	def lwusers_item_clicked(self, item):
		self.ui.lbAlias.setText( str(item.text()) )

	def closeEvent(self, e):
		result = QtWidgets.QMessageBox.question(self, 'Закрытие', 'Вы действительно хотите выйти из программы?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
		if result == QtWidgets.QMessageBox.Yes:
			e.accept()
			QtWidgets.QWidget.closeEvent(self, e)
		else:
			e.ignore()

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
			i += 1

		self.check_tasks()
		self.check_news()
		self.getTmr.start(5000)
		self.newsTmr.start(10000)

	def save_config(self):
		f = open("config.dat", "w")
		cfg = pObj()
		cfg.config = {}
		cfg.config["mdbserver"] = self.MDBServer
		cfg.config["mdbuser"] = self.MDBUser
		cfg.config["mdbpasswd"] = self.MDBPasswd
		cfg.config["tcpserver"] = self.TCPServer
		cfg.config["tcpport"] = self.TCPPort
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