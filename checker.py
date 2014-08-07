#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtGui
from tcpclient import TcpClient
from mariadb import MariaDB
import sqlite3


class CheckerThread(QtCore.QThread):
	task = str
	user = str
	configs = {}
	msg_status = bool
	news_count = int

	serverOffline = QtCore.pyqtSignal()
	serverOnline = QtCore.pyqtSignal()
	err = QtCore.pyqtSignal(str)
	nothingAvailable = QtCore.pyqtSignal()
	updateAvailable = QtCore.pyqtSignal()
	msgAvailable = QtCore.pyqtSignal()
	filesAvailable = QtCore.pyqtSignal()
	showNewsBaloon = QtCore.pyqtSignal([str, str])
	addNews = QtCore.pyqtSignal([str, str])
	setNewsCount = QtCore.pyqtSignal(int)
	clearNews = QtCore.pyqtSignal()

	def __init__(self):
		super(CheckerThread, self).__init__()

	def set_configs(self, configs, user):
		self.configs = configs
		self.user = user

	def run(self):
		if self.task == "news":
			con = sqlite3.connect('news.db')
			cur = con.cursor()

			try:
				cur.execute('CREATE TABLE news(id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(512), date VARCHAR(20))')
				con.commit()
			except:
				pass	
		
			mdb = MariaDB()
			if not mdb.connect(self.configs["MDBServer"], self.configs["MDBUser"], self.configs["MDBPasswd"], "DokuMail"):
				QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtWidgets.QMessageBox.Yes)
				return
			news_list = mdb.check_news()

			l = len(news_list)
			if l != self.news_count:
				self.setNewsCount.emit(l)
				self.clearNews.emit()

				for news in news_list:
					cur.execute("SELECT * FROM news WHERE title='" + news["title"] + "' and date='" + news["date"] + "'")
					if len(cur.fetchall()) == 0:
						cur.execute("INSERT INTO news(title, date) VALUES('" + news["title"] + "', '" + news["date"] + "')")
						con.commit()

						"""
						Show tooltip
						"""
						if not mdb.is_admin(self.user):
							self.showNewsBaloon.emit(news["date"], news["title"])

					self.addNews.emit(news["date"], news["title"])
			mdb.close()
			con.close()

		elif self.task == "msg_and_files":
			"""
			Checking server status (online/offline)
			"""

			client = TcpClient()
			if not client.check_status(self.configs["TcpServer"], self.configs["TcpPort"]):
				self.serverOffline.emit()				
			else:
				self.serverOnline.emit()
			client.close()

			"""
			Checking update, messages, files
			"""			
			mdb = MariaDB()
			if not mdb.connect(self.configs["MDBServer"], self.configs["MDBUser"], self.configs["MDBPasswd"], "DokuMail"):
				self.err.emit("Ошибка соединения с Базой Данных!", self.task)
				return

			if mdb.check_update(self.user):
				mdb.close()
				print("Доступны обновления.")
				self.updateAvailable.emit()
				return

			if mdb.check_files(self.user):
				mdb.close()
				print("Есть новые файлы.")
				self.filesAvailable.emit()
				return

			if (mdb.check_messages(self.user) and (not self.msg_status)):
				mdb.close()
				print("Есть новые сообщения.")
				self.msgAvailable.emit()
				return

			print("nothing")
			mdb.close()
			self.nothingAvailable.emit()


class Checker():
	"""
	Class for checking update, messages, files and checking server status
	"""
	def __init__(self, wnd):
		self.mainWnd = wnd
		self.getTmr = QtCore.QTimer()
		self.getTmr.timeout.connect(self.check_msg_and_files)
		self.newsTmr = QtCore.QTimer()
		self.newsTmr.timeout.connect(self.check_news)

		self.th_c = CheckerThread()
		self.th_n = CheckerThread()

	"""
	Checker thread signals
	"""
	def on_show_baloon(self, date, title):
		rect = self.mainWnd.newsBaloon.geometry()
		rect.setY(0)
		self.mainWnd.newsBaloon.setGeometry(rect)
		self.mainWnd.newsBaloon.ui.leTitle.setText("[" + date + "]" + title)
		self.mainWnd.newsBaloon.show()

	def on_add_news(self, date, title):
		item = QtWidgets.QListWidgetItem()
		item.setIcon(QtGui.QIcon("images/news.ico"))
		item.setText("[" + date + "]" + title)
		self.mainWnd.ui.lwNews.insertItem(0, item)

	def on_online_server(self):
		self.mainWnd.ui.lbStatus.setText("<html><head/><body><p><span style='color:#00ff0b;'>Онлайн</span></p></body></html>")

	def on_offline_server(self):
		self.mainWnd.ui.lbStatus.setText("<html><head/><body><p><span style='color:#ff0000;'>Оффлайн</span></p></body></html>")

	def on_error(string, task):
		QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtWidgets.QMessageBox.Yes)
		if task == "news":
			self.newsTmr.start(10000)
		elif task == "msg_and_files":
			self.getTmr.start(5000)

	def on_update_available(self):
		self.mainWnd.recieve.set_configs(self.mainWnd.TCPServer, self.mainWnd.TCPPort, self.mainWnd.user, self.mainWnd.passwd, True)	
		self.mainWnd.recieve.start()

	def on_files_available(self):
		self.mainWnd.recieve.set_configs(self.mainWnd.TCPServer, self.mainWnd.TCPPort, self.mainWnd.user, self.mainWnd.passwd, False)	
		self.mainWnd.recieve.start()

	def on_msg_available(self):
		self.recieveMsg.set_configs(self.mainWnd.TCPServer, self.mainWnd.TCPPort, self.mainWnd.user, self.mainWnd.passwd)	
		self.recieveMsg.start()

	def on_nothing_available(self):
		self.getTmr.start(5000)

	def on_set_newscount(self, count):
		self.mainWnd.news_count = count

	def on_clear_news(self):
		self.mainWnd.ui.lwNews.clear()

	"""
	Timer's signals
	"""

	def check_news(self):		
		self.th_n.task = "news"
		self.th_n.news_count = self.mainWnd.news_count
		self.th_n.err.connect(self.on_error)
		self.th_n.showNewsBaloon.connect(self.on_show_baloon)
		self.th_n.addNews.connect(self.on_add_news)
		self.th_n.setNewsCount.connect(self.on_set_newscount)
		self.th_n.clearNews.connect(self.on_clear_news)
		self.th_n.start()

	def check_msg_and_files(self):
		self.getTmr.stop()
		
		self.th_c.task = "msg_and_files"
		self.th_c.msg_status = self.mainWnd.recieveMsg.get_msg_status()

		self.th_c.err.connect(self.on_error)
		self.th_c.serverOnline.connect(self.on_online_server)
		self.th_c.serverOffline.connect(self.on_offline_server)
		self.th_c.updateAvailable.connect(self.on_update_available)
		self.th_c.filesAvailable.connect(self.on_files_available)
		self.th_c.msgAvailable.connect(self.on_msg_available)
		self.th_c.nothingAvailable.connect(self.on_nothing_available)
		self.th_c.start()

	def set_configs(self, configs, user):
		self.th_c.set_configs( configs, user )
		self.th_n.set_configs( configs, user )

	def start_timers(self):
		"""
		Main function for start operations
		"""		
		self.getTmr.start(5000)
		self.newsTmr.start(10000)