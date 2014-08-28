import os
import sys
import json
import socket
import threading
import datetime
from mariadb import MariaDB
import multiprocessing as mp


class pObj(object):
	"""
	JSON class for configs
	"""
	pass

class ServerThread():
	def __init__(self, _sock, _addr):
		super(ServerThread, self).__init__()
		self.conn = _sock
		self.addr = _addr
		
		try:
			self.run()
		except:
			print("Client: " + str(_addr[0]) + " has crashed.")
			return

	def run(self):
		cmd = self.conn.recv(1024)

		if cmd == b"[LOGIN]":
			self.conn.send(b'ok')
			data = self.conn.recv(1024).decode('utf-8')

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
			self.conn.send(b'[LOGIN-OK]')
			print("Client " + self.usr + " authorized.")
			

			"""
			Reciveing files
			"""
			lfiles = str("")

			now_date = datetime.date.today()
			now_time = datetime.datetime.now()
			msg_name = str(now_date.year) + str(now_date.month) + str(now_date.day) + str(now_time.hour) + str(now_time.minute) + str(now_time.second)
		
			now_time_str = str(now_time).split(" ")[1].split(".")[0]

			data = self.conn.recv(1024).decode('utf-8')

			if data == '[GET-MSG]':
				print("Getting message")
				msgInfo = mdb.get_msg_info(self.usr)
				if msgInfo == None:
					mdb.change_state(self.usr, "isMsg", 0)
					print("No new messages")
					self.conn.send(b"[EMPTY-MSG]")
					self.conn.close()
					print("Client " + self.usr + " disconnected.")
					return

				idMsg = msgInfo.split("$")[0]
				fromMsg = msgInfo.split("$")[1]
				timeMsg = msgInfo.split("$")[2]
			
				self.conn.send( ( mdb.get_alias_by_user(fromMsg) + "$" + timeMsg).encode("utf-8") )
				self.conn.recv(1024)
				
				f = open("data/" + self.usr + "/" + idMsg + ".bin", "rb")
				self.conn.send( f.read() )
				f.close()
				mdb.delete_message(self.usr, fromMsg, idMsg)
			 
			"""
			Reciveing files
			"""

			if data.split("$")[0] == '[GET-FILES]':
				isUpdate = False

				if data.split("$")[1] == '[UPDATE]':
					isUpdate = True
				elif data.split("$")[1] == '[DOWNLOAD]':
					isUpdate = False

				files = []

				if not isUpdate:
					files = mdb.get_file_list(self.usr)
				else:
					files = mdb.get_update_list()

				if files == '':
					self.sock.send("[NOT-FILES]")
					return

				self.conn.send( str(len(files)).encode("utf-8") )
				self.conn.recv(1024)

				dest = str

				if not isUpdate:
					print("Sending files... " + str(len(files)))
				else:
					print("Start Update...")

				for sfile in files:
					self.conn.send(("sf$" + sfile).encode("utf-8"))
					print(self.conn.recv(1024))
					print("Sending " + sfile)

					if not isUpdate:
						dest = "data/" + self.usr + "/files/" + sfile + ".bin"							
					else:
						dest = "data/update/" + sfile

					f = open(dest, "rb")

					while True:
						data = f.read(4096)
						if len(data) != 0:
							self.conn.send(data)
						else:
							break;
					f.close()
					self.conn.send(b"[end]")					
					if not isUpdate:
						path = str
						mdb.delete_file(self.usr, sfile)
						os.remove( "data/" + self.usr + "/files/" + sfile + ".bin" )
					print(self.conn.recv(1024).decode('utf-8'))

				print("All files sended.")
				self.conn.send(b"[END-RETRIEVE]")
				if not isUpdate:
					mdb.change_state(self.usr, "isFiles", 0)
				else:
					mdb.change_state(self.usr, "isUpdate", 0)
				return

			"""
			Send messages
			"""

			if data.split("$")[0] == '[MSG-SEND]':
				toUsers = data.split("$")[1].split("*")
				if (len(toUsers) > 2) and (not mdb.check_user_admin(self.usr)):
					self.conn.send(b"[FAIL-ACCESS]")
					print("User does not have privileges! Disconnected.")
					self.conn.close()
					return

				self.conn.send(b"ok")
				msg = self.conn.recv(4096)	

				msg_name = str(now_date.year) + str(now_date.month) + str(now_date.day) + str(now_time.hour) + str(now_time.minute) + str(now_time.second)
				for toUsr in toUsers:
					if toUsr == "":
						break

					if not os.path.exists("data/" + toUsr):
						os.makedirs("data/" + toUsr)

					fname = str
					msgFile = open( "data/" + toUsr + "/" + msg_name + ".bin", 'wb')
					msgFile.write(msg)
					msgFile.close()
					mdb.add_file(msg_name, 'msg', self.usr, toUsr, str(now_date), now_time_str)
					mdb.log(self.usr, "Отправил сообщение " + toUsr, str(now_date), now_time_str)
					print("message from " + self.usr + " to " + toUsr + " saved.")
					mdb.change_state(toUsr, "isMsg", 1)
				self.conn.send(b"[SEND-MSG-OK]")


			"""
			Send files
			"""

			if (data.split("$")[0] == "[SEND-FILES]"):
				self.conn.send(b'ok')
				toUsr = data.split("$")[1]

				while True:
					data = self.conn.recv(1024)				

					if data == b"[END-RETRIEVE]":
						mdb.log(self.usr, "Отправил файлы (" + lfiles + ") - "  + toUsr, str(now_date), now_time_str)
						mdb.change_state(toUsr, "isFiles", 1)
						print("All files recieved")
						break

					if not os.path.exists( "data/" + toUsr + "/files/" ):
						print("create subdir")
						path = ""
						os.makedirs( "data/" + toUsr + "/files/" )

					print("Start downloading...")
					self.conn.send(b'recieveing...')

					fname = data.decode('utf-8').split("$")[1]
					print("New file: " + fname)

					index = 0
					newfn = fname
					while True:
						if not os.path.exists( "data/" + toUsr + "/files/" + newfn + ".bin" ):
							fname = newfn
							break
						else:
							newfn = fname
							index += 1
							fn = fname.split(".")
							nm = fn[0] + "(" + str(index) + ")"
							fe = fn[1]

							newfn = nm + "." + fe

					f = open( "data/" + toUsr + "/files/" + fname + ".bin", "wb")
					while True:
						data = self.conn.recv(4096)
						l = len(data) - 5

						try:
							if data[l:] == b'[end]':
								print("Download complete")
								f.write( data[:l] )
								f.close()
								lfiles = lfiles + fname + ","
								mdb.add_file(fname, "file", self.usr, toUsr, str(now_date), now_time_str)
								self.conn.send("complete".encode('utf-8'))
								break
						except:
							print('except')			
	
						f.write(data)
			print("Client " + self.usr + " disconnected")
			mdb.close()
		self.conn.close()


class MainThread(threading.Thread):
	cfg = {}
	def __init__(self):
		super(MainThread, self).__init__()

	def set_configs(self, config):
		self.cfg = config

	def run(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		try:
			s.bind((self.cfg["ip"], int(self.cfg["port"])))
			s.listen(int(self.cfg["clients"]))	
		except:
			print("Error of binding ip address")
			return

		print(
		"""
		#############################################################################
		#									    #
		#			 Doku Mail Server Started			    #
		#									    #
		#############################################################################
		
		""")

		while True:
			conn, addr = s.accept()
			proc = mp.Process(target=ServerThread, args=(conn, addr))
			proc.start()


def main():
	config = {}
	try:
		f = open("config.dat", "r")
		config = json.load(f)
		f.close()
	except:
		print("Error of reading config file")
		return

	"""
	Start server listener
	"""
	main_thread = MainThread()
	main_thread.set_configs( config )
	main_thread.setDaemon( True )

	while True:
		cmd = input("DokuServer> ")

		if cmd == "start":
			print("starting server...")
			main_thread.start()

		if cmd == "exit" or cmd == "quit" or cmd == "q":
			break

	print("Goodbye!")
	sys.exit()

if __name__ == '__main__':
	main()
