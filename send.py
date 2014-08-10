#!/usr/bin/python
# -*- coding: utf-8 -*-

from compress import *
from crypt import *
import shutil
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from upload import UploadWindow
from mariadb import MariaDB
from tcpclient import TcpClient
from logger import Log


def send_msg(wnd, msg, all, lUsrPwd, usr):
	"""
	Send message to remote tcp server
	"""
	answ = str
	toUser = str
	toUsersStr = str
	toUsers = list

	if msg == "":
		QtWidgets.QMessageBox.warning(wnd, 'Complete', 'Введите сообщение!', QtWidgets.QMessageBox.Yes)
		return

	if (usr == "") and (not all)):
		"""
		If message sending to single user and user not selected then fail
		"""
		QtWidgets.QMessageBox.warning(wnd, 'Complete', 'Выберите пользователя!', QtWidgets.QMessageBox.Yes)
		return

	mdb = MariaDB()
	if not mdb.connect(wnd.MDBServer, wnd.MDBUser, wnd.MDBPasswd, "DokuMail"):
		QtWidgets.QMessageBox.critical(wnd, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtWidgets.QMessageBox.Yes)
		return

	if not all:
		toUser = mdb.get_user_by_alias( usr )
	else:
		toUsers = mdb.get_user_list(wnd.user)
	mdb.close()

	client = TcpClient()
	if not client.connect(wnd.TCPServer, wnd.TCPPort, wnd.user, lUsrPwd):
		QtWidgets.QMessageBox.critical(wnd, "Ошибка", "Ошибка соединения с сервером!", QtWidgets.QMessageBox.Yes)
		return

	if not all:
		answ = client.send_message(toUser + "*", msg)
	else:		
		for usr in toUsers:
			toUsersStr = toUsersStr + usr + "*"
		answ = client.send_message(toUsersStr, msg)
	client.close()

	if answ == b"[FAIL]":
		QtWidgets.QMessageBox.critical(wnd, 'Ошибка', 'Ошибка передачи сообщения!', QtWidgets.QMessageBox.Yes)
		client.close()
		return

	if answ == b"[FAIL-ACCESS]":
		QtWidgets.QMessageBox.critical(wnd, 'Ошибка', 'У Вас нет прав на отправку всем пользователям!', QtWidgets.QMessageBox.Yes)
		client.close()
		return

	if answ == b"[SEND-MSG-OK]":
		if not all:
			QtWidgets.QMessageBox.information(wnd, 'Complete', 'Сообщение отправлено!', QtWidgets.QMessageBox.Yes)
		else:
			QtWidgets.QMessageBox.information(wnd, 'Complete', 'Сообщение отправлено всем пользователям!', QtWidgets.QMessageBox.Yes)


class SendFilesThread(QtCore.QThread):
	connectionStart = QtCore.pyqtSignal()
	err = QtCore.pyqtSignal(str)
	compressStart = QtCore.pyqtSignal(str)
	cryptStart = QtCore.pyqtSignal(str)
	sendStart = QtCore.pyqtSignal(str)
	sendComplete = QtCore.pyqtSignal()
	sendFileComplete = QtCore.pyqtSignal()

	def __init__(self):
		super(SendFilesThread, self).__init__()		

	def send(self, wnd, TCPServer, TCPPort, flist, toUsr):
		"""
		Set connection configs
		"""
		self._wnd = wnd
		self._server = TCPServer
		self._port = TCPPort
		self.fileList = flist
		self._toUsr = toUsr

	def run(self):
		toUser = str("")
		self.client = TcpClient()

		mdb = MariaDB()
		if not mdb.connect(self._wnd.MDBServer, self._wnd.MDBUser, self._wnd.MDBPasswd, "DokuMail"):
			self.err.emit('Ошибка соединения с Базой Данных!')
			return
		toUser = mdb.get_user_by_alias( self._toUsr )	
		mdb.close()

		if not os.path.exists("sendfiles"):
			os.makedirs("sendfiles")

		self.connectionStart.emit()
		if not self.client.connect(self._server, self._port, self._wnd.user, self._wnd.passwd):
			print("fail connection")
			self.err.emit("Ошибка соединения с сервером!")
			return
		
		exts = []
		try:
			f = open("unzip_formats.cfg", "r")
			while True:
				line = f.readline().split("\n")[0]
				if line == "":
					break
				else:
					exts.append(line)
			f.close()
		except:
			Log().local("Error reading unzip formats file")

		c_exts = []
		try:
			f = open("uncrypt_formats.cfg", "r")
			while True:
				line = f.readline().split("\n")[0]
				if line == "":
					break
				else:
					c_exts.append(line)
			f.close()
		except:
			Log().local("Error reading uncrypted formats")

		print("start send")
		self.client.begin_send_files(toUser)		

		for sfile in self.fileList:			
			lsf = sfile.split("/")
			l = len(lsf)
			fname = lsf[l-1]

			"""
			Checking extension
			"""	
			isCompress = True
			isCrypt = True
			
			tmp_fname = fname.split(".")
			ext = tmp_fname[ len(tmp_fname)-1 ].lower()

			for ex in exts:
				if ex == ext:
					isCompress = False
					break

			for ex in c_exts:
				if ex == ext:
					isCrypt = False
					break

			self.compressStart.emit(fname)
			if isCompress:				
				if not zlib_compress_file(sfile, "sendfiles/" + fname + ".z"):
					Log().local("Error compressing send file: " + fname)
					print("error compressing")
			else:
				print(fname + " not compressed")
				shutil.copy2(sfile, "sendfiles/" + fname + ".z")

			if isCrypt:
				self.cryptStart.emit(fname)
				if not AES256_encode_file("sendfiles/" + fname + ".z", "sendfiles/" + fname + ".bin", "transf.crt"):
					Log().local("Error encrypting send file: " + fname)
					print("error crypting")
			else:
				print(fname + " not crypt")
				shutil.copy2("sendfiles/" + fname + ".z", "sendfiles/" + fname + ".bin")

			self.sendStart.emit(fname)
			self.client.send_file( "sendfiles/" + fname )
			self.sendFileComplete.emit()
			os.remove("sendfiles/" + fname + ".z")
			os.remove("sendfiles/" + fname + ".bin")

		self.client.end_send_files()

		self.sendComplete.emit()
		print("send complete")
		self.client.close()


