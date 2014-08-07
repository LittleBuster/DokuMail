#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from mariadb import MariaDB
from tcpclient import TcpClient
from download import DownloadWnd
from msg import MsgWnd


class TcpConfig():
	__tcpServer = str
	__tcpPort = int
	__user = str
	__passwd = str

	def setTcpServer(self, server):
		self.__tcpServer = server

	def getTcpServer(self):
		return self.__tcpServer

	def setTcpPort(self, port):
		self.__tcpPort = port

	def getTcpPort(self):
		return self.__tcpPort

	def setUser(self, user):
		self.__user = user

	def getUser(self):
		return self.__user

	def setPasswd(self, passwd):
		self.__passwd = passwd

	def getPasswd(self):
		return self.__passwd

	TCPServer = property(getTcpServer, setTcpServer)
	TCPPort = property(getTcpPort, setTcpPort)
	user = property(getUser, setUser)
	passwd = property(getPasswd, setPasswd)


class RecieveThread(QtCore.QThread, TcpConfig):
	err = QtCore.pyqtSignal(str)
	downloadStart = QtCore.pyqtSignal(str)
	decryptStart = QtCore.pyqtSignal()
	decompressStart = QtCore.pyqtSignal()
	downloadComplete = QtCore.pyqtSignal()
	fileDownloaded = QtCore.pyqtSignal()
	fileCount = QtCore.pyqtSignal(int)

	update = False

	def __init__(self):
		super(RecieveThread, self).__init__()
		self.client = TcpClient()
		self.client.downloadStart.connect(self.on_download_start)
		self.client.decryptStart.connect(self.on_decrypt_start)
		self.client.decompressStart.connect(self.on_decompress_start)
		self.client.downloadComplete.connect(self.on_download_complete)
		self.client.fileDownloaded.connect(self.on_file_downloaded)
		self.client.fileCount.connect(self.on_file_count)

	def set_configs(self, tcpserver, tcpport, usr, pwd, update):
		self.TCPServer = tcpserver
		self.TCPPort = tcpport
		self.user = usr
		self.passwd = pwd
		self.update = update

	def on_file_downloaded(self):
		self.fileDownloaded.emit()

	def on_download_start(self, fname):
		self.downloadStart.emit(fname)

	def on_decrypt_start(self):
		self.decryptStart.emit()

	def on_decompress_start(self):
		self.decompressStart.emit()

	def on_download_complete(self):
		self.downloadComplete.emit()

	def on_file_count(self, cnt):
		self.fileCount.emit(cnt)

	def run(self):		
		if self.client.connect(self.TCPServer, self.TCPPort, self.user, self.passwd):
			self.client.get_files(self.update)
			self.client.close()


