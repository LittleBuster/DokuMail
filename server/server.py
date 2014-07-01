import socket
from PyQt5 import QtCore
from Crypto.Cipher import AES
import zlib
from scrypt import *
import datetime
from smariadb import MariaDB

class ServerThread(QtCore.QThread):
	def __init__(self, parent=None):
		super().__init__(parent)

	def create_thread(self, _conn, _ip):
		self.conn = _conn 
		self.ip = _ip

	def run(self):
#		try:
			print("New connection from " + str(self.ip))
			if AES256_decode_msg(self.conn.recv(128)) == "[CRED]":
				self.conn.send(b'1')
				data = AES256_decode_msg(self.conn.recv(1024))
				
				self.usr = data.split("$")[1]
				h_pwd = data.split("$")[2]

				"""
				Check user's login and password
				"""
				mdb = MariaDB()
				if not mdb.connect("172.20.0.11", "doku", "School184", "DokuMail"):
					print("Error connection to Database")
					return

				if not mdb.check_login(self.usr, h_pwd):
					print("Access denided")
					print("Client " + self.usr + " disconnected.")
					mdb.close()
					self.conn.close()
					return
				
				"""
				User authorized
				"""
	
				print("Client " + self.usr + " authorized.")
				self.conn.send(AES256_encode_msg("[CRED-OK]"))
				
				data = AES256_decode_msg( self.conn.recv(1024) )
				
				if data.split("$")[0] == "MSG-SEND":
					to_users = data.split("$")[1].split("*")

					"""
					Check user is admin?
					"""
					if (len(to_users) > 2) and (not mdb.check_user_admin(self.usr)):
						self.conn.send( AES256_encode_msg("[FAIL-ACCESS]"))
						print("User does not have privileges! Disconnected.")
						self.conn.close()
						return
					self.conn.send( AES256_encode_msg("NONE") )
					msg = self.conn.recv(2048)

					now_date = datetime.date.today()
					now_time = datetime.datetime.now()
					msg_name = str(now_date.year) + str(now_date.month) + str(now_date.day) + str(now_time.hour) + str(now_time.minute) + str(now_time.second)
					now_time = str(now_time).split(" ")[1].split(".")[0]					
					for to_usr in to_users:
						if to_usr == "":
							break

						if not os.path.exists("data/" + to_usr):
							os.makedirs("data/" + to_usr)

						msgFile = open("data/" + to_usr + "/" + msg_name + ".bin", "wb")
						msgFile.write( msg )
						msgFile.close()
						mdb.add_msg(msg_name, self.usr, to_usr, str(now_date), str(now_time))
						mdb.log(self.usr, "Отправил сообщение " + to_usr, str(now_date), str(now_time))
						print("message from " + self.usr + " to " + to_usr + " saved.")
						mdb.change_state(to_usr, "isMsg", 1)

					self.conn.send( AES256_encode_msg("[SEND-MSG-OK]") )

				mdb.close()
				print("Client " + self.usr + " disconnected")
				self.conn.close()
#		except:
#			print("Client disconnected")
				

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('172.20.0.10', 5000))
sock.listen(1)

count = 0

while True:
	conn, addr = sock.accept()
	th = ServerThread()
	th.create_thread(conn, addr)
	th.start()