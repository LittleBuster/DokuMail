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

		self.sock.send( AES256_encode_msg("[CRED]", "retrieve.crt") )
		self.sock.recv(5)

		h = hashlib.sha512()
		h.update(pwd.encode('utf-8'))
		h_passwd = h.hexdigest().upper()
		
		cred = "[cred$" + user + "$" + h_passwd + "$]"
		self.sock.send( AES256_encode_msg(cred, "retrieve.crt") )
		
		answ = self.sock.recv(1024)
		if not AES256_decode_msg(answ, "retrieve.crt") == "[CRED-OK]":
			self.sock.close()
			return False
		return True

	def send_message(self, toUsers, message):
		try:
			self.sock.send( AES256_encode_msg( "MSG-SEND$" + toUsers, "retrieve.crt") )
			answ = AES256_decode_msg( self.sock.recv(1024), "retrieve.crt" )
			if answ == "[FAIL-ACCESS]":
				return answ

			self.sock.send( AES256_encode_msg( message, "transf.crt" ) )
			answ = AES256_decode_msg( self.sock.recv(1024), "retrieve.crt")
			return answ
		except:
			return "[FAIL]"

	def begin_send_files(self):
		self.sock.send( AES256_encode_msg("[FILES-SEND]$" + toUser, "retrieve.crt"))
		self.sock.recv(10)

	def send_file(self, fname, toUser):
		lsf = fname.split("/")
		l = len(lsf)

		self.sock.send( ("FILE$" + lsf[l-1]).encode("utf-8") )
		self.sock.recv(10)

		f = open(lsf[l-1], "rb")

		while True:
			data = f.read(1024)

			if len(data) != 0:
				self.sock.send( data )
				self.sock.recv(10)
			else:
				self.sock.send("[END-FILE]".encode("utf-8"))
				self.sock.recv(10)
				break

	def end_send_files(self):
		self.sock.send("[END-RETRIEVE]".encode("utf-8"))
		

	def close(self):
		self.sock.close()
