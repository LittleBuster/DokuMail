import hashlib
import pymysql
from PyQt5 import QtCore


class MariaDB(QtCore.QObject):
	conn = None

	def __init__(self):
		super(MariaDB, self).__init__()

	def connect(self, ip, usr, pwd, database):
		self.conn = None
		try:
			self.conn = pymysql.connect(host=ip, port=3306, user=usr, passwd=pwd, db=database, charset='utf8')
			return True
		except:
			return False

	def check_login(self, login, password):
		h = hashlib.sha512()
		h.update(password.encode('utf-8'))
		h_passwd = h.hexdigest().upper()

		cur = self.conn.cursor()
		cur.execute("SELECT password FROM users WHERE name='" + login + "' LIMIT 1")

		for row in cur:
			if row[0] == h_passwd:
				return True
		return False

	def get_user_by_alias(self, alias):
		cur = self.conn.cursor()
		cur.execute("SELECT name FROM users WHERE alias='" + alias + "' LIMIT 1")
		
		for row in cur:
			return row[0]

	def get_user_list(self, curUser):
		usrlist = list()
		cur = self.conn.cursor()
		cur.execute("SELECT name FROM users")

		for row in cur:
			if row[0] != curUser:
				usrlist.append(row[0])
		return usrlist

	def get_alias_list(self):
		usrlist = list()

		cur = self.conn.cursor()
		cur.execute("SELECT alias FROM users WHERE enable='1'")

		for row in cur:	
			usrlist.append(row[0])

		return usrlist		

	def close(self):
		self.conn.close()
