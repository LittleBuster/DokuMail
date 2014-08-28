#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
from crypt import *
from compress import *
import hashlib
import shutil
from PyQt5 import QtCore
from logger import Log


class TcpClient(QtCore.QObject):
    """
	Class for low-level communication with a socket
	"""
    downloadStart = QtCore.pyqtSignal(str)
    decryptStart = QtCore.pyqtSignal()
    decompressStart = QtCore.pyqtSignal()
    downloadComplete = QtCore.pyqtSignal()
    fileDownloaded = QtCore.pyqtSignal()
    fileCount = QtCore.pyqtSignal(int)

    def __init__(self):
        super(TcpClient, self).__init__()

    def connect(self, ip, port, user, pwd):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((ip, port))
        except:
            Log().local("TCP Client: error connection to server: " + ip)
            return False

        self.sock.send(b"[LOGIN]")
        print(self.sock.recv(1024))

        h = hashlib.sha512()
        h.update(pwd.encode('utf-8'))
        h_passwd = h.hexdigest().upper()

        """
        Send creditionals login and password hash to server
        """
        cred = "login$" + user + "$" + h_passwd + "$"
        self.sock.send(cred.encode('utf-8'))

        if self.sock.recv(1024) == b'[LOGIN-OK]':
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
            self.sock.connect((ip, port))
            self.sock.close()
            return True
        except:
            return False

    def send_message(self, toUsers, message):
        try:
            self.sock.send(("[MSG-SEND]$" + toUsers).encode('utf-8'))
            answ = self.sock.recv(1024)
            if answ == b"[FAIL-ACCESS]":
                return answ

            self.sock.send(AES256_encode_msg(message, "transf.crt"))
            answ = self.sock.recv(1024)

            return answ
        except:
            Log().local("TCP Server: Fail sending message")
            return b"[FAIL]"

    def begin_send_files(self, toUser):
        """
        Init send files process
        """
        self.sock.send(("[SEND-FILES]$" + toUser).encode('utf-8'))
        print(self.sock.recv(1024))

    def send_file(self, fname):
        """
        Send single file to server
        """
        lsf = fname.split("/")
        l = len(lsf)

        self.sock.send(("sf$" + lsf[l - 1]).encode("utf-8"))
        print(self.sock.recv(1024).decode('utf-8'))

        f = open(fname + ".bin", "rb")

        while True:
            data = f.read(4096)
            if len(data) != 0:
                self.sock.send(data)
            else:
                break
        f.close()
        self.sock.send(b"[end]")
        print(self.sock.recv(1024).decode('utf-8'))

    def end_send_files(self):
        """
        Stop sending files process
        """
        self.sock.send(b"[END-RETRIEVE]")

    def get_messages(self):
        """
        Get from server 1 last message
        """
        self.sock.send(b'[GET-MSG]')
        msgInfo = self.sock.recv(1024).decode("utf-8")

        if msgInfo == '[EMPTY-MSG]':
            self.sock.close()
            print("No new messages")
            return "[EMPTY-MSG]"

        self.sock.send(b"ok")
        data = self.sock.recv(4096)

        msg = {'FromUser': msgInfo.split("$")[0], 'Time': msgInfo.split("$")[1]}
        try:
            msg["Data"] = AES256_decode_msg(data, "transf.crt")
        except:
            Log().local("Error reading message file")
        return msg

    def get_files(self, update, cur_path):
        """
        Get all files for client, from remote TCP server
        """
        exts = []
        try:
            f = open("unzip_formats.cfg", "r")
            exts = f.readline().split(",")
            f.close()
        except:
            Log().local("Error reading unzip formats file")

        c_exts = []
        try:
            f = open("uncrypt_formats.cfg", "r")
            c_exts = f.readline().split(",")
            f.close()
        except:
            Log().local("Error reading uncrypt formats file")

        if update:
            self.sock.send('[GET-FILES]$[UPDATE]'.encode('utf-8'))
        else:
            self.sock.send('[GET-FILES]$[DOWNLOAD]'.encode('utf-8'))

        if not update:
            if not os.path.exists(cur_path + "downloads"):
                os.makedirs(cur_path + "downloads")
        else:
            if not os.path.exists(cur_path + "update/data"):
                os.makedirs(cur_path + "update/data")

        cnt = int(self.sock.recv(1024).decode("utf-8"))
        self.sock.send(b"ok")

        self.fileCount.emit(cnt)

        while True:
            data = self.sock.recv(1024)

            if data == b'[NOT-FILES]':
                break

            if data == b"[END-RETRIEVE]":
                self.downloadComplete.emit()
                print("All files recieved")
                break

            print("Start downloading...")
            self.sock.send(b'recieveing...')

            try:
                fname = data.decode('utf-8').split("$")[1]
            except:
                return
            print("New file: " + fname)

            self.downloadStart.emit(fname)

            if update:
                dest = "update/data/"
                destf = dest + fname
            else:
                dest = "downloads/"
                destf = dest + fname + ".bin"

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
                                if not AES256_decode_file(dest + fname + ".bin", dest + fname + ".z", "transf.crt"):
                                    Log().local("Error decrypting recieved file: " + fname)
                                    print("error decrypting")
                            else:
                                shutil.copy2(dest + fname + ".bin", dest + fname + ".z")

                            self.decompressStart.emit()

                            if isDecompress:
                                print("Decompress: " + fname)
                                if not zlib_decompress_file(dest + fname + ".z", dest + fname):
                                    Log().local("Error decompressing recieved file: " + fname)
                                    print("error decompressing")
                            else:
                                shutil.copy2(dest + fname + ".z", dest + fname)

                        self.fileDownloaded.emit()

                        if not update:
                            os.remove(dest + fname + ".bin")
                            os.remove(dest + fname + ".z")

                        break
                except:
                    Log().local("Fatal error when files recieved")
                    print('except')

                f.write(data)

    def close(self):
        self.sock.close()
