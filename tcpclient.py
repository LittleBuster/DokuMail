import socket
from Crypto.Cipher import AES
import zlib
from crypt import *


class TcpClient():
	def __init__(self):
		super(TcpClient, self).__init__()

	def connect(self, ip, port, user, h_pwd):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		try:
			self.sock.connect((ip, port))
		except:
			return False

		self.sock.send( AES256_encode_msg("[CRED]", "retrieve.crt") )
		self.sock.recv(5)
		
		cred = "[cred$" + user + "$" + h_pwd + "$]"
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

	def send_files(self, flist):
		for sfile in flist:
			print(sfile + " $ ")

	def close(self):
		self.sock.close()
