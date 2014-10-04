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

    def __init__(self):
        app_path = AppPath().main()

        if not os.path.isfile( "".join((app_path, "config.cfg")) ):
            Log().local("Config file not exists")
            QtGui.QMessageBox.critical(QtGui.QWidget(), 'Ошибка', 'Отсутствует файл конфигураций!',
                                       QtGui.QMessageBox.Yes)
            QtGui.QApplication.quit()
            return

        f = open("".join((app_path, "config.cfg")), "r")
        self.cfg = json.load(f)
        f.close()

    def new(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance

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