class SendFiles(QtCore.QObject):
	sth = SendFilesThread()

	def __init__(self):
		super(SendFiles, self).__init__()
		self.sth.connectionStart.connect(self.on_connection_start)
		self.sth.compressStart.connect(self.on_compress_start)
		self.sth.cryptStart.connect(self.on_crypt_start)
		self.sth.sendStart.connect(self.on_send_start)
		self.sth.sendComplete.connect(self.on_send_complete)
		self.sth.sendFileComplete.connect(self.on_send_file_complete)
		self.sth.err.connect(self.on_error)

		self.uploadWnd = UploadWindow()

	def on_connection_start(self):
		self.uploadWnd.ui.pB.setValue(0)
		self.uploadWnd.show()
		self.uploadWnd.ui.lbAct.setText("<html><head/><body><p><span style=' color:#00d4ff;'>Соединение...</span></p></body></html>")
		self.uploadWnd.ui.lbFile.setText("")

	def on_compress_start(self, filename):
		self.uploadWnd.ui.lbAct.setText("<html><head/><body><p><span style=' color:#00d4ff;'>Сжатие:</span></p></body></html>")
		self.uploadWnd.ui.lbFile.setText("<html><head/><body><p><span style=' color:#ffffff;'>" + filename + "</span></p></body></html>")
		self.uploadWnd.ui.pB.setValue(0)

	def on_crypt_start(self, filename):
		self.uploadWnd.ui.lbAct.setText("<html><head/><body><p><span style=' color:#00d4ff;'>Шифрование:</span></p></body></html>")
		self.uploadWnd.ui.pB.setValue(33)

	def on_send_start(self, filename):
		self.uploadWnd.ui.lbAct.setText("<html><head/><body><p><span style=' color:#00d4ff;'>Отправка:</span></p></body></html>")
		self.uploadWnd.ui.pB.setValue(66)

	def on_send_file_complete(self):
		self.uploadWnd.ui.lbAct.setText("<html><head/><body><p><span style=' color:#00d4ff;'>Готово.</span></p></body></html>")
		self.uploadWnd.ui.lbFile.setText("")
		self.uploadWnd.ui.pB.setValue(100)

	def on_send_complete(self):
		self.uploadWnd.ui.lbAct.setText("<html><head/><body><p><span style=' color:#00d4ff;'>Готово.</span></p></body></html>")
		self.uploadWnd.ui.lbFile.setText("")
		self.uploadWnd.ui.pB.setValue(100)
		QtWidgets.QMessageBox.information(self.uploadWnd, "Complete", "Файлы отправлены!", QtWidgets.QMessageBox.Yes)
		self.uploadWnd.hide()

	def on_error(self, txt):
		QtWidgets.QMessageBox.critical(self._wnd, "Ошибка", txt, QtWidgets.QMessageBox.Yes)

	def send(self, wnd, flist, toUsr):
		if toUsr == "":
			QtWidgets.QMessageBox.warning(wnd, 'Complete', 'Выберите пользователя!', QtWidgets.QMessageBox.Yes)
			return
		self._wnd = wnd
		self.sth.send(wnd, wnd.TCPServer, wnd.TCPPort, flist, toUsr)
		self.sth.start()