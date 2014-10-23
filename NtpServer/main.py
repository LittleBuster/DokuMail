__author__ = 'sergey'
import sys
import json
import socket
from logger import *
import multiprocessing as mp
from threading import Thread
from datetime import datetime


class pObj(object):
    """
    JSON class for configs
    """
    pass


class ServerThread():
    def __init__(self, _sock, _addr):
        self.sock = _sock
        self.addr = _addr
        self.header = "DokuMail 2.0 Header - p1.0.0"
        self.run()

    def run(self):
        data = b''
        try:
            data = self.sock.recv(1024).decode("utf-8")
            data = json.loads(data)
        except:
            Log().local(str(self.addr), "Client crashed", LOG_CRITICAL)
            self.sock.close()
            return

        if not data["header"] == self.header:
            Log().local(str(self.addr), "Incorrect header. Access denided.", LOG_CRITICAL)
            return

        if data["cmd"] == "get-datetime":
            date = str(datetime.now()).split(".")[0]
            answ = {"header": self.header, "date": date.split(" ")[0], "time": date.split(" ")[1]}
            self.sock.send(json.dumps(answ).encode("utf-8"))
            self.sock.close()
            print("[" + str(self.addr[0]) + "]:Time sended.")


class Server(Thread):
    def __init__(self):
        super(Server, self).__init__()

    def set_configs(self, config):
        self.cfg = config

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind((self.cfg["NtpServer"]["ip"], self.cfg["NtpServer"]["port"]))
            s.listen(int(self.cfg["NtpServer"]["clients"]))
        except:
            Log().local("SERVER", "Error of binding ip address", LOG_CRITICAL)
            return

        print(
            """
            ##########################################################################
            #                                                                        #
            #                     Doku Mail NTP Server Started                       #
            #                                                                        #
            ##########################################################################
            """)

        while True:
            conn, addr = s.accept()
            proc = mp.Process(target=ServerThread, args=(conn, addr))
            proc.start()


def main():
    config = {}
    try:
        f = open("config.cfg", "r")
        config = json.load(f)
        f.close()
    except:
        Log().local("SERVER", "Error of reading config file", LOG_CRITICAL)
        return

    """
	Start server listener
	"""
    main_thread = Server()
    main_thread.set_configs(config)
    main_thread.setDaemon(True)

    while True:
        cmd = input("NtpServer> ")

        if cmd == "start":
            print("starting server...")
            main_thread.start()

        if cmd == "exit" or cmd == "quit" or cmd == "q":
            break

    print("Goodbye!")
    sys.exit()


if __name__ == '__main__':
    main()