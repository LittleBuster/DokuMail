#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import json
import getpass
from paths import AppPath
from PyQt4 import QtGui
from logger import Log


class pObj(object):
    """
    JSON temp class
    """
    pass

class Configs(object):
    cfg = {}

    def __init__(self, path=None):
        pth = ""
        app_path = AppPath().main()
        if path == None:
            pth = "".join((app_path, "config.cfg"))
        else:
            pth = path

        if not os.path.isfile( pth ):
            Log().local("Config file not exists")
            QtGui.QMessageBox.critical(QtGui.QWidget(), 'Ошибка', 'Отсутствует файл конфигураций!',
                                       QtGui.QMessageBox.Yes)
            QtGui.QApplication.quit()
            return

        f = None
        if path == None:
            f = open(pth, "r")
        else:
            f = open(pth, "r")

        try:
            self.cfg = json.load(f)
        except:
            QtGui.QMessageBox.critical(QtGui.QWidget(), 'Ошибка', 'Неверный файл конфигураций!', QtGui.QMessageBox.Yes)
            import sys
            sys.exit()
        f.close()

    def new(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance

    def save_to_file(self, cfg=None):
        f = open("".join((AppPath().main(), "config.cfg")), "w")
        config = pObj()
        config.cfg = cfg
        json.dump(config.cfg, f)
        f.close()

    def downloads_path(self):
        path = ""
        for part in self.cfg["DownloadsPath"]:
            if part == "$USER_PATH$":
                path += getpass.getuser()
            else:
                path += part
        return path

    def db_config(self):
        return self.cfg["MariaDB"]

    def tcp_config(self):
        return self.cfg["TcpServer"]

    def file_managers(self):
        return self.cfg["FileManagers"]

    def unzip_formats(self):
        return self.cfg["UnzipFormats"]

    def uncrypt_formats(self):
        return self.cfg["UncryptFormats"]

    def get_icons(self):
        return self.cfg["Icons"]


class PacketHeader(object):
    """
    Packets header for exchanging messaging between client and server
    """
    def new(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance

    def header(self):
        return "DokuMail 2.0 Header - p1.0.0"