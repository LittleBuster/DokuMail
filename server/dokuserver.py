#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import socket
import threading
import datetime
from configs import Configs
from crypt import *
from logger import *
from mariadb import MariaDB
import multiprocessing as mp


class ServerThread():
    cfg = {}

    def __init__(self, _sock, _addr, cfg):
        super(ServerThread, self).__init__()
        self.conn = _sock
        self.addr = _addr
        self.cfg = cfg
        self.header = "DokuMail 2.0 Header - p1.0.0"
        self.r_key = AES256_cert_read("retrieve.crt")

        #try:
        self.run()
        #except:
        #    Log().local("Client: " + str(_addr[0]) + " has crashed.")
        #    return

    def run(self):
        data = str
        try:
            data = AES256_decode_msg( self.conn.recv(1024), self.r_key )
            data = json.loads(data)
        except:
            return

        if data["header"] == self.header and data["type"] == "login":
            self.usr = data["user"]
            h_pwd = data["passwd"]

            """
            Check user's login and password
            """

            mdb = MariaDB()
            if not mdb.connect(self.cfg["MariaDB"]["ip"], self.cfg["MariaDB"]["login"],
                               self.cfg["MariaDB"]["password"], self.cfg["MariaDB"]["base"]):
                Log().local("SERVER", "Error connection to Database", LOG_CRITICAL, mdb)
                return

            if not mdb.check_login(self.usr, h_pwd):
                Log().local(self.usr, "Access denided. Client disconnected.", LOG_CRITICAL, mdb)
                mdb.close()
                self.conn.close()
                return

            """
            User authorized
            """
            answ = json.dumps({"header": self.header, "answ": "login-ok"})
            self.conn.send( AES256_encode_msg(answ, self.r_key) )

            """
            Reciveing files
            """
            lfiles = str("")

            now_date = datetime.date.today()
            now_time = datetime.datetime.now()
            now_time_str = str(now_time).split(" ")[1].split(".")[0]

            data = AES256_decode_msg( self.conn.recv(1024), self.r_key )
            data = json.loads(data)

            """
            Get messages
            """

            if data["type"] == 'get-message':
                answ = {"header": self.header, "answ": ""}
                msgInfo = mdb.get_msg_info(self.usr)

                if msgInfo["type"] == "empty":
                    mdb.change_state(self.usr, "isMsg", 0)
                    answ["answ"] = "empty-msg"
                    self.conn.send(AES256_encode_msg(json.dumps(answ), self.r_key))
                    self.conn.close()
                    return

                idMsg = msgInfo["name"]
                fromMsg = msgInfo["from"]
                timeMsg = msgInfo["time"]

                answ = {"header": self.header, "answ": "msg", "From": mdb.get_alias_by_user(fromMsg), "Time": timeMsg}
                self.conn.send(AES256_encode_msg(json.dumps(answ), self.r_key))
                self.conn.recv(1024)

                f = open("".join(("data/", self.usr, "/", idMsg, ".bin")), "rb")
                self.conn.send(f.read())
                f.close()
                mdb.delete_message(self.usr, fromMsg, idMsg)
                Log().local(self.usr, "Get new message", LOG_INFO, mdb)

            """
            Reciveing files
            """

            if data["type"] == 'get-files':
                isUpdate = False

                if data["operation"] == "update":
                    isUpdate = True
                elif data["operation"] == 'download':
                    isUpdate = False

                files = []

                if not isUpdate:
                    files = mdb.get_file_list(self.usr)
                else:
                    files = mdb.get_update_list()

                if files == '':
                    answ = {"header": self.header, "type": "not-files"}
                    self.sock.send( AES256_encode_msg(json.dumps(answ), self.r_key ))
                    return

                answ = {"header": self.header, "count": len(files)}
                self.conn.send(AES256_encode_msg(json.dumps(answ), self.r_key))
                self.conn.recv(1024)

                dest = str

                if isUpdate:
                   Log().local(self.usr, "Start update", LOG_INFO, mdb)

                for sfile in files:
                    answ = {"header": self.header, "type": "sf", "filename": sfile}
                    self.conn.send(AES256_encode_msg(json.dumps(answ), self.r_key))
                    self.conn.recv(1024)
                    Log().local(self.usr, "Get file " + sfile, LOG_INFO, mdb)

                    if not isUpdate:
                        dest = "".join(("data/", self.usr, "/files/", sfile, ".bin"))
                    else:
                        dest = "data/update/" + sfile

                    f = open(dest, "rb")

                    while True:
                        data = f.read(4096)
                        if len(data) != 0:
                            self.conn.send(data)
                        else:
                            break
                    f.close()
                    self.conn.send(b"[end]")
                    if not isUpdate:
                        path = str
                        mdb.delete_file(self.usr, sfile)
                        os.remove("data/" + self.usr + "/files/" + sfile + ".bin")
                    self.conn.recv(1024).decode('utf-8')

                Log().local(self.usr, "All files downloaded.", LOG_INFO, mdb)
                answ = {"header": self.header, "type": "end-retrieve"}
                self.conn.send(AES256_encode_msg(json.dumps(answ), self.r_key))
                if not isUpdate:
                    mdb.change_state(self.usr, "isFiles", 0)
                else:
                    mdb.change_state(self.usr, "isUpdate", 0)
                self.conn.close()
                return

            """
            Send messages
            """

            if data["type"] == "send-message":
                toUsers = []
                answ = {"header": self.header, "answ": ""}

                if (data["ToUsers"] == "$ALL_USERS$") and (not mdb.check_user_admin(self.usr)):
                    answ["answ"] = "fail-access"
                    self.conn.send(json.dumps(answ).encode("utf-8"))
                    Log().local(self.usr, "User does not have privileges! Disconnected.", LOG_INFO, mdb)
                    self.conn.close()
                    return

                answ["answ"] = "ok"
                self.conn.send( AES256_encode_msg(json.dumps(answ), self.r_key))
                msg = self.conn.recv(4096)

                msg_name = "".join((str(now_date.year), str(now_date.month), str(now_date.day), str(now_time.hour),
                                    str(now_time.minute), str(now_time.second)))

                if not data["ToUsers"] == "$ALL_USERS$":
                    toUsers.append( data["ToUsers"] )
                else:
                    toUsers = mdb.get_user_list(self.usr)

                for toUsr in toUsers:
                    if not os.path.exists("data/" + toUsr):
                        os.makedirs("data/" + toUsr)

                    msgFile = open("".join(("data/", toUsr, "/", msg_name, ".bin")), 'wb')
                    msgFile.write(msg)
                    msgFile.close()
                    mdb.add_file(msg_name, 'msg', self.usr, toUsr, str(now_date), now_time_str)
                    Log().local(self.usr, "Message to " + toUsr + " sended.", LOG_INFO, mdb)
                    mdb.change_state(toUsr, "isMsg", 1)

                sz = os.path.getsize("".join(("data/", toUsr, "/", msg_name, ".bin")))
                sz = round(sz / 1024, 2)
                mdb.stat(self.usr, "msg", str(sz), now_time_str, str(now_date))
                answ["answ"] = "send-msg-ok"
                self.conn.send( AES256_encode_msg(json.dumps(answ), self.r_key) )

                """
                Upload backup message to server
                """
                if self.cfg["MediaFire"]["enable"] == True:
                    from firecloud import MediaFire
                    fire = MediaFire()
                    fire.set_config(self.cfg)
                    fire.upload_msg("".join(("data/", toUsr, "/", msg_name, ".bin")))
                return

            """
            Create/Delete news log
            """

            if data["type"] == "news":
                if data["action"] == "create":
                    Log().local(self.usr, "".join(('Create news "', data["news-header"],'"')), LOG_INFO, mdb)
                elif data["action"] == "delete":
                    Log().local(self.usr, "".join(('Delete news "', data["news-header"],'"')), LOG_INFO, mdb)
                return

            """
            Send files
            """

            if data["type"] == "send-files":
                self.conn.send(b'ok')
                toUsr = data["ToUser"]

                while True:
                    answ = AES256_decode_msg(self.conn.recv(1024), self.r_key)
                    answ = json.loads(answ)

                    if not answ["header"] == self.header:
                        return

                    if answ["type"] == "end-retrieve":
                        mdb.change_state(toUsr, "isFiles", 1)
                        break

                    if not os.path.exists("".join(("data/" + toUsr + "/files/"))):
                        os.makedirs("".join(("data/", toUsr, "/files/")))

                    self.conn.send(b'recieveing...')

                    fname = ""

                    if answ["type"] == "sf":
                        fname = answ["filename"]

                    index = 0
                    newfn = fname
                    while True:
                        if not os.path.exists("".join(("data/", toUsr, "/files/", newfn, ".bin"))):
                            fname = newfn
                            break
                        else:
                            newfn = fname
                            index += 1
                            fn = fname.split(".")
                            nm = fn[0] + "(" + str(index) + ")"
                            fe = fn[1]

                            newfn = nm + "." + fe

                    f = open("".join(("data/", toUsr, "/files/", fname, ".bin")), "wb")
                    while True:
                        data = self.conn.recv(4096)
                        l = len(data) - 5

                        try:
                            if data[l:] == b'[end]':
                                f.write(data[:l])
                                f.close()
                                lfiles = lfiles + fname + ","
                                sz = os.path.getsize("".join(("data/", toUsr, "/files/", fname, ".bin")))
                                sz = round(sz / 1024, 2)
                                mdb.stat(self.usr, "file", str(sz), now_time_str, str(now_date))
                                Log().local(self.usr, "Send file: " + fname + " to " + toUsr, LOG_INFO, mdb)
                                mdb.add_file(fname, "file", self.usr, toUsr, str(now_date), now_time_str)
                                self.conn.send("complete".encode('utf-8'))
                                break
                        except:
                            Log().local(self.usr, "Error while downloading files", LOG_CRITICAL, mdb)

                        f.write(data)
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
            s.bind((self.cfg["TcpServer"]["ip"], self.cfg["TcpServer"]["port"]))
            s.listen(int(self.cfg["TcpServer"]["clients"]))
        except:
            Log().local("SERVER", "Error of binding ip address", LOG_CRITICAL)
            return

        print(
            """
            ##########################################################################
            #                                                                        #
            #                     Doku Mail Server 2.0 Started                       #
            #                                                                        #
            ##########################################################################
            """)

        while True:
            conn, addr = s.accept()
            proc = mp.Process(target=ServerThread, args=(conn, addr, self.cfg))
            proc.start()


def main():
    config = Configs().load()

    """
	Start server listener
	"""
    main_thread = MainThread()
    main_thread.set_configs(config)
    main_thread.setDaemon(True)

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
