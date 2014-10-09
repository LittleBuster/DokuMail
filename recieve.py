#!/usr/bin/python
# -*- coding: utf-8 -*-

from msg import MsgWnd
from PyQt4 import QtGui
from PyQt4 import QtCore
from configs import Configs
from msgbase import MessageBase
from tcpclient import TcpClient
from download import DownloadWnd
from update import UpdateWnd


class TcpConfig():
    __tcpServer = str
    __tcpPort = int
    __user = str
    __passwd = str

    def setTcpServer(self, server):
        self.__tcpServer = server

    def getTcpServer(self):
        return self.__tcpServer

    def setTcpPort(self, port):
        self.__tcpPort = port

    def getTcpPort(self):
        return self.__tcpPort

    def setUser(self, user):
        self.__user = user

    def getUser(self):
        return self.__user

    def setPasswd(self, passwd):
        self.__passwd = passwd

    def getPasswd(self):
        return self.__passwd

    TCPServer = property(getTcpServer, setTcpServer)
    TCPPort = property(getTcpPort, setTcpPort)
    user = property(getUser, setUser)
    passwd = property(getPasswd, setPasswd)


class RecieveThread(QtCore.QThread, TcpConfig):
    err = QtCore.pyqtSignal(str)
    downloadStart = QtCore.pyqtSignal(str)
    decryptStart = QtCore.pyqtSignal()
    decompressStart = QtCore.pyqtSignal()
    downloadComplete = QtCore.pyqtSignal()
    fileDownloaded = QtCore.pyqtSignal(str)
    fileCount = QtCore.pyqtSignal(int)

    update = False
    cur_path = str

    def __init__(self):
        super(RecieveThread, self).__init__()
        self.client = TcpClient()
        QtCore.QObject.connect(self.client, QtCore.SIGNAL("downloadStart(QString)"), self.on_download_start)
        QtCore.QObject.connect(self.client, QtCore.SIGNAL("decryptStart()"), self.on_decrypt_start)
        QtCore.QObject.connect(self.client, QtCore.SIGNAL("decompressStart()"), self.on_decompress_start)
        QtCore.QObject.connect(self.client, QtCore.SIGNAL("downloadComplete()"), self.on_download_complete)
        QtCore.QObject.connect(self.client, QtCore.SIGNAL("fileDownloaded(QString)"), self.on_file_downloaded)
        QtCore.QObject.connect(self.client, QtCore.SIGNAL("fileCount(int)"), self.on_file_count)

    def set_configs(self, tcpserver, tcpport, usr, pwd, update, path):
        self.TCPServer = tcpserver
        self.TCPPort = tcpport
        self.user = usr
        self.passwd = pwd
        self.update = update
        self.cur_path = path

    def on_file_downloaded(self, fname):
        self.fileDownloaded.emit(fname)

    def on_download_start(self, fname):
        self.downloadStart.emit(fname)

    def on_decrypt_start(self):
        self.decryptStart.emit()

    def on_decompress_start(self):
        self.decompressStart.emit()

    def on_download_complete(self):
        self.downloadComplete.emit()

    def on_file_count(self, cnt):
        self.fileCount.emit(cnt)

    def run(self):
        if self.client.connect(self.TCPServer, self.TCPPort, self.user, self.passwd):
            self.client.get_files(self.update, self.cur_path)
            self.client.close()


