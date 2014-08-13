#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtGui
from tcpclient import TcpClient
from mariadb import MariaDB
import sqlite3
from logger import Log


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
	addInNews = QtCore.pyqtSignal([str, str])
	setNewsCount = QtCore.pyqtSignal(int)
	clearNews = QtCore.pyqtSignal()
	checkNewsComplete = QtCore.pyqtSignal()

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
					n_list = cur.fetchall()
					if len(n_list) == 0:
						cur.execute("INSERT INTO news(title, date) VALUES('" + news["title"] + "', '" + news["date"] + "')")
						con.commit()

						"""
						Show tooltip
						"""
						if not mdb.is_admin(self.user):
							self.showNewsBaloon.emit(news["date"], news["title"])

					self.addInNews.emit(news["date"], news["title"])

			mdb.close()
			con.close()
			self.checkNewsComplete.emit()
			self.exit(0)

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
			return

class DeleteNewsThread(QtCore.QThread):
	deleteComplete = QtCore.pyqtSignal()
	err = QtCore.pyqtSignal(str)
	news = {}
	configs = {}

	def __init__(self):
		super(DeleteNewsThread, self).__init__()

	def set_news(self, news):
		self.news = news

	def set_configs(self, configs):
		self.configs = configs

	def run(self):
		mdb = MariaDB()
		if not mdb.connect(self.configs["MDBServer"], self.configs["MDBUser"], self.configs["MDBPasswd"], "DokuMail"):
			self.err.emit("Ошибка соединения с Базой Данных!", self.task)
			return
		if not mdb.is_admin( self.news["user"] ):
			self.err.emit("Нет прав на удаление новости!")
			mdb.close()
			return
		else:
			mdb.delete_news( self.news )
		mdb.close()

		con = sqlite3.connect('news.db')
		cur = con.cursor()
		cur.execute("DELETE FROM news WHERE title='" + self.news["header"] + "' and date='" + self.news["date"] + "'")
		con.commit()
		con.close()

		self.deleteComplete.emit()

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
		self.del_news = DeleteNewsThread()

		self.th_n.err.connect(self.on_error)
		self.th_n.showNewsBaloon.connect(self.on_show_baloon)
		self.th_n.addInNews.connect(self.on_add_innews)
		self.th_n.setNewsCount.connect(self.on_set_newscount)
		self.th_n.clearNews.connect(self.on_clear_news)
		self.th_n.checkNewsComplete.connect(self.on_check_news_complete)

		self.th_c.err.connect(self.on_error)
		self.th_c.serverOnline.connect(self.on_online_server)
		self.th_c.serverOffline.connect(self.on_offline_server)
		self.th_c.updateAvailable.connect(self.on_update_available)
		self.th_c.filesAvailable.connect(self.on_files_available)
		self.th_c.msgAvailable.connect(self.on_msg_available)
		self.th_c.nothingAvailable.connect(self.on_nothing_available)

		self.del_news.deleteComplete.connect(self.on_delete_news_complete)
		self.del_news.err.connect(self.on_delnews_error)

	"""
	Checker thread signals
	"""
	def on_show_baloon(self, date, title):
		rect = self.mainWnd.newsBaloon.geometry()
		rect.setY(0)
		self.mainWnd.newsBaloon.setGeometry(rect)
		self.mainWnd.newsBaloon.ui.leTitle.setText("[" + date + "]" + title)
		self.mainWnd.newsBaloon.show()

	def on_add_innews(self, date, title):
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
		self.mainWnd.recieveMsg.set_configs(self.mainWnd.TCPServer, self.mainWnd.TCPPort, self.mainWnd.user, self.mainWnd.passwd)	
		self.mainWnd.recieveMsg.start()

	def on_nothing_available(self):
		self.getTmr.start(5000)

	def on_set_newscount(self, count):
		self.mainWnd.news_count = count

	def on_clear_news(self):
		self.mainWnd.ui.lwNews.clear()

	def on_check_news_complete(self):
		self.newsTmr.start(10000)

	"""
	Delete news in other thread
	"""
	def on_delete_news(self):
		news = {}
		news["header"] = self.mainWnd.newsCurWnd.ui.leTitle.text()
		news["date"] = self.mainWnd.newsCurWnd.ui.lbTime.text().split(">")[5].split("<")[0]
		news["user"] = self.mainWnd.user

		self.newsTmr.stop()
		self.del_news.set_news( news )
		self.del_news.start()

	def on_delete_news_complete(self):
		self.newsTmr.start(1)
		self.mainWnd.newsCurWnd.hide()
		QtWidgets.QMessageBox.information(self.mainWnd, 'Complete', 'Новость успешно удалена!', QtWidgets.QMessageBox.Yes)

	def on_delnews_error(self, text):
		Log().local("News delete:" + text)
		QtWidgets.QMessageBox.critical(self, 'Ошибка', text, QtWidgets.QMessageBox.Yes)
		self.newsTmr.start(10000)

	"""
	Timer's signals
	"""

	def check_news(self):
		"""
		Start checking news
		"""
		self.newsTmr.stop()
		self.th_n.task = "news"
		self.th_n.news_count = self.mainWnd.news_count		
		self.th_n.start()

	def check_msg_and_files(self):
		"""
		Start checking files on server
		"""
		self.getTmr.stop()
		
		self.th_c.task = "msg_and_files"
		self.th_c.msg_status = self.mainWnd.recieveMsg.get_msg_status()		
		self.th_c.start()

	def set_configs(self, configs, user):
		self.th_c.set_configs( configs, user )
		self.th_n.set_configs( configs, user )
		self.del_news.set_configs( configs )

	def start_timers(self):
		"""
		Main function for start operations
		"""		
		self.getTmr.start(5000)
		self.newsTmr.start(1)

	def stop_timers(self):
		self.getTmr.stop()
		self.newsTmr.stop()