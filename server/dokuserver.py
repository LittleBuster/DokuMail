import os
import sys
import json
import socket
import threading
import datetime
from logger import Log
from mariadb import MariaDB
import multiprocessing as mp


class pObj(object):
    """
    JSON class for configs
    """
    pass


class ServerThread():
    cfg = {}

    def __init__(self, _sock, _addr, cfg):
        super(ServerThread, self).__init__()
        self.conn = _sock
        self.addr = _addr
        self.cfg = cfg
        self.header = "DokuMail 2.0 Header - p1.0.0"

        #try:
        self.run()
        #except:
        #    Log().local("Client: " + str(_addr[0]) + " has crashed.")
        #    return

    def run(self):
        cmd = b''
        try:
            cmd = self.conn.recv(1024).decode("utf-8")
            cmd = json.loads(cmd)
        except:
            return

        if cmd["header"] == self.header and cmd["type"] == "login":
            self.conn.send(b'ok')
            data = self.conn.recv(1024).decode('utf-8')
            data = json.loads(data)

            if not data["header"] == self.header and not data["type"] == "login":
                return

            self.usr = data["user"]
            h_pwd = data["passwd"]

            """
            Check user's login and password
            """

            mdb = MariaDB()
            if not mdb.connect(self.cfg["MariaDB"]["ip"], self.cfg["MariaDB"]["login"],
                               self.cfg["MariaDB"]["password"], self.cfg["MariaDB"]["base"]):
                Log().local("Error connection to Database")
                return

            if not mdb.check_login(self.usr, h_pwd):
                Log().local("Access denided. Client " + self.usr + " disconnected.")
                mdb.close()
                self.conn.close()
                return

            """
            User authorized
            """
            self.conn.send(json.dumps({"header": self.header, "answ": "login-ok"}).encode("utf-8"))
            Log().local("Client " + self.usr + " authorized.")

            """
            Reciveing files
            """
            lfiles = str("")

            now_date = datetime.date.today()
            now_time = datetime.datetime.now()
            msg_name = str(now_date.year) + str(now_date.month) + str(now_date.day) + str(now_time.hour) + str(
                now_time.minute) + str(now_time.second)

            now_time_str = str(now_time).split(" ")[1].split(".")[0]

            data = self.conn.recv(1024).decode('utf-8')
            data = json.loads(data)

            if data["type"] == 'get-message':
                answ = {"header": self.header, "answ": ""}
                msgInfo = mdb.get_msg_info(self.usr)

                if msgInfo["type"] == "empty":
                    mdb.change_state(self.usr, "isMsg", 0)
                    print("No new messages")
                    answ["answ"] = "empty-msg"
                    self.conn.send(json.dumps(answ).encode("utf-8"))
                    self.conn.close()
                    Log().local("Client " + self.usr + " disconnected.")
                    return

                idMsg = msgInfo["name"]
                fromMsg = msgInfo["from"]
                timeMsg = msgInfo["time"]

                answ = {"header": self.header, "answ": "msg", "From": mdb.get_alias_by_user(fromMsg), "Time": timeMsg}

                self.conn.send(json.dumps(answ).encode("utf-8"))
                self.conn.recv(1024)

                f = open("".join(("data/", self.usr, "/", idMsg, ".bin")), "rb")
                self.conn.send(f.read())
                f.close()
                mdb.delete_message(self.usr, fromMsg, idMsg)

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
                    self.sock.send(json.dumps(answ).encode("utf-8"))
                    return

                answ = {"header": self.header, "count": len(files)}
                self.conn.send(json.dumps(answ).encode("utf-8"))
                self.conn.recv(1024)

                dest = str

                if not isUpdate:
                    print("Sending files... " + str(len(files)))
                else:
                    print("Start Update...")

                for sfile in files:
                    answ = {"header": self.header, "type": "sf", "filename": sfile}
                    self.conn.send(json.dumps(answ).encode("utf-8"))
                    print(self.conn.recv(1024))
                    Log().local("User " + self.usr + " get file " + sfile)

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
                            break;
                    f.close()
                    self.conn.send(b"[end]")
                    if not isUpdate:
                        path = str
                        mdb.delete_file(self.usr, sfile)
                        os.remove("data/" + self.usr + "/files/" + sfile + ".bin")
                    print(self.conn.recv(1024).decode('utf-8'))

                Log().local(self.usr + ": All files geted.")
                answ = {"header": self.header, "type": "end-retrieve"}
                self.conn.send(json.dumps(answ).encode("utf-8"))
                if not isUpdate:
                    mdb.change_state(self.usr, "isFiles", 0)
                else:
                    mdb.change_state(self.usr, "isUpdate", 0)
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
                    Log().local(self.usr + ": does not have privileges! Disconnected.")
                    self.conn.close()
                    return

                answ["answ"] = "ok"
                self.conn.send(json.dumps(answ).encode("utf-8"))
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
                    mdb.log(self.usr, "Отправил сообщение " + toUsr, str(now_date), now_time_str)
                    Log().local("Message from " + self.usr + " to " + toUsr + " saved.")
                    mdb.change_state(toUsr, "isMsg", 1)

                answ["answ"] = "send-msg-ok"
                self.conn.send(json.dumps(answ).encode("utf-8"))

            """
            Send files
            """

            if data["type"] == "send-files":
                self.conn.send(b'ok')
                toUsr = data["ToUser"]

                while True:
                    answ = self.conn.recv(1024).decode("utf-8")
                    answ = json.loads(answ)

                    if not answ["header"] == self.header:
                        return

                    if answ["type"] == "end-retrieve":
                        mdb.log(self.usr, "Отправил файлы (" + lfiles + ") - " + toUsr, str(now_date), now_time_str)
                        Log().local(self.usr + " отправил файлы (" + lfiles + ") - " + toUsr)
                        mdb.change_state(toUsr, "isFiles", 1)
                        print("All files recieved")
                        break

                    if not os.path.exists("".join(("data/" + toUsr + "/files/"))):
                        print("create subdir")
                        os.makedirs("".join(("data/", toUsr, "/files/")))

                    print("Start downloading...")
                    self.conn.send(b'recieveing...')

                    fname = ""

                    if answ["type"] == "sf":
                        fname = answ["filename"]
                        print("New file: " + fname)

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
                                print("Download complete")
                                f.write(data[:l])
                                f.close()
                                lfiles = lfiles + fname + ","
                                mdb.add_file(fname, "file", self.usr, toUsr, str(now_date), now_time_str)
                                self.conn.send("complete".encode('utf-8'))
                                break
                        except:
                            Log().local(self.usr + "Error while getting files")

                        f.write(data)
            Log().local("Client " + self.usr + " disconnected")
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
            Log().local("Error of binding ip address")
            return

        print(
            """
		#############################################################################
		#									                                        #
		#			 Doku Mail Server Started			                            #
		#									                                        #
		#############################################################################
		
		""")

        while True:
            conn, addr = s.accept()
            proc = mp.Process(target=ServerThread, args=(conn, addr, self.cfg))
            proc.start()


def main():
    config = {}
    try:
        f = open("config.cfg", "r")
        config = json.load(f)
        f.close()
    except:
        Log().local("Error of reading config file")
        return

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
