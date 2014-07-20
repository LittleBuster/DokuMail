#!/usr/bin/python
# -*- coding: utf-8 -*-

from compress import *
from crypt import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from upload import UploadWindow
from mariadb import MariaDB
from tcpclient import TcpClient


def send_msg(wnd, msg, all, lUsrPwd, usr):
	answ = str("")
	toUser = str("")
	toUsersStr = str("")
	toUsers = None

	if msg == str(""):
		QtWidgets.QMessageBox.warning(wnd, 'Complete', 'Введите сообщение!', QtWidgets.QMessageBox.Yes)
		return

	if (usr == str("") and (not all)):
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

	def __init__(self):
		super(SendFilesThread, self).__init__()		

	def send(self, wnd, TCPServer, TCPPort, flist, toUsr):
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

		print("start send")
		self.client.begin_send_files(toUser)		

		for sfile in self.fileList:			
			lsf = sfile.split("/")
			l = len(lsf)
			fname = lsf[l-1]

			self.compressStart.emit(fname)
			if not zlib_compress_file(sfile, "sendfiles/" + fname + ".z"):
				print("error compressing")

			self.cryptStart.emit(fname)
			if not AES256_encode_file("sendfiles/" + fname + ".z", "sendfiles/" + fname + ".bin", "transf.crt"):
				print("error crypting")

			self.sendStart.emit(fname)
			self.client.send_file( "sendfiles/" + fname )
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
		self.sth.err.connect(self.on_error)

		self.uploadWnd = UploadWindow()

	def on_connection_start(self):
		self.uploadWnd.pB.setValue(0)
		self.uploadWnd.show()
		self.uploadWnd.lbAct.setText("<html><head/><body><p><span style=' color:#00d4ff;'>Соединение...</span></p></body></html>")
		self.uploadWnd.lbFile.setText("")

	def on_compress_start(self, filename):
		self.uploadWnd.lbAct.setText("<html><head/><body><p><span style=' color:#00d4ff;'>Сжатие:</span></p></body></html>")
		self.uploadWnd.lbFile.setText("<html><head/><body><p><span style=' color:#ffffff;'>" + filename + "</span></p></body></html>")
		self.uploadWnd.pB.setValue(0)

	def on_crypt_start(self, filename):
		self.uploadWnd.lbAct.setText("<html><head/><body><p><span style=' color:#00d4ff;'>Шифрование:</span></p></body></html>")
		self.uploadWnd.pB.setValue(33)

	def on_send_start(self, filename):
		self.uploadWnd.lbAct.setText("<html><head/><body><p><span style=' color:#00d4ff;'>Отправка:</span></p></body></html>")
		self.uploadWnd.pB.setValue(66)

	def on_send_complete(self):
		self.uploadWnd.lbAct.setText("<html><head/><body><p><span style=' color:#00d4ff;'>Готово.</span></p></body></html>")
		self.uploadWnd.lbFile.setText("")
		self.uploadWnd.pB.setValue(100)
		QtWidgets.QMessageBox.information(self._wnd, "Complete", "Файлы отправлены!", QtWidgets.QMessageBox.Yes)
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