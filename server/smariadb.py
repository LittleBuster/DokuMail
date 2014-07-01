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

	def check_login(self, login, h_passwd):
		cur = self.conn.cursor()
		cur.execute("SELECT password FROM users WHERE name='" + login + "' LIMIT 1")

		for row in cur:
			if row[0] == h_passwd:
				return True
		return False

	def check_user_admin(self, user):
		cur = self.conn.cursor()
		cur.execute("SELECT priv FROM users WHERE name='" + user + "'")

		for row in cur:
			if row[0] == "user":
				return False
			else:
				return True

	def add_msg(self, idMsg, fromUsr, toUsr, date, time):
		cur = self.conn.cursor()
		
		cur.execute("INSERT INTO data(name, type, fromUsr, toUsr, date, time) VALUES ('" + idMsg + "', 'msg', '" + fromUsr + "','" + toUsr + "','" + date + "','" + time  + "')")
		self.conn.commit()
	
	def change_state(self, user, state, param):
		cur = self.conn.cursor()
		cur.execute("UPDATE actions SET " + state + "='"+ str(param) +"' WHERE name='" + user + "'")
		self.conn.commit()
	
	def log(self, name, message, date, time):
		cur = self.conn.cursor()
		cur.execute("INSERT INTO log(name, message, date, time) VALUES ('" + name + "','" + message + "','" + date + "','" + time + "')")
		self.conn.commit()

	def close(self):
		self.conn.close()