class Recieve(QtCore.QObject):
	downloadComplete = QtCore.pyqtSignal(bool)

	def __init__(self):
		super(Recieve, self).__init__()
		self.dldWnd = DownloadWnd()
		self.recieveTh = RecieveThread()
		self.recieveTh.downloadStart.connect(self.on_download_start)
		self.recieveTh.decryptStart.connect(self.on_decrypt_start)
		self.recieveTh.decompressStart.connect(self.on_decompress_start)
		self.recieveTh.err.connect(self.on_err)
		self.recieveTh.downloadComplete.connect(self.on_download_complete)
		self.recieveTh.fileDownloaded.connect(self.on_file_downloaded)
		self.recieveTh.fileCount.connect(self.on_file_count)
		self.step = 0
		self.update = False
		self.fname = str("")

	def set_configs(self, tcpserver, tcpport, usr, pwd, update):
		self.update = update
		self.recieveTh.set_configs(tcpserver, tcpport, usr, pwd, update)
		if not self.update:
			self.dldWnd.ui.pb2.setValue(0)

	def on_download_start(self, fname):
		self.fname = fname
		if not self.update:
			self.dldWnd.ui.pb1.setValue(0)		
			self.dldWnd.ui.lbFile.setText( "<html><head/><body><p><span style='color:#00ffd5;'>" + "Загрузка: " + fname + "</span></p></body></html>" )

	def on_decrypt_start(self):
		if not self.update:
			self.dldWnd.ui.pb1.setValue(33)
			self.dldWnd.ui.lbFile.setText( "<html><head/><body><p><span style='color:#00ffd5;'>" + "Дешифрование: " + self.fname + "</span></p></body></html>" )

	def on_decompress_start(self):
		if not self.update:
			self.dldWnd.ui.lbFile.setText( "<html><head/><body><p><span style='color:#00ffd5;'>" + "Распаковка: " + self.fname + "</span></p></body></html>" )
			self.dldWnd.ui.pb1.setValue(66)

	def on_file_downloaded(self):
		if not self.update:
			self.dldWnd.ui.lbFile.setText( "<html><head/><body><p><span style='color:#00ffd5;'>Готово.</span></p></body></html>" )

			item = QtWidgets.QListWidgetItem()
			item.setIcon(QtGui.QIcon("images/filenew_8842.ico"))
			item.setText(self.fname)

			self.dldWnd.ui.lwFiles.insertItem(0, item)
			self.dldWnd.ui.pb1.setValue(100)
			self.dldWnd.ui.pb2.setValue( self.dldWnd.ui.pb2.value() + self.step )

	def on_file_count(self, cnt):
		self.step = round(100 / cnt)

	def on_err(self, text):
		QtWidgets.QMessageBox.critical(self.dldWnd, 'Complete', text, QtWidgets.QMessageBox.Yes)

	def on_download_complete(self):
		if not self.update:
			self.dldWnd.ui.pb2.setValue(100)
			QtWidgets.QMessageBox.information(self.dldWnd, 'Complete', 'Приняты новые файлы!', QtWidgets.QMessageBox.Yes)
		self.downloadComplete.emit(self.update)

	def start(self):
		if not self.update:
			self.dldWnd.show()
		self.recieveTh.start()


class RecieveMsgThread(QtCore.QThread, TcpConfig):
	msgRecieved = QtCore.pyqtSignal([str, str, str])
	msgNone = QtCore.pyqtSignal()

	def __init__(self):
		super(RecieveMsgThread, self).__init__()
		self.client = TcpClient()

	def set_configs(self, tcpserver, tcpport, usr, pwd):
		self.TCPServer = tcpserver
		self.TCPPort = tcpport
		self.user = usr
		self.passwd = pwd

	def run(self):
		if self.client.connect(self.TCPServer, self.TCPPort, self.user, self.passwd):
			msg = self.client.get_messages()
			if msg == "[EMPTY-MSG]":
				self.client.close()
				self.msgNone.emit()
			else:
				self.msgRecieved.emit(msg["FromUser"], msg["Time"], msg["Data"])
				self.client.close()


class RecieveMsg(QtCore.QObject):
	msgComplete = QtCore.pyqtSignal()

	def __init__(self):
		super(RecieveMsg, self).__init__()
		self.msgWnd = MsgWnd()
		self.rt = RecieveMsgThread()
		self.rt.msgRecieved.connect(self.show_msg)
		self.rt.msgNone.connect(self.msg_empty)

	def show_msg(self, fromUser, timeMsg, Data):
		self.msgWnd.ui.lbFrom.setText("<html><head/><body><p><span style='color:#ffffff;'>" + fromUser + "</span></p></body></html>")
		self.msgWnd.ui.lbTime.setText("<html><head/><body><p><span style='color:#ffffff;'>" + timeMsg + "</span></p></body></html>")
		self.msgWnd.ui.teMsg.setPlainText(Data)
		self.msgWnd.show()
		self.msgComplete.emit()

	def msg_empty(self):
		self.msgComplete.emit()

	def get_msg_status(self):
		if self.msgWnd.isVisible():
			return True
		else:
			return False

	def set_configs(self, tcpserver, tcpport, usr, pwd):
		self.rt.set_configs(tcpserver, tcpport, usr, pwd)

	def start(self):
		self.rt.start()