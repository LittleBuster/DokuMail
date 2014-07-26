#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
from Crypto.Cipher import AES
import zlib
from crypt import *
from compress import *
import hashlib
from PyQt5 import QtCore


class TcpClient(QtCore.QObject):
	downloadStart = QtCore.pyqtSignal(str)
	decryptStart = QtCore.pyqtSignal()
	decompressStart = QtCore.pyqtSignal()
	downloadComplete = QtCore.pyqtSignal()
	fileDownloaded = QtCore.pyqtSignal()
	fileCount = QtCore.pyqtSignal(int)

	def __init__(self):
		super(TcpClient, self).__init__()

	def connect(self, ip, port, user, pwd):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			self.sock.connect((ip, port))
		except:
			return False

		self.sock.send(b"[LOGIN]")
		print(self.sock.recv(1024))

		h = hashlib.sha512()
		h.update(pwd.encode('utf-8'))
		h_passwd = h.hexdigest().upper()
		
		cred = "login$" + user + "$" + h_passwd + "$"
		self.sock.send( cred.encode('utf-8') )
		
		if self.sock.recv(1024) == b'[LOGIN-OK]':
			print("Login ok")
			return True
		else:
			print("login fail")
			return False

	def send_message(self, toUsers, message):
		try:
			self.sock.send( ("MSG-SEND$" + toUsers).encode('utf-8') )
			answ = self.sock.recv(1024)
			if answ == b"[FAIL-ACCESS]":
				return answ

			self.sock.send( AES256_encode_msg( message, "transf.crt" ) )
			answ = self.sock.recv(1024)

			return answ
		except:
			return b"[FAIL]"

	def begin_send_files(self, toUser):
		self.sock.send( ("[SEND-FILES]$" + toUser).encode('utf-8') )
		print (self.sock.recv(1024))

	def send_file(self, fname):
		lsf = fname.split("/")
		l = len(lsf)

		self.sock.send( ("sf$" + lsf[l-1]).encode("utf-8") )
		print(self.sock.recv(1024).decode('utf-8'))

		f = open(fname + ".bin", "rb")

		while True:
			data = f.read(4096)
			if len(data) != 0:
				self.sock.send(data)
			else:
				break;
		f.close()
		self.sock.send(b"[end]")
		print(self.sock.recv(1024).decode('utf-8'))

	def end_send_files(self):
		self.sock.send(b"[END-RETRIEVE]")

	def get_files(self):
		self.sock.send( b'[GET-FILES]' )

		if not os.path.exists("downloads"):
			os.makedirs("downloads")

		cnt = int(self.sock.recv(1024).decode("utf-8"))
		self.sock.send(b"ok")

		self.fileCount.emit(cnt)

		while True:
			data = self.sock.recv(1024)

			if data == b'[NOT-FILES]':
				break

			if data == b"[END-RETRIEVE]":
				self.downloadComplete.emit()
				print("All files recieved")
				break			

			print("Start downloading...")
			self.sock.send(b'recieveing...')

			fname = str("")
			try:
				fname = data.decode('utf-8').split("$")[1]
			except:
				return
			print("New file: " + fname)

			self.downloadStart.emit(fname)

			f = open("downloads/" + fname + ".bin", "wb")
			while True:
				data = self.sock.recv(4096)
				l = len(data) - 5

				try:
					if data[l:] == b'[end]':
						print("Download complete")
						f.write( data[:l] )
						#mdb.add_file(fname, "file", self.usr, toUsr, str(now_date), now_time_str)
						self.sock.send("complete".encode('utf-8'))
						f.close()

						self.decryptStart.emit()

						print("Decrypt: " + fname)
						if not AES256_decode_file("downloads/" + fname + ".bin", "downloads/" + fname + ".z", "transf.crt"):
							print("error crypting")

						self.decompressStart.emit()

						print("Decompress: " + fname)
						if not zlib_decompress_file("downloads/" + fname + ".z", "downloads/" + fname):
							print("error decompressing")

						self.fileDownloaded.emit()

						os.remove("downloads/" + fname + ".bin")
						os.remove("downloads/" + fname + ".z")

						break
				except:
					print('except')			
	
				f.write(data)

	def close(self):
		self.sock.close()
