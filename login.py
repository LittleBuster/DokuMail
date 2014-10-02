#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import loginWnd
from crypt import *
from PyQt4 import QtGui
from PyQt4 import QtCore
from mariadb import MariaDB
from wndparams import WndParams


class pObj(object):
    """
    JSON temp class
    """
    pass


class LoginWindow(QtGui.QWidget):
    """
    Class which connect Login Window interface
    in python app
    """

    isAuto = bool

    def __init__(self, parent=None):
        super(LoginWindow, self).__init__()
        self.ui = loginWnd.Ui_Form()
        self.ui.setupUi(self)

        self.loginTmr = QtCore.QTimer()
        QtCore.QObject.connect(self.loginTmr, QtCore.SIGNAL("timeout()"), self.on_autologin)
        QtCore.QObject.connect(self.ui.pbLogin, QtCore.SIGNAL("clicked()"), self.on_login)
        QtCore.QObject.connect(self.ui.pbCancel, QtCore.SIGNAL("clicked()"), self.on_cancel)

        WndParams().on_screen_center(self)


    def set_wnds(self, mw):
        """
        Start Autologin timer
        """
        self._mw = mw

        if platform.system() == "Linux":
            self.ui.lbBack.setPixmap(QtGui.QPixmap( "".join((self._mw.app_path, "images/fon3.png")) ))
            self.ui.label.setPixmap(QtGui.QPixmap( "".join((self._mw.app_path, "images/logo.png")) ))
            self.ui.pbLogin.setIcon(QtGui.QIcon( "".join((self._mw.app_path, "images/login.png")) ))
            self.ui.pbCancel.setIcon(QtGui.QIcon( "".join((self._mw.app_path, "images/exit.png")) ))

        if os.path.isfile( "".join((self._mw.app_path, "svpwd.dat"))):
            self.load_passwd()

        if not ((self.ui.edLogin.text() == "") or (self.ui.edPasswd.text() == "")):
            self.loginTmr.start(2000)

    def finish(self):
        self._mw.hide()

    def on_login(self):
        """
        Checking login and password in database and init start processes
        in main window. After close login windows and show main window.
        """
        self.loginTmr.stop()
        state = False

        if (self.ui.edLogin.text() == "") or (self.ui.edPasswd.text() == ""):
            QtGui.QMessageBox.warning(self, 'Ошибка', 'Введите логин или пароль!', QtGui.QMessageBox.Yes)
            return

        if (self.ui.cbSave.checkState() == QtCore.Qt.Checked):
            self.save_passwd()

        mdb = MariaDB()
        if not mdb.connect(self._mw.MDBServer, self._mw.MDBUser, self._mw.MDBPasswd, "DokuMail"):
            QtGui.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!',
                                           QtGui.QMessageBox.Yes)
            return
        state = mdb.check_login(self.ui.edLogin.text(), self.ui.edPasswd.text())
        username = mdb.get_alias_by_user(self.ui.edLogin.text())
        mdb.close()

        if state == True:
            self.hide()

            WndParams().on_screen_center(self._mw)
            self._mw.setWindowTitle("Doku (" + username + ")")
            self._mw.show()

            import platform

            if platform.system() == "Windows" and self.isAuto:
                QtCore.QTimer().singleShot(1500, self.finish)

            self._mw.passwd = self.ui.edPasswd.text()
            self._mw.user = self.ui.edLogin.text()
            self._mw.loginWnd = self
            self._mw.init_app()
        else:
            QtGui.QMessageBox.critical(self, 'Ошибка', 'Неверный логин или пароль!', QtGui.QMessageBox.Yes)


    def save_passwd(self):
        """
        Create json object. Send password in it.
        Save json object in file.
        """
        f = open("".join((self._mw.app_path, "svpwd.tmp")), "w")
        cfgPasswd = pObj()
        cfgPasswd.config = {}
        cfgPasswd.config["login"] = self.ui.edLogin.text()
        cfgPasswd.config["passwd"] = self.ui.edPasswd.text()
        json.dump(cfgPasswd.config, f)
        f.close()
        DES3_encrypt_file("".join((self._mw.app_path, "svpwd.tmp")), "".join((self._mw.app_path, "svpwd.dat")), 16,
                          b'*', b'*')
        os.remove("".join((self._mw.app_path, "svpwd.tmp")))

    def load_passwd(self):
        """
        Create json object. Load password from file in it.
        Set password and login in line edits.
        """
        try:
            DES3_decrypt_file("".join((self._mw.app_path,"svpwd.dat")), "".join((self._mw.app_path,"svpwd.tmp")), 16,
                              b'*', b'*')
            f = open("".join((self._mw.app_path,"svpwd.tmp")), "r")
            cfgPasswd = json.load(f)
            self.ui.edLogin.setText(cfgPasswd["login"])
            self.ui.edPasswd.setText(cfgPasswd["passwd"])
            f.close()
            os.remove("".join((self._mw.app_path,"svpwd.tmp")))
        except:
            self.ui.edLogin.setText("")
            self.ui.edPasswd.setText("")
            if os.path.exists("".join((self._mw.app_path,"svpwd.dat"))):
                os.remove("".join((self._mw.app_path,"svpwd.dat")))

    def on_autologin(self):
        """
        After some time check edits and try autologin
        """
        self.loginTmr.stop()
        self.on_login()

    def on_cancel(self):
        """
        Emergency stop autologin
        """
        self.loginTmr.stop()
        self.ui.edLogin.setText("")
        self.ui.edPasswd.setText("")