class Recieve(QtCore.QObject):
    downloadComplete = QtCore.pyqtSignal(bool)

    def __init__(self):
        super(Recieve, self).__init__()
        self.dldWnd = DownloadWnd()
        self.updWnd = UpdateWnd()
        self.recieveTh = RecieveThread()

        self.cfg = Configs()

        QtCore.QObject.connect(self.recieveTh, QtCore.SIGNAL("downloadStart(QString)"), self.on_download_start)
        QtCore.QObject.connect(self.recieveTh, QtCore.SIGNAL("decryptStart()"), self.on_decrypt_start)
        QtCore.QObject.connect(self.recieveTh, QtCore.SIGNAL("decompressStart()"), self.on_decompress_start)
        QtCore.QObject.connect(self.recieveTh, QtCore.SIGNAL("downloadComplete()"), self.on_download_complete)
        QtCore.QObject.connect(self.recieveTh, QtCore.SIGNAL("fileDownloaded(QString)"), self.on_file_downloaded)
        QtCore.QObject.connect(self.recieveTh, QtCore.SIGNAL("fileCount(int)"), self.on_file_count)
        QtCore.QObject.connect(self.recieveTh, QtCore.SIGNAL("err(QString)"), self.on_err)

        self.step = 0
        self.update = False
        self.fname = str("")

    def set_configs(self, tcpserver, tcpport, usr, pwd, update, path):
        self.update = update
        self.recieveTh.set_configs(tcpserver, tcpport, usr, pwd, update, path)
        if not self.update:
            self.dldWnd.ui.pb2.setValue(0)

    def on_download_start(self, fname):
        self.fname = fname
        if not self.update:
            self.dldWnd.ui.pb1.setValue(0)
            self.dldWnd.ui.lbFile.setText("<html><head/><body><p><span style='color:#00ffd5;'>" + "Загрузка: "
                                          + fname + "</span></p></body></html>")
        else:
            self.updWnd.ui.lbFile.setText("<html><head/><body><p><span style='color:#00d2ff;'>Загрузка: " + fname
                                          + "</span></p></body></html>")

    def on_decrypt_start(self):
        if not self.update:
            self.dldWnd.ui.pb1.setValue(33)
            self.dldWnd.ui.lbFile.setText("<html><head/><body><p><span style='color:#00ffd5;'>" + "Дешифрование: "
                                          + self.fname + "</span></p></body></html>")

    def on_decompress_start(self):
        if not self.update:
            self.dldWnd.ui.lbFile.setText("<html><head/><body><p><span style='color:#00ffd5;'>" + "Распаковка: "
                                          + self.fname + "</span></p></body></html>")
            self.dldWnd.ui.pb1.setValue(66)

    def on_file_downloaded(self, fname):
        if not self.update:
            self.dldWnd.ui.lbFile.setText(
                "<html><head/><body><p><span style='color:#00ffd5;'>Готово.</span></p></body></html>")

            parts = fname.split('.')
            ext = parts[len(parts) - 1].lower()
            ico = ""
            try:
                ico = self.cfg.get_icons()["FileIcons"][ext]
            except:
                ico = self.cfg.get_icons()["FileIcons"]["default"]

            item = QtGui.QListWidgetItem()
            item.setIcon(QtGui.QIcon( "".join((self.dldWnd.app_path, "images/ext/", ico))))
            item.setText(self.fname)

            self.dldWnd.ui.lwFiles.insertItem(0, item)
            self.dldWnd.ui.pb1.setValue(100)
            self.dldWnd.ui.pb2.setValue(self.dldWnd.ui.pb2.value() + self.step)

    def on_file_count(self, cnt):
        self.step = round(100 / cnt)

    def on_err(self, text):
        QtGui.QMessageBox.critical(self.dldWnd, 'Complete', text, QtGui.QMessageBox.Yes)

    def on_download_complete(self):
        if not self.update:
            self.dldWnd.ui.pb2.setValue(100)
            QtGui.QMessageBox.information(self.dldWnd, 'Complete', 'Приняты новые файлы!', QtGui.QMessageBox.Yes)
        self.downloadComplete.emit(self.update)

    def start(self):
        if not self.update:
            self.dldWnd.show()
        else:
            self.updWnd.show()
        self.recieveTh.start()


class RecieveMsgThread(QtCore.QThread, TcpConfig):
    msgRecieved = QtCore.pyqtSignal([str, str, str])
    msgNone = QtCore.pyqtSignal()

    def __init__(self):
        super(RecieveMsgThread, self).__init__()
        self.client = TcpClient()

    def set_configs(self, tcpserver, tcpport, usr, pwd):
        self.TCPServer = tcpserver
        self.TCPPort = tcpport
        self.user = usr
        self.passwd = pwd

    def run(self):
        if self.client.connect(self.TCPServer, self.TCPPort, self.user, self.passwd):
            msg = self.client.get_messages()
            if msg == "[EMPTY-MSG]":
                self.client.close()
                self.msgNone.emit()
            else:
                self.msgRecieved.emit(msg["FromUser"], msg["Time"], msg["Data"])
                self.client.close()


class RecieveMsg(QtCore.QObject):
    msgComplete = QtCore.pyqtSignal()

    def __init__(self):
        super(RecieveMsg, self).__init__()
        self.msgWnd = MsgWnd()
        self.rt = RecieveMsgThread()

        QtCore.QObject.connect(self.rt, QtCore.SIGNAL("msgRecieved(QString, QString, QString)"), self.show_msg)
        QtCore.QObject.connect(self.rt, QtCore.SIGNAL("msgNone()"), self.msg_empty)

    def show_msg(self, fromUser, timeMsg, Data):
        self.msgWnd.ui.lbFrom.setText(
            "<html><head/><body><p><span style='color:#ffffff;'>" + fromUser + "</span></p></body></html>")
        self.msgWnd.ui.lbTime.setText(
            "<html><head/><body><p><span style='color:#ffffff;'>" + timeMsg + "</span></p></body></html>")
        self.msgWnd.ui.teMsg.setPlainText(Data)
        self.msgWnd.ui.lbFormTitle.setText('<html><head/><body><p><span style=" color:#00dbff;">От кого:\
                                                            </span></p></body></html>')
        self.msgWnd.show()

        mb = MessageBase()
        mb.save_message(fromUser, Data, True)

        self.msgComplete.emit()

    def msg_empty(self):
        self.msgComplete.emit()

    def get_msg_status(self):
        if self.msgWnd.isVisible():
            return True
        else:
            return False

    def set_configs(self, tcpserver, tcpport, usr, pwd):
        self.rt.set_configs(tcpserver, tcpport, usr, pwd)

    def start(self):
        self.rt.start()