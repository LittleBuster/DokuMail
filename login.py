#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
import loginWnd
from mariadb import MariaDB
from PyQt5 import QtCore, QtWidgets


class pObj(object):
    """
	JSON temp class
	"""
    pass


class LoginWindow(QtWidgets.QWidget):
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
        self.loginTmr.timeout.connect(self.on_autologin)
        self.ui.pbLogin.clicked.connect(self.on_login)
        self.ui.pbCancel.clicked.connect(self.on_cancel)

        width = self.frameGeometry().width()
        height = self.frameGeometry().height()

        wid = QtWidgets.QDesktopWidget()
        screenWidth = wid.screen().width()
        screenHeight = wid.screen().height()

        self.setGeometry((screenWidth / 2) - (width / 2), (screenHeight / 2) - (height / 2), width, height)

        if os.path.isfile("svpwd.dat"):
            self.load_passwd()

    def set_wnds(self, mw):
        """
        Start Autologin timer
        """
        self._mw = mw
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
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Введите логин или пароль!', QtWidgets.QMessageBox.Yes)
            return

        if (self.ui.cbSave.checkState() == QtCore.Qt.Checked):
            self.save_passwd()

        mdb = MariaDB()
        if not mdb.connect(self._mw.MDBServer, self._mw.MDBUser, self._mw.MDBPasswd, "DokuMail"):
            QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!',
                                           QtWidgets.QMessageBox.Yes)
            return
        state = mdb.check_login(self.ui.edLogin.text(), self.ui.edPasswd.text())
        username = mdb.get_alias_by_user(self.ui.edLogin.text())
        mdb.close()

        if state == True:
            self.hide()

            """
            Show window on center of the screen
            """

            width = self._mw.frameGeometry().width()
            height = self._mw.frameGeometry().height()

            wid = QtWidgets.QDesktopWidget()
            screenWidth = wid.screen().width()
            screenHeight = wid.screen().height()

            self._mw.setGeometry((screenWidth / 2) - (width / 2), (screenHeight / 2) - (height / 2), width, height)
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
            QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Неверный логин или пароль!', QtWidgets.QMessageBox.Yes)


    def save_passwd(self):
        """
        Create json object. Send password in it.
        Save json object in file.
        """
        f = open("svpwd.dat", "w")
        cfgPasswd = pObj()
        cfgPasswd.config = {}
        cfgPasswd.config["login"] = self.ui.edLogin.text()
        cfgPasswd.config["passwd"] = self.ui.edPasswd.text()
        json.dump(cfgPasswd.config, f)
        f.close()

    def load_passwd(self):
        """
        Create json object. Load password from file in it.
        Set password and login in line edits.
        """
        try:
            f = open("svpwd.dat", "r")
            cfgPasswd = json.load(f)
            self.ui.edLogin.setText(cfgPasswd["login"])
            self.ui.edPasswd.setText(cfgPasswd["passwd"])
            f.close()
        except:
            self.ui.edLogin.setText("")
            self.ui.edPasswd.setText("")
            os.remove("svpwd.dat")

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