import hashlib
import pymysql


class MariaDB():
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

	def get_msg_info(self, user):
		info = str("")
		cur = self.conn.cursor()
		cur.execute("SELECT name,fromUsr,time FROM data WHERE toUsr='" + user + "' and type='msg'")

		try:
			for row in cur:
				if row == None:
					return "[EMPTY-MSG]"
				info = row[0] + "$" + row[1] + "$" + row[2]
				return info
		except:
			return "[EMPTY-MSG]"

	def get_file_list(self, user):
		files = []

		cur = self.conn.cursor()
		cur.execute("SELECT name FROM data WHERE toUsr='" + user + "' and type='file'")

		for row in cur:
			files.append( row[0] )

		return files

	def get_update_list(self):
		files = []

		cur = self.conn.cursor()
		cur.execute("SELECT filename FROM updates")

		for row in cur:
			files.append( row[0] )

		return files

	def delete_file(self, user, fname):
		cur = self.conn.cursor()
		cur.execute("DELETE FROM data where name='" + fname + "' and toUsr='" + user + "'")
		self.conn.commit()
	
	def delete_message(self, toUser, fromUser, idMsg):
		cur = self.conn.cursor()
		cur.execute("DELETE FROM data where name='" + idMsg + "' and toUsr='" + toUser + "' and fromUsr='" + fromUser + "'")
		self.conn.commit()

	def add_file(self, idFile, type, fromUsr, toUsr, date, time):
		cur = self.conn.cursor()
		
		cur.execute("INSERT INTO data(name, type, fromUsr, toUsr, date, time) VALUES ('" + idFile + "','" +  type + "','" + fromUsr + "','" + toUsr + "','" + date + "','" + time  + "')")
		self.conn.commit()
	
	def change_state(self, user, state, param):
		cur = self.conn.cursor()
		cur.execute("UPDATE actions SET " + state + "='"+ str(param) +"' WHERE name='" + user + "'")
		self.conn.commit()
	
	def log(self, name, message, date, time):
		cur = self.conn.cursor()
		cur.execute("INSERT INTO log(name, message, date, time) VALUES ('" + name + "','" + message + "','" + date + "','" + time + "')")
		self.conn.commit()

	def get_alias_by_user(self, user):
		cur = self.conn.cursor()
		cur.execute("SELECT alias FROM users WHERE name='" + user + "' LIMIT 1")

		for row in cur:
			return row[0]

	def close(self):
		self.conn.close()
