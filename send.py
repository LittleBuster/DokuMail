#!/usr/bin/python
# -*- coding: utf-8 -*-

import shutil
from crypt import *
from paths import AppPath
from msgbase import MessageBase
from compress import *
from logger import Log
from PyQt4 import QtGui
from configs import Configs
from PyQt4 import QtCore
from mariadb import MariaDB
from upload import UploadWindow
from tcpclient import TcpClient



def send_msg(wnd, msg, all, lUsrPwd, usr):
    """
    Send message to remote tcp server
    """
    answ = str
    toUser = str

    if msg == "":
        QtGui.QMessageBox.warning(wnd, 'Complete', 'Введите сообщение!', QtGui.QMessageBox.Yes)
        return

    if (usr == "") and (not all):
        """
        If message sending to single user and user not selected then fail
        """
        QtGui.QMessageBox.warning(wnd, 'Complete', 'Выберите пользователя!', QtGui.QMessageBox.Yes)
        return

    mdb = MariaDB()
    if not mdb.connect(wnd.MDBServer, wnd.MDBUser, wnd.MDBPasswd, wnd.MDBBase):
        QtGui.QMessageBox.critical(wnd, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtGui.QMessageBox.Yes)
        return

    if not all:
        toUser = mdb.get_user_by_alias(usr)
    mdb.close()

    client = TcpClient()
    if not client.connect(wnd.TCPServer, wnd.TCPPort, wnd.user, lUsrPwd):
        QtGui.QMessageBox.critical(wnd, "Ошибка", "Ошибка соединения с сервером!", QtGui.QMessageBox.Yes)
        return

    if not all:
        answ = client.send_message(toUser, msg)
    else:
        answ = client.send_message("$ALL_USERS$", msg)
    client.close()

    if answ == "[FAIL]":
        QtGui.QMessageBox.critical(wnd, 'Ошибка', 'Ошибка передачи сообщения!', QtGui.QMessageBox.Yes)
        client.close()
        return

    if answ == "[FAIL-LEN]":
        QtGui.QMessageBox.critical(wnd, 'Ошибка', 'Сообщение слишком длинное!', QtGui.QMessageBox.Yes)
        client.close()
        return

    if answ == "[FAIL-ACCESS]":
        QtGui.QMessageBox.critical(wnd, 'Ошибка', 'У Вас нет прав на отправку всем пользователям!',
                                       QtGui.QMessageBox.Yes)
        client.close()
        return

    if answ == "[SEND-MSG-OK]":
        mb = MessageBase()
        if not all:
            mb.save_message(usr, msg, False)
            QtGui.QMessageBox.information(wnd, 'Complete', 'Сообщение отправлено!', QtGui.QMessageBox.Yes)
        else:
            mb.save_message("Всем", msg, False)
            QtGui.QMessageBox.information(wnd, 'Complete', 'Сообщение отправлено всем пользователям!',
                                              QtGui.QMessageBox.Yes)


class SendFilesThread(QtCore.QThread):
    connectionStart = QtCore.pyqtSignal()
    err = QtCore.pyqtSignal(str)
    compressStart = QtCore.pyqtSignal(str)
    cryptStart = QtCore.pyqtSignal(str)
    sendStart = QtCore.pyqtSignal(str)
    sendComplete = QtCore.pyqtSignal()
    sendFileComplete = QtCore.pyqtSignal()

    def __init__(self):
        super(SendFilesThread, self).__init__()
        self.cfg = Configs()
        self.app_path = AppPath().main()
        self.a_key = AES256_cert_read("".join((self.app_path, "transf.crt")))

    def send(self, wnd, TCPServer, TCPPort, flist, toUsr):
        """
        Set connection configs
		"""
        self._wnd = wnd
        self._server = TCPServer
        self._port = TCPPort
        self.fileList = flist
        self._toUsr = toUsr

    def run(self):
        toUser = str("")
        self.client = TcpClient()

        mdb = MariaDB()
        if not mdb.connect(self._wnd.MDBServer, self._wnd.MDBUser, self._wnd.MDBPasswd, self._wnd.MDBBase):
            self.err.emit('Ошибка соединения с Базой Данных!')
            return
        toUser = mdb.get_user_by_alias(self._toUsr)
        mdb.close()

        if not os.path.exists("".join((self._wnd.app_path, "sendfiles"))):
            os.makedirs("".join((self._wnd.app_path,"sendfiles")))

        self.connectionStart.emit()
        if not self.client.connect(self._server, self._port, self._wnd.user, self._wnd.passwd):
            print("fail connection")
            self.err.emit("Ошибка соединения с сервером!")
            return

        exts = []
        try:
            exts = self.cfg.unzip_formats()
        except:
            Log().local("Error reading unzip formats")

        c_exts = []
        try:
            c_exts = self.cfg.uncrypt_formats()
        except:
            Log().local("Error reading uncrypted formats")

        print("start send")
        self.client.begin_send_files(toUser)

        for sfile in self.fileList:
            lsf = sfile.split("/")
            l = len(lsf)
            fname = lsf[l - 1]

            """
            Checking extension
			"""
            isCompress = True
            isCrypt = True

            tmp_fname = fname.split(".")
            ext = tmp_fname[len(tmp_fname) - 1].lower()

            for ex in exts:
                if ex == ext:
                    isCompress = False
                    break

            for ex in c_exts:
                if ex == ext:
                    isCrypt = False
                    break

            """
            Rename file
            """
            while True:
                try:
                    parts = fname.split("'")
                    fname = ""
                    l = len(parts)
                    i = 0
                    for part in parts:
                        i += 1
                        if i < l:
                            fname = fname + part + "_"
                        else:
                            fname = fname + part
                    break
                except:
                    break

            self.compressStart.emit(fname)
            if isCompress:
                if not zlib_compress_file(sfile, "".join((self._wnd.app_path, "sendfiles/", fname, ".z"))):
                    Log().local("Error compressing send file: " + fname)
                    print("error compressing")
                    self.client.close()
                    self.err.emit("Ошибка при сжатии файла")
                    return
                else:
                    print("".join((fname, " compressed")))
            else:
                print(fname + " not compressed")
                shutil.copy2(sfile, "sendfiles/" + fname + ".z")

            if isCrypt:
                self.cryptStart.emit(fname)
                if not AES256_encode_file("".join((self._wnd.app_path, "sendfiles/", fname, ".z")),
                                          "".join((self._wnd.app_path, "sendfiles/", fname, ".bin")),
                                          self.a_key):
                    Log().local("Error encrypting send file: " + fname)
                    print("error crypting")
                    self.client.close()
                    self.err.emit("Ошибка при шифровании сообщения")
                else:
                    print("".join((fname, " crypted")))
            else:
                print(fname + " not crypt")
                shutil.copy2("".join((self._wnd.app_path,"sendfiles/", fname, ".z")),
                             "".join((self._wnd.app_path,"sendfiles/", fname, ".bin")))

            self.sendStart.emit(fname)
            self.client.send_file("".join((self._wnd.app_path, "sendfiles/", fname)))
            self.sendFileComplete.emit()

            try:
                os.remove("".join((self._wnd.app_path, "sendfiles/", fname, ".z")))
                os.remove("".join((self._wnd.app_path, "sendfiles/", fname, ".bin")))
            except:
                Log().local("Error filename")
                self.err.emit("Ошибка в имени файла!")

        self.client.end_send_files()

        self.sendComplete.emit()
        print("send complete")
        self.client.close()


