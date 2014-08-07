#!/usr/bin/python
# -*- coding: utf-8 -*-

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

	def get_alias_by_user(self, user):
		cur = self.conn.cursor()
		cur.execute("SELECT alias FROM users WHERE name='" + user + "' LIMIT 1")
		
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

	def send_news(self, user, news, title, date):
		cur = self.conn.cursor()
		try:
			cur.execute("INSERT INTO news(name,news,title,date) VALUES ('" + user + "', '" + news + "', '" + title + "', '" + date + "')")
			self.conn.commit()
			return True
		except:
			return False

	def get_news(self, title):
		news = {}
		cur = self.conn.cursor()
		cur.execute("SELECT name,news,title,date FROM news WHERE title='" + title + "'")

		for row in cur:
			news["user"] = row[0]
			news["news"] = row[1]
			news["title"] = row[2]
			news["date"] = row[3]
			return news

	def check_news(self):
		news_list = list()
		cur = self.conn.cursor()
		cur.execute("SELECT title,date FROM news")

		for row in cur:
			news = {}
			news["title"] = row[0]
			news["date"] = row[1]
			news_list.append( news )
		return news_list

	def check_files(self, curUser):
		cur = self.conn.cursor()
		cur.execute("SELECT isFiles FROM actions WHERE name='" + curUser + "' LIMIT 1" )

		for row in cur:
			if int(row[0]) == 1:
				return True
			else:
				return False

	def check_update(self, curUser):
		cur = self.conn.cursor()
		cur.execute("SELECT isUpdate FROM actions WHERE name='" + curUser + "' LIMIT 1" )

		for row in cur:
			if int(row[0]) == 1:
				return True
			else:
				return False

	def check_messages(self, curUser):
		cur = self.conn.cursor()
		cur.execute("SELECT isMsg FROM actions WHERE name='" + curUser + "' LIMIT 1" )

		for row in cur:
			if int(row[0]) == 1:
				return True
			else:
				return False

	def get_alias_list(self):
		usrlist = list()

		cur = self.conn.cursor()
		cur.execute("SELECT alias FROM users WHERE enable='1'")

		for row in cur:	
			usrlist.append(row[0])

		return usrlist

	def create_task(self, name, task, typeTask, date, diff, status):
		cur = self.conn.cursor()
		try:
			cur.execute("INSERT INTO tasks(name,task,typeTask,dateTask,difficult,status) VALUES ('" + name + "','" + task + "','" + typeTask + "','" + str(date) + "','" + diff + "','" + status + "')")
			self.conn.commit()
			return True
		except:
			return False

	def get_task_list(self, user):
		taskList = list()

		cur = self.conn.cursor()
		cur.execute("SELECT id,typeTask,dateTask,status FROM tasks WHERE name='" + user + "'")

		for row in cur:
			task = {}
			task["id"] = str(row[0])
			task["type"] = row[1]
			task["date"] = row[2]
			task["status"] = row[3]
			taskList.append( task )

		return taskList

	def is_admin(self, user):
		cur = self.conn.cursor()
		cur.execute("SELECT priv FROM users WHERE name='" + user + "' LIMIT 1")

		for row in cur:
			if row[0] == "admin":
				return True
			else:
				return False

	def change_state(self, user, state, param):
                cur = self.conn.cursor()
                cur.execute("UPDATE actions SET " + state + "='"+ str(param) +"' WHERE name='" + user + "'")
                self.conn.commit()

	def close(self):
		self.conn.close()		