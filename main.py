import os
import sys
import hashlib
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
		self.tr = SystemTrayIcon(self)
		self.tr.show()
		
		self.pbSendMsg.clicked.connect(self.on_send_msg)
		self.pbSendAllMsg.clicked.connect(self.on_sendall_msg)
		self.lwUsers.itemClicked.connect(self.lwusers_item_clicked)
		self.pbClearMsg.clicked.connect(self.on_clear_msg_clicked)
		self.pbSendFiles.clicked.connect(self.on_sendfiles_clicked)

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
		print(self.TCPServer, self.TCPPort)
		mdb = MariaDB()
		if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "DokuMail"):
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtWidgets.QMessageBox.Yes)
			return
		to_user = mdb.get_user_by_alias( self.lbAlias.text() )
		mdb.close()

		h = hashlib.sha512()
		h.update(self.passwd.encode('utf-8'))
		h_passwd = h.hexdigest().upper()

		client = TcpClient()
		if not client.connect(self.TCPServer, self.TCPPort, self.user, h_passwd):
			QtWidgets.QMessageBox.critical(self, "Ошибка", "Ошибка соединения с сервером!", QtWidgets.QMessageBox.Yes)
			return
		answ = client.send_message(to_user + "*", self.teMsg.document().toPlainText())
		
		if answ == "[FAIL]":
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка передачи сообщения!', QtWidgets.QMessageBox.Yes)
			client.close()
			return

		if answ == "[SEND-MSG-OK]":
			QtWidgets.QMessageBox.information(self, 'Complete', 'Сообщение отправлено!', QtWidgets.QMessageBox.Yes)
		client.close()

	def on_sendall_msg(self):
		mdb = MariaDB()
		if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "DokuMail"):
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtWidgets.QMessageBox.Yes)
			return
		
		toUsers = mdb.get_user_list(self.user)
		mdb.close()
		toUsersStr = str("")
		
		for usr in toUsers:
			toUsersStr = toUsersStr + usr + "*"

		h = hashlib.sha512()
		h.update(self.passwd.encode('utf-8'))
		h_passwd = h.hexdigest().upper()

		client = TcpClient()
		if not client.connect(self.TCPServer, self.TCPPort, self.user, h_passwd):
			QtWidgets.QMessageBox.critical(self, "Ошибка", "Ошибка соединения с сервером!", QtWidgets.QMessageBox.Yes)
			return
		answ = client.send_message(toUsersStr, self.teMsg.document().toPlainText())
		
		if answ == "[FAIL]":
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка передачи сообщения!', QtWidgets.QMessageBox.Yes)
			client.close()
			return

		if answ == "[FAIL-ACCESS]":
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'У Вас нет прав на отправку всем пользователям!', QtWidgets.QMessageBox.Yes)
			client.close()
			return

		if answ == "[SEND-MSG-OK]":
			QtWidgets.QMessageBox.information(self, 'Complete', 'Сообщение отправлено всем пользователям!', QtWidgets.QMessageBox.Yes)
		client.close()

	def on_sendfiles_clicked(self):
		compress_file("test.jpg", "test.z")
		decompress_file("test.z", "test2.jpg")
 
	def minimize_app(self):
		self.hide()
