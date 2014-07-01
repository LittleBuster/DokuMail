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
		self.tr = SystemTrayIcon(self)
		self.tr.show()
		
		self.pbSendMsg.clicked.connect(self.on_send_msg)
		self.pbSendAllMsg.clicked.connect(self.on_sendall_msg)
		self.lwUsers.itemClicked.connect(self.lwusers_item_clicked)
		self.pbClearMsg.clicked.connect(self.on_clear_msg_clicked)
		self.pbSendFiles.clicked.connect(self.on_sendfiles_clicked)
		self.pbAddFile.clicked.connect(self.on_add_file)
		self.pbClearFiles.clicked.connect(self.on_clear_files)

		self.send_files = SendFiles()

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
		for i in range(items):
				flist.append(self.lwFiles.item(i).text())

		send_files.send(flist)

	def minimize_app(self):
		self.hide()

	def on_clear_files(self):
		self.lwFiles.clear()

	def on_add_file(self):
		filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'C:/')

		""" 
		Checking on exist file in lists
		"""
		items = self.lwFiles.count()

		if items > 0:
			for i in range(items):
				fname = self.lwFiles.item(i).text()
				if fname == filename[0]:
					QtWidgets.QMessageBox.warning(self, 'Error', 'Этот файл уже добавлен в очередь передачи', QtWidgets.QMessageBox.Yes)
					return

		""" 
		If file don't exists then add in list
		"""
		if not filename[0] == "":
			item = QtWidgets.QListWidgetItem()
			item.setIcon(QtGui.QIcon("images/filenew_8842.ico"))
			item.setText(filename[0])
			self.lwFiles.insertItem(0, item)