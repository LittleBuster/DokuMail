#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
from Crypto.Cipher import AES
import zlib
from crypt import *
import hashlib


class TcpClient():
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
		self.sock.send(b"[end]")
		print(self.sock.recv(1024).decode('utf-8'))

	def end_send_files(self):
		self.sock.send(b"[END-RETRIEVE]")

	def close(self):
		self.sock.close()