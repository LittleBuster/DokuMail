from compress import *
from crypt import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from mariadb import MariaDB
from tcpclient import TcpClient


def send_msg(wnd, msg, all, lUsrPwd, usr):
	answ = str("")
	toUser = str("")
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
		toUsersStr = str("")
		for usr in toUsers:
			toUsersStr = toUsersStr + usr + "*"

	answ = client.send_message(toUsersStr, msg)
	client.close()

	if answ == "[FAIL]":
		QtWidgets.QMessageBox.critical(wnd, 'Ошибка', 'Ошибка передачи сообщения!', QtWidgets.QMessageBox.Yes)
		client.close()
		return

	if answ == "[FAIL-ACCESS]":
		QtWidgets.QMessageBox.critical(wnd, 'Ошибка', 'У Вас нет прав на отправку всем пользователям!', QtWidgets.QMessageBox.Yes)
		client.close()
		return

	if answ == "[SEND-MSG-OK]":
		if not all:
			QtWidgets.QMessageBox.information(wnd, 'Complete', 'Сообщение отправлено!', QtWidgets.QMessageBox.Yes)
		else:
			QtWidgets.QMessageBox.information(wnd, 'Complete', 'Сообщение отправлено всем пользователям!', QtWidgets.QMessageBox.Yes)


class SendFilesThread(QtCore.QThread):
	startUpload = pyqtSignal(str)
	connectToServer = pyqtSignal()

	def __init__(self):
		super(SendFilesThread, self).__init__()

	def send(self, TCPServer, TCPPort, flist):
		client = TcpClient()
		if not client.connect(TCPServer, TCPPort, "user25", lUsrPwd):
			QtWidgets.QMessageBox.critical(wnd, "Ошибка", "Ошибка соединения с сервером!", QtWidgets.QMessageBox.Yes)
			return

		client.begin_send_files()



		#for fname in flist:
		#	self.startUpload.emit(fname)



		client.close()

	def run(self):

class SendFiles(QtCore.QObject):
	self. sth = SendFilesThread()

	def send(self, flist):
		self.sth.send(flist)
		self.sth.start()

	def on_start(self):
