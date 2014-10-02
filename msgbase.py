#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sqlite3
from paths import AppPath
from datetime import datetime


class MessageBase():
    def __init__(self):
        self.app_path = AppPath().main()

    def save_message(self, user, message, incoming):
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
                                 "','", time, "','", message, ")")))
            con.commit()
        else:
            cur.execute("".join(("INSERT INTO outgoing(ToUser, date, time, text) VALUES ('", user, "','", date,
                                 "','", time, "','", message, ")")))
            con.commit()
        con.close()

    def load_message_list(self, incoming):
        msg_list = []
        if not os.path.exists("".join((AppPath(), "msgbase.db"))):
            return

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
        msg_list = []
        con = sqlite3.connect("".join((self.app_path, 'msgbase.db')))
        cur = con.cursor()

        msg_string_list = msg_string.split(' ')

        if incoming:
            cur.execute("".join(("SELECT text FROM incoming WHERE date='", msg_string_list[0], "' and time='",
                                 msg_string_list[1], "' and FromUser='", msg_string_list[2], "' LIMIT 1")))
            m_lst = cur.fetchall()
            for m in m_lst:
                msg = {}
                msg["date"] = msg_string_list[0]
                msg["time"] = msg_string_list[1]
                msg["from"] = msg_string_list[2]
                msg["text"] = m[0]
                msg_list.append(msg)

            con.close()
            return msg_list
        else:
            cur.execute("".join(("SELECT text FROM outgoing WHERE date='", msg_string_list[0], "' and time='",
                                 msg_string_list[1], "' and ToUser='", msg_string_list[2], "' LIMIT 1")))
            m_lst = cur.fetchall()
            for m in m_lst:
                msg = {}
                msg["date"] = msg_string_list[0]
                msg["time"] = msg_string_list[1]
                msg["to"] = msg_string_list[2]
                msg["text"] = m[0]
                msg_list.append(msg)
            con.close()
            return msg_list