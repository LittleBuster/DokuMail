#!/usr/bin/python
# -*- coding: utf-8 -*-

import shutil
import socket
import json
import hashlib
import platform
from crypt import *
from configs import Configs, PacketHeader
from compress import *
from keys import AppKeys
from logger import Log
from PyQt4 import QtCore
from paths import AppPath


class TcpClient(QtCore.QObject):
    """
    Class for low-level communication with a socket
    """
    downloadStart = QtCore.pyqtSignal(str)
    decryptStart = QtCore.pyqtSignal()
    decompressStart = QtCore.pyqtSignal()
    downloadComplete = QtCore.pyqtSignal()
    fileDownloaded = QtCore.pyqtSignal(str)
    fileCount = QtCore.pyqtSignal(int)

    def __init__(self):
        super(TcpClient, self).__init__()
        self.app_path = AppPath().main()
        self.cfg = Configs()
        self.a_key = AES256_cert_read("".join((self.app_path, "transf.crt")))
        self.r_key = AES256_cert_read("".join((self.app_path, "retrieve.crt")))
        self.header = PacketHeader().header()

    def connect(self, ip, port, user, pwd):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((ip, int(port)))
        except:
            Log().local("TCP Client: error connection to server: " + ip)
            return False

        h = hashlib.sha512()
        h.update(pwd.encode('utf-8'))
        h_passwd = h.hexdigest().upper()

        """
        Send creditionals login and password hash to server
        """
        cred = {"header": self.header, "type": "login", "user": user, "passwd": h_passwd}
        self.sock.send(AES256_encode_msg(json.dumps(cred), self.r_key ))


        answ = AES256_decode_msg(self.sock.recv(1024), self.r_key )
        answ = json.loads(answ)

        if not answ["header"] == self.header:
            return

        if answ["answ"] == 'login-ok':
            print("Login ok")
            return True
        else:
            print("login fail")
            Log().local("TCP Server: Login fail")
            return False

    def check_status(self, ip, port):
        """
        Check server status: offline/online
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.sock.connect((ip, int(port)))
            self.sock.close()
            return True
        except:
            return False

    def create_news(self, news_header):
        data = {"header": self.header, "type": "news", "action": "create", "news-header": news_header}
        data = AES256_encode_msg( json.dumps(data), self.r_key )
        self.sock.send( data )

    def delete_news(self, news_header):
        data = {"header": self.header, "type": "news", "action": "delete", "news-header": news_header}
        data = AES256_encode_msg( json.dumps(data), self.r_key )
        self.sock.send( data )

    def send_message(self, toUsers, message):
        if len(message.encode("utf-8")) > 3050:
            return "[FAIL-LEN]"

        try:
            data = {"header": self.header, "type": "send-message", "ToUsers": toUsers}

            data = json.dumps(data)
            self.sock.send( AES256_encode_msg(data, self.r_key) )
            answ = AES256_decode_msg( self.sock.recv(1024), self.r_key )
            answ = json.loads( answ )

            if not answ["header"] == self.header:
                return "[FAIL]"

            if answ["answ"] == "fail-access":
                return "[FAIL-ACCESS]"

            data = {"header": self.header, "message": message}
            self.sock.send(AES256_encode_msg(json.dumps(data), self.a_key))

            answ = AES256_decode_msg(self.sock.recv(1024), self.r_key)
            answ = json.loads(answ)

            if answ["answ"] == "send-msg-ok":
                return "[SEND-MSG-OK]"
            else:
                return "[FAIL]"
        except:
            Log().local("TCP Server: Fail sending message")
            return "[FAIL]"

    def get_messages(self):
        """
        Get from server 1 last message
        """
        msg = {}
        data = {"header": self.header, "type": "get-message"}
        data = json.dumps(data)

        self.sock.send( AES256_encode_msg(data, self.r_key) )
        answ = AES256_decode_msg(self.sock.recv(1024), self.r_key)
        answ = json.loads(answ)

        if not answ["header"] == self.header:
            msg["Time"] = "-"
            msg["FromUser"] = "Client"
            msg["Data"] = "Сервер обмена не совместим с вашим протоколом."
            Log().local("Error header")
            return msg

        if answ["answ"] == 'empty-msg':
            self.sock.close()
            print("No new messages")
            return "[EMPTY-MSG]"

        self.sock.send(b"ok")
        data = self.sock.recv(4096)
        msg["FromUser"] = answ["From"]
        msg["Time"] = answ["Time"]
        try:
            data = AES256_decode_msg(data, self.a_key)
            data = json.loads(data)

            if not data["header"] == self.header:
                msg["Time"] = "-"
                msg["FromUser"] = "Client"
                msg["Data"] = "Сервер обмена не совместим с вашим протоколом."
                Log().local("Error header")
                return msg

            msg["Data"] = data["message"]
        except:
            Log().local("Error reading message file")
            msg["Data"] = "Ошибка декодирования сообщения"
        return msg

    def begin_send_files(self, toUser):
        """
        Init send files process
        """
        data = {"header": self.header, "type": "send-files", "ToUser": toUser}
        self.sock.send(AES256_encode_msg(json.dumps(data), self.r_key))
        print(self.sock.recv(1024))

    def send_file(self, fname):
        """
        Send single file to server
        """
        lsf = fname.split("/")
        l = len(lsf)

        data = {"header": self.header, "type": "sf", "filename": lsf[l - 1]}
        data = json.dumps(data)
        self.sock.send( AES256_encode_msg(data, self.r_key ))
        print(self.sock.recv(1024))

        f = open(fname + ".bin", "rb")

        while True:
            data = f.read(4096)
            if len(data) != 0:
                self.sock.send(data)
            else:
                break
        f.close()
        self.sock.send(b"[end]")
        print(self.sock.recv(1024))

    def end_send_files(self):
        """
        Stop sending files process
        """
        data = {"header": self.header, "type": "end-retrieve"}
        self.sock.send(AES256_encode_msg(json.dumps(data), self.r_key))

    def get_files(self, update, cur_path):
        """
        Get all files for client, from remote TCP server
        """
        exts = []
        try:
            exts = self.cfg.unzip_formats()
        except:
            Log().local("Error reading unzip formats")

        c_exts = []
        try:
            c_exts = self.cfg.uncrypt_formats()
        except:
            Log().local("Error reading uncrypt formats file")

        data = {}

        if update:
            data = {"header": self.header, "type": "get-files", "operation": "update"}
        else:
            data = {"header": self.header, "type": "get-files", "operation": "download"}

        self.sock.send(AES256_encode_msg(json.dumps(data), self.r_key))

        if not update:
            path = self.cfg.downloads_path()
            if not os.path.exists(path):
                os.makedirs( path )
        else:
            if not os.path.exists("".join((cur_path, "update/data"))):
                os.makedirs("".join((cur_path, "update/data")))

        answ = AES256_decode_msg(self.sock.recv(1024), self.r_key)
        answ = json.loads(answ)
        cnt = answ["count"]
        self.sock.send(b"ok")

        self.fileCount.emit(cnt)

        while True:
            data = AES256_decode_msg(self.sock.recv(1024), self.r_key)
            data = json.loads(data)

            if data["type"] == "not-files":
                break

            if data["type"] == "end-retrieve":
                self.downloadComplete.emit()
                print("All files recieved")
                break

            print("Start downloading...")
            self.sock.send(b'recieveing...')

            try:
                fname = data["filename"]
            except:
                return
            print("New file: " + fname)

            self.downloadStart.emit(fname)

            if update:
                dest = "".join((cur_path, "update/data/"))
                destf = "".join((dest, fname))
            else:
                dest = self.cfg.downloads_path()
                destf = "".join((dest, fname, ".bin"))

            """
            Check extention
            """
            isDecompress = True
            isCrypt = True

            tmp_fname = fname.split(".")
            ext = tmp_fname[len(tmp_fname) - 1].lower()

            for ex in exts:
                if ex == ext:
                    isDecompress = False
                    break

            for ex in c_exts:
                if ex == ext:
                    isCrypt = False
                    break

            f = open(destf, "wb")
            while True:
                data = self.sock.recv(4096)
                l = len(data) - 5

                try:
                    if data[l:] == b'[end]':
                        print("Download complete")
                        f.write(data[:l])
                        self.sock.send("complete".encode('utf-8'))
                        f.close()

                        if not update:
                            self.decryptStart.emit()

                            if isCrypt:
                                print("Decrypt: " + fname)
                                if not AES256_decode_file( "".join((dest, fname, ".bin")), "".join((dest, fname, ".z")),
                                                          self.a_key):
                                    Log().local("Error decrypting recieved file: " + fname)
                                    print("error decrypting")
                            else:
                                shutil.copy2("".join((dest, fname, ".bin")), "".join((dest, fname, ".z")))

                            self.decompressStart.emit()

                            if isDecompress:
                                print("Decompress: " + fname)
                                if not zlib_decompress_file("".join((dest, fname, ".z")), "".join((dest, fname))):
                                    Log().local("Error decompressing recieved file: " + fname)
                                    print("error decompressing")
                            else:
                                print("".join((fname, " not compressed")))
                                shutil.copy2("".join((dest, fname, ".z")), "".join((dest, fname)))

                        self.fileDownloaded.emit(fname)

                        if not update:
                            os.remove("".join((dest, fname, ".bin")))
                            os.remove("".join((dest, fname, ".z")))

                        break
                except:
                    Log().local("Fatal error when files recieved")
                    print('except')

                f.write(data)

    def close(self):
        self.sock.close()
