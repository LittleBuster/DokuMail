import os
import sys
import hashlib
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
		tr = SystemTrayIcon(self)
		tr.show()
		
		self.pbSendMsg.clicked.connect(self.on_send_msg)

	def init_app(self):
		mdb = MariaDB()
		if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "USDE"):
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
		if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "USDE"):
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtWidgets.QMessageBox.Yes)
			return
		to_user = mdb.get_user_by_alias( self.lbAlias.text() )
		mdb.close()

		h = hashlib.sha512()
		h.update(self.passwd.encode('utf-8'))
		h_passwd = h.hexdigest().upper()

		client = TcpClient()
		if not client.connect(self.TCPServer, self.TCPPort, self.user, h_passwd):
			QtWidgets.QMessageBox.critical(self, "ERR", "ERR TCP CONNECTION", QtWidgets.QMessageBox.Yes)
			return
		if not client.send_message(to_user + "*", self.teMsg.document().toPlainText()):
			QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка передачи сообщения', QtWidgets.QMessageBox.Yes)
		else:
			QtWidgets.QMessageBox.information(self, 'Complete', 'Сообщение отправлено!', QtWidgets.QMessageBox.Yes)
		client.close()

	def minimize_app(self):
		self.hide()
