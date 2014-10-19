#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sqlite3
from paths import AppPath
from datetime import datetime


class MessageBase():
    """
    Class for managing in/out messages history
    """
    def __init__(self):
        self.app_path = AppPath().main()

    def save_message(self, user, message, incoming):
        """
        Save incoming or outgoing message in local database file
        """
        con = sqlite3.connect("".join((self.app_path, 'msgbase.db')))
        cur = con.cursor()

        date = str(datetime.now().date())
        time = str(datetime.now().time()).split('.')[0]

        try:
            if incoming:
                cur.execute(
                    'CREATE TABLE incoming(id INTEGER PRIMARY KEY AUTOINCREMENT, FromUser VARCHAR(20), \
                    date VARCHAR(20), time VARCHAR(20), text TEXT)')
                con.commit()
            else:
                cur.execute(
                    'CREATE TABLE outgoing(id INTEGER PRIMARY KEY AUTOINCREMENT, ToUser VARCHAR(20), \
                    date VARCHAR(20), time VARCHAR(20), text TEXT)')
                con.commit()
        except:
            pass

        if incoming:
            cur.execute("".join(("INSERT INTO incoming(FromUser, date, time, text) VALUES ('", user, "','", date,
                                 "','", time, "','", message, "')")))
            con.commit()
        else:
            cur.execute("".join(("INSERT INTO outgoing(ToUser, date, time, text) VALUES ('", user, "','", date,
                                 "','", time, "','", message, "')")))
            con.commit()
        con.close()

    def load_message_list(self, incoming):
        """
        Load incomming/outgoing  messages list from local database file
        """
        msg_list = []
        if not os.path.exists("".join((self.app_path, "msgbase.db"))):
            return msg_list

        con = sqlite3.connect("".join((self.app_path, 'msgbase.db')))
        cur = con.cursor()
        if incoming:
            cur.execute("SELECT FromUser,date,time FROM incoming")
            m_lst = cur.fetchall()
            for m in m_lst:
                msg_list.append("".join((m[0], " ", m[1], " ", m[2])))
            con.close()
            return msg_list
        else:
            cur.execute("SELECT ToUser,date,time FROM outgoing")
            m_lst = cur.fetchall()
            for m in m_lst:
                msg_list.append("".join((m[0], " ", m[1], " ", m[2])))
            con.close()
            return msg_list

    def get_message(self, msg_string, incoming):
        """
        Load old in/out message from local database file
        """
        con = sqlite3.connect("".join((self.app_path, 'msgbase.db')))
        cur = con.cursor()

        msg_string_list = msg_string.split(' ')

        if incoming:
            cur.execute("".join(("SELECT text FROM incoming WHERE date='", msg_string_list[1], "' and time='",
                                 msg_string_list[2], "' and FromUser='", msg_string_list[0], "' LIMIT 1")))
            m_lst = cur.fetchall()
            for m in m_lst:
                msg = {}
                msg["date"] = msg_string_list[1]
                msg["time"] = msg_string_list[2]
                msg["from"] = msg_string_list[0]
                msg["text"] = m[0]
                con.close()
                return msg
        else:
            cur.execute("".join(("SELECT text FROM outgoing WHERE date='", msg_string_list[1], "' and time='",
                                 msg_string_list[2], "' and ToUser='", msg_string_list[0], "' LIMIT 1")))
            m_lst = cur.fetchall()
            for m in m_lst:
                msg = {}
                msg["date"] = msg_string_list[1]
                msg["time"] = msg_string_list[2]
                msg["to"] = msg_string_list[0]
                msg["text"] = m[0]
                con.close()
                return msg

    def clear_messages(self, incoming):
        """
        Clear in/out messages table
        """
        con = sqlite3.connect("".join((self.app_path, 'msgbase.db')))
        cur = con.cursor()

        if incoming:
            cur.execute("DROP TABLE incoming")
            con.commit()
        else:
            cur.execute("DROP TABLE outgoing")
            con.commit()
        con.close()