from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from mariadb import MariaDB
from tcpclient import TcpClient
from download import DownloadWnd


class RecieveThread(QtCore.QThread):
	err = QtCore.pyqtSignal(str)
	downloadStart = QtCore.pyqtSignal(str)
	decryptStart = QtCore.pyqtSignal()
	decompressStart = QtCore.pyqtSignal()
	downloadComplete = QtCore.pyqtSignal()
	fileDownloaded = QtCore.pyqtSignal()
	fileCount = QtCore.pyqtSignal(int)

	TCPServer = str("")
	TCPPort = 0
	user = str("")
	passwd = str("")
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

	def set_configs(self, tcpserver, tcpport, usr, pwd, update):
		self.update = update
		self.recieveTh.set_configs(tcpserver, tcpport, usr, pwd, update)
		if not self.update:
			self.dldWnd.ui.pb2.setValue(0)

	def on_download_start(self, fname):
		if not self.update:
			self.dldWnd.ui.pb1.setValue(0)		
			self.dldWnd.ui.lbFile.setText( fname )

	def on_decrypt_start(self):
		if not self.update:
			self.dldWnd.ui.pb1.setValue(33)

	def on_decompress_start(self):
		if not self.update:
			self.dldWnd.ui.pb1.setValue(66)

	def on_file_downloaded(self):
		if not self.update:
			self.dldWnd.ui.pb1.setValue(100)
			self.dldWnd.ui.pb2.setValue( self.dldWnd.ui.pb2.value() + self.step )

	def on_file_count(self, cnt):
		self.step = round(100 / cnt)

	def on_err(self, text):
		QtWidgets.QMessageBox.critical(self.dldWnd, 'Complete', text, QtWidgets.QMessageBox.Yes)

	def on_download_complete(self):
		if not self.update:
			self.dldWnd.ui.pb2.setValue(100)
			QtWidgets.QMessageBox.information(self.dldWnd, 'Complete', 'Скачивание завершено!', QtWidgets.QMessageBox.Yes)
			self.dldWnd.hide()
		self.downloadComplete.emit(self.update)

	def start(self):
		if not self.update:
			self.dldWnd.show()
		self.recieveTh.start()