class SendFiles(QtCore.QObject):
    sth = SendFilesThread()

    def __init__(self):
        super(SendFiles, self).__init__()

        QtCore.QObject.connect(self.sth, QtCore.SIGNAL("connectionStart()"), self.on_connection_start)
        QtCore.QObject.connect(self.sth, QtCore.SIGNAL("compressStart(QString)"), self.on_compress_start)
        QtCore.QObject.connect(self.sth, QtCore.SIGNAL("cryptStart(QString)"), self.on_crypt_start)
        QtCore.QObject.connect(self.sth, QtCore.SIGNAL("sendStart(QString)"), self.on_send_start)
        QtCore.QObject.connect(self.sth, QtCore.SIGNAL("sendComplete()"), self.on_send_complete)
        QtCore.QObject.connect(self.sth, QtCore.SIGNAL("sendFileComplete()"), self.on_send_file_complete)
        QtCore.QObject.connect(self.sth, QtCore.SIGNAL("err(QString)"), self.on_error)

        self.uploadWnd = UploadWindow()

    def on_connection_start(self):
        self.uploadWnd.ui.pB.setValue(0)
        self.uploadWnd.show()
        self.uploadWnd.ui.lbAct.setText(
            "<html><head/><body><p><span style=' color:#00d4ff;'>Соединение...</span></p></body></html>")
        self.uploadWnd.ui.lbFile.setText("")

    def on_compress_start(self, filename):
        self.uploadWnd.ui.lbAct.setText(
            "<html><head/><body><p><span style=' color:#00d4ff;'>Сжатие:</span></p></body></html>")
        self.uploadWnd.ui.lbFile.setText(
            "<html><head/><body><p><span style=' color:#ffffff;'>" + filename + "</span></p></body></html>")
        self.uploadWnd.ui.pB.setValue(0)

    def on_crypt_start(self, filename):
        self.uploadWnd.ui.lbAct.setText(
            "<html><head/><body><p><span style=' color:#00d4ff;'>Шифрование:</span></p></body></html>")
        self.uploadWnd.ui.pB.setValue(33)

    def on_send_start(self, filename):
        self.uploadWnd.ui.lbAct.setText(
            "<html><head/><body><p><span style=' color:#00d4ff;'>Отправка:</span></p></body></html>")
        self.uploadWnd.ui.pB.setValue(66)

    def on_send_file_complete(self):
        self.uploadWnd.ui.lbAct.setText(
            "<html><head/><body><p><span style=' color:#00d4ff;'>Готово.</span></p></body></html>")
        self.uploadWnd.ui.lbFile.setText("")
        self.uploadWnd.ui.pB.setValue(100)

    def on_send_complete(self):
        self.uploadWnd.ui.lbAct.setText(
            "<html><head/><body><p><span style=' color:#00d4ff;'>Готово.</span></p></body></html>")
        self.uploadWnd.ui.lbFile.setText("")
        self.uploadWnd.ui.pB.setValue(100)
        QtGui.QMessageBox.information(self.uploadWnd, "Complete", "Файлы отправлены!", QtGui.QMessageBox.Yes)
        self.uploadWnd.hide()

    def on_error(self, txt):
        QtGui.QMessageBox.critical(self.uploadWnd, "Ошибка", txt, QtGui.QMessageBox.Yes)
        self.uploadWnd.hide()

    def send(self, wnd, flist, toUsr):
        if toUsr == "":
            QtGui.QMessageBox.warning(wnd, 'Complete', 'Выберите пользователя!', QtGui.QMessageBox.Yes)
            return
        self._wnd = wnd
        self.sth.send(wnd, wnd.TCPServer, wnd.TCPPort, flist, toUsr)
        try:
            self.sth.start()
        except:
            self.on_error("Ошибка отправки файлов")
            Log().local("Ошибка отправки файлов")