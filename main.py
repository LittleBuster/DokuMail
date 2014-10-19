#!/usr/bin/python
# -*- coding: utf-8 -*-
import getpass

import json
import sqlite3
import mainWnd
import datetime
import platform
from keys import AppKeys
import subprocess
from send import *
from crypt import *
from  msgbase import MessageBase
from PyQt4 import QtGui
from task import TaskWnd
from paths import AppPath
from configs import Configs
from mariadb import MariaDB
from checker import Checker
from login import LoginWindow
from tray import SystemTrayIcon
from recieve import Recieve, RecieveMsg
from news import NewsWnd, NewsCurWnd, NewsBaloonWnd


class pObj(object):
    """
    JSON temp class
    """
    pass


class MainWindow(QtGui.QWidget):
    __MDBServer = str
    __MDBUser = str
    __MDBPasswd = str
    __MDBBase = str
    __TCPServer = str
    __TCPPort = int
    loginWnd = LoginWindow
    cur_path = str

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.ui = mainWnd.Ui_Form()
        self.ui.setupUi(self)

        self.app_path = AppPath().main()

        self.user = str
        self.passwd = str
        self.news_count = 0

        self.history_in = True

        if platform.system() == "Linux":
            self.ui.label.setPixmap(QtGui.QPixmap( "".join((self.app_path, "images/fon2.png")) ))
            self.ui.lbAbout.setPixmap(QtGui.QPixmap( "".join((self.app_path, "images/about.png")) ))
            self.ui.lbCurUser.setPixmap(QtGui.QPixmap( "".join((self.app_path, "images/user.ico")) ))
            self.ui.pbNews.setIcon(QtGui.QIcon( "".join((self.app_path, "images/news.ico")) ))
            self.ui.pbCreateNews.setIcon(QtGui.QIcon( "".join((self.app_path, "images/news.ico")) ))
            self.ui.pbMessages.setIcon(QtGui.QIcon( "".join((self.app_path, "images/Email.png")) ))
            self.ui.pbFiles.setIcon(QtGui.QIcon( "".join((self.app_path, "images/filenew.png")) ))
            self.ui.pbTasks.setIcon(QtGui.QIcon( "".join((self.app_path, "images/filenew_8842.ico")) ))
            self.ui.pbSettings.setIcon(QtGui.QIcon( "".join((self.app_path, "images/settings.ico")) ))
            self.ui.pbDownloads.setIcon(QtGui.QIcon( "".join((self.app_path, "images/downloads.png")) ))
            self.ui.pbAbout.setIcon(QtGui.QIcon( "".join((self.app_path, "images/elena8d89.png")) ))
            self.ui.pbRelogin.setIcon(QtGui.QIcon( "".join((self.app_path, "images/touser.png")) ))
            self.ui.pbSendMsg.setIcon(QtGui.QIcon( "".join((self.app_path, "images/cloud.png")) ))
            self.ui.pbSendFiles.setIcon(QtGui.QIcon( "".join((self.app_path, "images/cloud.png")) ))
            self.ui.pbSendAllMsg.setIcon(QtGui.QIcon( "".join((self.app_path, "images/users.ico")) ))
            self.ui.pbClearMsg.setIcon(QtGui.QIcon( "".join((self.app_path, "images/recycle.png")) ))
            self.ui.pbClearFiles.setIcon(QtGui.QIcon( "".join((self.app_path, "images/recycle.png")) ))
            self.ui.pbDeleteFile.setIcon(QtGui.QIcon( "".join((self.app_path, "images/cancel.png")) ))
            self.ui.pbAddFile.setIcon(QtGui.QIcon( "".join((self.app_path, "images/add.png")) ))
            self.ui.pbCreateTask.setIcon(QtGui.QIcon( "".join((self.app_path, "images/filenew_8842.ico")) ))
            self.ui.pbSetConfig.setIcon(QtGui.QIcon( "".join((self.app_path, "images/settings.ico")) ))
            self.ui.pbClearHistory.setIcon(QtGui.QIcon( "".join((self.app_path, "images/recycle.png")) ))
            self.ui.pbCloseHistory.setIcon(QtGui.QIcon( "".join((self.app_path, "images/exit.png")) ))
            self.ui.pbOutgoing.setIcon(QtGui.QIcon( "".join((self.app_path, "images/up.ico")) ))
            self.ui.pbIncoming.setIcon(QtGui.QIcon( "".join((self.app_path, "images/down.ico")) ))

        QtCore.QObject.connect(self.ui.pbMinimize, QtCore.SIGNAL("clicked()"), self.minimize_app)
        self.tr = SystemTrayIcon(self, QtGui.QIcon( os.path.join(self.app_path, "images/cmp.ico")) )
        self.tr.show()

        QtCore.QObject.connect(self.ui.pbSendMsg, QtCore.SIGNAL("clicked()"), self.on_send_msg)
        QtCore.QObject.connect(self.ui.pbSendAllMsg, QtCore.SIGNAL("clicked()"),self.on_sendall_msg)
        QtCore.QObject.connect(self.ui.lwUsers, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"),self.lwusers_item_clicked)
        QtCore.QObject.connect(self.ui.pbClearMsg, QtCore.SIGNAL("clicked()"), self.on_clear_msg_clicked)
        QtCore.QObject.connect(self.ui.pbSendFiles, QtCore.SIGNAL("clicked()"), self.on_sendfiles_clicked)
        QtCore.QObject.connect(self.ui.pbAddFile, QtCore.SIGNAL("clicked()"), self.on_add_file)
        QtCore.QObject.connect(self.ui.pbClearFiles, QtCore.SIGNAL("clicked()"), self.on_clear_files)
        QtCore.QObject.connect(self.ui.pbDeleteFile, QtCore.SIGNAL("clicked()"), self.on_delete_file)

        QtCore.QObject.connect(self.ui.pbNews, QtCore.SIGNAL("clicked()"),self.on_news_clicked)
        QtCore.QObject.connect(self.ui.pbMessages, QtCore.SIGNAL("clicked()"), self.on_messages_clicked)
        QtCore.QObject.connect(self.ui.pbFiles, QtCore.SIGNAL("clicked()"), self.on_files_clicked)
        QtCore.QObject.connect(self.ui.pbTasks, QtCore.SIGNAL("clicked()"), self.on_tasks_clicked)
        QtCore.QObject.connect(self.ui.pbSettings, QtCore.SIGNAL("clicked()"), self.on_settings_clicked)
        QtCore.QObject.connect(self.ui.pbAbout, QtCore.SIGNAL("clicked()"), self.on_about_clicked)
        QtCore.QObject.connect(self.ui.pbCreateTask, QtCore.SIGNAL("clicked()"), self.on_create_task)

        QtCore.QObject.connect(self.ui.pbIncoming, QtCore.SIGNAL("clicked()"), self.on_incoming_clicked)
        QtCore.QObject.connect(self.ui.pbOutgoing, QtCore.SIGNAL("clicked()"), self.on_outgoing_clicked)
        QtCore.QObject.connect(self.ui.lwHistory, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"),self.lwhist_item_clicked)

        """
        Task List
        """

        self.ui.cbTaskType.addItem("")
        self.ui.cbTaskType.addItem("Microsoft Office")
        self.ui.cbTaskType.addItem("Интернет")
        self.ui.cbTaskType.addItem("Принтер")
        self.ui.cbTaskType.addItem("Антивирус")
        self.ui.cbTaskType.addItem("Другое")
        self.ui.cbTaskDiff.addItem("Низкая")
        self.ui.cbTaskDiff.addItem("Средняя")
        self.ui.cbTaskDiff.addItem("Высокая")

        lst = list()
        lst.append("№")
        lst.append("Тип проблемы")
        lst.append("Дата")
        lst.append("Решение")
        self.ui.tw1.setHorizontalHeaderLabels(lst)
        self.ui.tw1.horizontalHeader().resizeSection(0, 30)
        self.ui.tw1.horizontalHeader().resizeSection(1, 350)
        self.ui.tw1.horizontalHeader().resizeSection(2, 100)
        """"""

        self.send_files = SendFiles()
        self.recieve = Recieve()
        self.taskWnd = TaskWnd()
        self.newsWnd = NewsWnd()
        self.newsCurWnd = NewsCurWnd()
        self.recieveMsg = RecieveMsg()
        self.newsBaloon = NewsBaloonWnd()

        QtCore.QObject.connect(self.newsBaloon, QtCore.SIGNAL("hideBaloon()"), self.on_baloon_close)
        QtCore.QObject.connect(self.recieveMsg, QtCore.SIGNAL("msgComplete()"), self.on_msg_complete)
        QtCore.QObject.connect(self.recieve, QtCore.SIGNAL("downloadComplete(bool)"), self.on_download_complete)
        QtCore.QObject.connect(self.taskWnd.ui.pbSendTask, QtCore.SIGNAL("clicked()"), self.on_send_task)
        QtCore.QObject.connect(self.ui.pbSetConfig, QtCore.SIGNAL("clicked()"), self.on_set_config)
        QtCore.QObject.connect(self.ui.pbCreateNews, QtCore.SIGNAL("clicked()"), self.on_create_news)
        QtCore.QObject.connect(self.newsWnd.ui.pbSendNews, QtCore.SIGNAL("clicked()"), self.on_send_news)
        QtCore.QObject.connect(self.ui.lwNews, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"), self.on_lwnews_clicked)
        QtCore.QObject.connect(self.newsBaloon.ui.pbRead, QtCore.SIGNAL("clicked()"), self.on_read_news)
        QtCore.QObject.connect(self.newsBaloon.ui.pbClose, QtCore.SIGNAL("clicked()"), self.on_baloon_close)
        self.newsBaloon.ui.pbClose.clicked.connect(self.on_baloon_close)

        self.checker = Checker(self)
        QtCore.QObject.connect(self.newsCurWnd.ui.pbDeleteNews, QtCore.SIGNAL("clicked()"), self.checker.on_delete_news)
        QtCore.QObject.connect(self.ui.pbRelogin, QtCore.SIGNAL("clicked()"), self.on_relogin)
        QtCore.QObject.connect(self.ui.pbDownloads, QtCore.SIGNAL("clicked()"), self.on_downloads)
        QtCore.QObject.connect(self.ui.pbCloseHistory, QtCore.SIGNAL("clicked()"), self.on_messages_clicked)
        QtCore.QObject.connect(self.ui.pbClearHistory, QtCore.SIGNAL("clicked()"), self.on_clearhistory_clicked)

    """
    Properties for configs
    """

    def setTcpServer(self, server):
        self.__TCPServer = server
        self.ui.leTcpServer.setText(server)

    def getTcpServer(self):
        return self.__TCPServer

    def setTcpPort(self, port):
        self.__TCPPort = port
        self.ui.leTcpPort.setText(str(port))

    def getTcpPort(self):
        return self.__TCPPort

    def setMDBServer(self, server):
        self.__MDBServer = server
        self.ui.leMDBServer.setText(server)

    def getMDBServer(self):
        return self.__MDBServer

    def setMDBUser(self, user):
        self.__MDBUser = user
        self.ui.leMDBUser.setText(user)

    def getMDBUser(self):
        return self.__MDBUser

    def setMDBPasswd(self, passwd):
        self.__MDBPasswd = passwd
        self.ui.leMDBPasswd.setText(passwd)

    def getMDBPasswd(self):
        return self.__MDBPasswd

    def setMDBBase(self, passwd):
        self.__MDBBase = passwd

    def getMDBBase(self):
        return self.__MDBBase

    TCPServer = property(getTcpServer, setTcpServer)
    TCPPort = property(getTcpPort, setTcpPort)
    MDBServer = property(getMDBServer, setMDBServer)
    MDBUser = property(getMDBUser, setMDBUser)
    MDBPasswd = property(getMDBPasswd, setMDBPasswd)
    MDBBase = property(getMDBBase, setMDBBase)

    """"""

    def on_msg_complete(self):
        self.checker.getTmr.start(5000)

    def on_download_complete(self, update):
        if not update:
            self.checker.getTmr.start(5000)
        else:
            import platform

            if platform.system() == "Windows":
                import win32api

                os.chdir("update")
                win32api.ShellExecute(0, 'open', 'update.exe', '', '', 1)
            QtGui.QApplication.quit()

    def on_create_news(self):
        mdb = MariaDB()
        if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, self.MDBBase):
            QtGui.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!',
                                           QtGui.QMessageBox.Yes)
            return
        if mdb.is_admin(self.user):
            self.newsWnd.show()
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'У вас нет прав на создание новостей!',
                                          QtGui.QMessageBox.Yes)
        mdb.close()

    def on_send_news(self):
        """
        Create news record in database
        """
        if self.newsWnd.ui.leTitle.text() == "":
            QtGui.QMessageBox.warning(self.newsWnd, 'Error', 'Введите заголовок новости!', QtGui.QMessageBox.Yes)
            return

        if self.newsWnd.ui.teNews.document().toPlainText() == "" or \
                        self.newsWnd.ui.teNews.document().toPlainText() == "Напишите новость...":
            QtGui.QMessageBox.warning(self.newsWnd, 'Error', 'Введите текст новости!', QtGui.QMessageBox.Yes)
            return

        mdb = MariaDB()
        if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, self.MDBBase):
            QtGui.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!',
                                           QtGui.QMessageBox.Yes)
            return
        date = datetime.date.today()
        if mdb.send_news(mdb.get_alias_by_user(self.user), self.newsWnd.ui.teNews.document().toPlainText(),
                         self.newsWnd.ui.leTitle.text(), str(date)):
            self.newsWnd.close()
            mdb.log(self.user, "".join(("Добавил новость [", self.newsWnd.ui.leTitle.text(), "]")))

            client = TcpClient()
            client.connect(self.TCPServer, self.TCPPort, self.user, self.passwd)
            client.create_news(self.newsWnd.ui.leTitle.text())
            client.close()

            QtGui.QMessageBox.information(self, 'Complete', 'Новость успешно добавлена!', QtGui.QMessageBox.Yes)
        else:
            QtGui.QMessageBox.critical(self, 'Error', 'Ошибка добавления новости', QtGui.QMessageBox.Yes)
        mdb.close()

    def on_read_news(self):
        """
        Click on newslist item
        """
        item = QtGui.QListWidgetItem()
        item.setText(self.newsBaloon.ui.leTitle.text())
        self.newsBaloon.hide()
        self.on_lwnews_clicked(item)

    def on_baloon_close(self):
        self.newsBaloon.close()
        con = sqlite3.connect( "".join((self.app_path, 'news.db')))
        cur = con.cursor()
        title = self.newsBaloon.ui.leTitle.text().split("]")[1]
        date = self.newsBaloon.ui.leTitle.text().split("[")[1].split("]")[0]

        cur.execute("DELETE FROM news WHERE title='" + title + "' and date='" + date + "'")
        con.commit()
        con.close()

    def on_relogin(self):
        self.checker.stop_timers()
        self.hide()
        self.ui.lwUsers.clear()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.loginWnd.show()

    def on_send_task(self):
        mdb = MariaDB()
        if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, self.MDBBase):
            QtGui.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtGui.QMessageBox.Yes)
            return

        date = datetime.date.today()
        if mdb.create_task(self.user, self.taskWnd.ui.teMsg.document().toPlainText(), self.ui.cbTaskType.currentText(),
                           date, self.ui.cbTaskDiff.currentText(), "Нет"):
            self.taskWnd.ui.teMsg.clear()
            self.taskWnd.close()
            self.check_tasks()
            QtGui.QMessageBox.information(self, 'Complete', 'Заявка зарегистрирована', QtGui.QMessageBox.Yes)
        else:
            QtGui.QMessageBox.critical(self, 'Ошибка', 'Ошибка при регистрации заявки', QtGui.QMessageBox.Yes)
        mdb.close()

    def on_create_task(self):
        if self.ui.cbTaskType.currentText() != "":
            self.taskWnd.show()
        else:
            QtGui.QMessageBox.warning(self, 'Ошибка', 'Выберите тип проблемы!', QtGui.QMessageBox.Yes)

    def check_tasks(self):
        self.ui.tw1.setRowCount(0)
        mdb = MariaDB()
        if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, self.MDBBase):
            QtGui.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!', QtGui.QMessageBox.Yes)
            return
        taskList = mdb.get_task_list(self.user)

        for task in taskList:
            self.ui.tw1.setRowCount(self.ui.tw1.rowCount() + 1)
            item = QtGui.QTableWidgetItem(task["id"])
            self.ui.tw1.setItem(self.ui.tw1.rowCount() - 1, 0, item)
            item = QtGui.QTableWidgetItem(task["type"])
            self.ui.tw1.setItem(self.ui.tw1.rowCount() - 1, 1, item)
            item = QtGui.QTableWidgetItem(task["date"])
            self.ui.tw1.setItem(self.ui.tw1.rowCount() - 1, 2, item)
            item = QtGui.QTableWidgetItem(task["status"])
            self.ui.tw1.setItem(self.ui.tw1.rowCount() - 1, 3, item)
        mdb.close()

    def on_set_config(self):
        result = QtGui.QMessageBox.question(self, 'Configs', 'Применить изменения?',
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                                QtGui.QMessageBox.No)
        if result == QtGui.QMessageBox.Yes:
            self.TCPServer = self.ui.leTcpServer.text()
            try:
                self.TCPPort = int(self.ui.leTcpPort.text())
            except:
                Log().local("Settings: set not port correct")
                QtGui.QMessageBox.critical(self, 'Ошибка', 'Неверный номер порта!', QtGui.QMessageBox.Yes)
            self.MDBServer = self.ui.leMDBServer.text()
            self.MDBUser = self.ui.leMDBUser.text()
            self.MDBPasswd = self.ui.leMDBPasswd.text()

            config = {}
            config["TcpServer"] = self.TCPServer
            config["TcpPort"] = self.TCPPort
            config["MDBServer"] = self.MDBServer
            config["MDBUser"] = self.MDBUser
            config["MDBPasswd"] = self.MDBPasswd
            config["MDBBase"] = self.MDBBase
            self.checker.set_configs(config, self.user)

            self.save_config()

    def on_downloads(self):
        cfg = Configs()
        if not os.path.exists(cfg.downloads_path()):
            QtGui.QMessageBox.warning(self, 'Ошибка', 'Нет загруженных файлов!', QtGui.QMessageBox.Yes)
            return

        if platform.system() == "Linux":
            for mngr in cfg.file_managers():
                if os.path.exists("".join(("/usr/bin/", mngr))):
                    subprocess.call("".join((mngr, " ", cfg.downloads_path())), shell=True)
                    break
        else:
            import win32api
            win32api.ShellExecute(0, 'open', cfg.downloads_path(), '', '', 1)

    def on_delete_file(self):
        try:
            self.ui.lwFiles.removeItemWidget(
                self.ui.lwFiles.takeItem(self.ui.lwFiles.row(self.ui.lwFiles.selectedItems()[0])))
        except:
            QtGui.QMessageBox.warning(self, 'Ошибка', 'Выделите файл!', QtGui.QMessageBox.Yes)

    def on_news_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_tasks_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_settings_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_about_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_messages_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_files_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_clear_msg_clicked(self):
        self.ui.teMsg.clear()

    def on_incoming_clicked(self):
        lst = []
        self.history_in = True
        self.ui.label_19.setText("<html><head/><body><p><span style=' color:#ffffff;'>История (Входящие сообщения)\
                                    </span></p></body></html>")
        self.ui.lwHistory.clear()
        self.ui.stackedWidget.setCurrentIndex(6)
        mb = MessageBase()
        try:
            lst = mb.load_message_list(True)
        except:
            QtGui.QMessageBox.warning(self, 'Warning', 'У Вас нет входящих сообщений', QtGui.QMessageBox.Yes)
            return

        if len(lst) == 0:
            return
        else:
            for msg in lst:
                item = QtGui.QListWidgetItem()
                item.setIcon(QtGui.QIcon( "".join((self.app_path, "images/conv.ico")) ))
                item.setText(msg)
                self.ui.lwHistory.insertItem(0, item)

    def on_outgoing_clicked(self):
        lst = []
        self.ui.label_19.setText("<html><head/><body><p><span style=' color:#ffffff;'>История (Исходящие сообщения)\
                                    </span></p></body></html>")
        self.history_in = False
        self.ui.lwHistory.clear()
        self.ui.stackedWidget.setCurrentIndex(6)
        mb = MessageBase()
        try:
            lst = mb.load_message_list(False)
        except:
            QtGui.QMessageBox.warning(self, 'Warning', 'У Вас нет исходящих сообщений', QtGui.QMessageBox.Yes)
            return

        if len(lst) == 0:
            return
        else:
            for msg in lst:
                item = QtGui.QListWidgetItem()
                item.setIcon(QtGui.QIcon( "".join((self.app_path, "images/conv.ico")) ))
                item.setText(msg)
                self.ui.lwHistory.insertItem(0, item)

    def lwhist_item_clicked(self, item):
        mb = MessageBase()
        msg = mb.get_message(item.text(), self.history_in)

        if self.history_in:
            self.recieveMsg.msgWnd.ui.lbFrom.setText(
                "<html><head/><body><p><span style='color:#ffffff;'>" + msg["from"] + "</span></p></body></html>")
            self.recieveMsg.msgWnd.ui.lbTime.setText(
                "<html><head/><body><p><span style='color:#ffffff;'>" + msg["time"] + "</span></p></body></html>")
            self.recieveMsg.msgWnd.ui.teMsg.setPlainText(msg["text"])
            self.recieveMsg.msgWnd.ui.lbFormTitle.setText('<html><head/><body><p><span style=" color:#00dbff;">От кого:\
                                                            </span></p></body></html>')
            self.recieveMsg.msgWnd.show()
        else:
            self.recieveMsg.msgWnd.ui.lbFormTitle.setText('<html><head/><body><p><span style=" color:#00dbff;">Кому:\
                                                            </span></p></body></html>')
            self.recieveMsg.msgWnd.ui.lbFrom.setText(
                "<html><head/><body><p><span style='color:#ffffff;'>" + msg["to"] + "</span></p></body></html>")
            self.recieveMsg.msgWnd.ui.lbTime.setText(
                "<html><head/><body><p><span style='color:#ffffff;'>" + msg["time"] + "</span></p></body></html>")
            self.recieveMsg.msgWnd.ui.teMsg.setPlainText(msg["text"])
            self.recieveMsg.msgWnd.show()

    def on_clearhistory_clicked(self):
        """
        Delete all in or out messages
        """
        result = QtGui.QMessageBox.question(self, 'Очистка', 'Вы действительно хотите удалить все сообщения?',
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if result == QtGui.QMessageBox.Yes:
            mb = MessageBase()
            try:
                mb.clear_messages(self.history_in)
                self.ui.lwHistory.clear()
            except:
                QtGui.QMessageBox.warning(self, 'Очистка', 'У Вас нет сообщений', QtGui.QMessageBox.Yes)

    def on_lwnews_clicked(self, item):
        """
        Show current clicked news
        """
        title = str(item.text()).split("]")[1]
        mdb = MariaDB()
        if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, self.MDBBase):
            QtGui.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!',
                                           QtGui.QMessageBox.Yes)
            return
        news = mdb.get_news(title)
        self.newsCurWnd.ui.lbFrom.setText("<html><head/><body><p><span style='color:#ffffff;'>" + news["user"]
                                          + "</span></p></body></html>")
        self.newsCurWnd.ui.lbTime.setText("<html><head/><body><p><span style='color:#ffffff;'>" + news["date"]
                                          + "</span></p></body></html>")
        self.newsCurWnd.ui.teNews.setPlainText(news["news"])
        self.newsCurWnd.ui.leTitle.setText(news["title"])
        self.newsCurWnd.show()
        mdb.close()

    def lwusers_item_clicked(self, item):
        self.ui.lbAlias.setText(str(item.text()))

    def closeEvent(self, e):
        result = QtGui.QMessageBox.question(self, 'Закрытие', 'Вы действительно хотите выйти из программы?',
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                                QtGui.QMessageBox.No)
        if result == QtGui.QMessageBox.Yes:
            QtGui.QApplication.quit()
        else:
            e.ignore()

    def init_app(self):
        cfg = Configs()
        mdb = MariaDB()
        if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, self.MDBBase):
            QtGui.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!',
                                           QtGui.QMessageBox.Yes)
            return
        aliases = mdb.get_alias_list()
        mdb.close()

        i = 0
        for alias in aliases:
            item = QtGui.QListWidgetItem()
            item.setIcon(QtGui.QIcon( os.path.join(self.app_path, "images", cfg.get_icons()["UsersIcon"])) )
            item.setText(alias)
            self.ui.lwUsers.insertItem(i, item)
            i += 1

        self.check_tasks()

        config = dict(TcpServer=self.TCPServer, TcpPort=self.TCPPort, MDBServer=self.MDBServer, MDBUser=self.MDBUser,
                      MDBPasswd=self.MDBPasswd, MDBBase=self.MDBBase)
        self.checker.set_configs(config, self.user)
        self.checker.start_timers()

    def save_config(self):
        cfg = Configs().cfg
        cfg["MariaDB"]["ip"] = self.ui.leMDBServer.text()
        cfg["MariaDB"]["base"] = self.ui.leMDBBase.text()
        cfg["TcpServer"]["ip"] = self.ui.leTcpServer.text()
        cfg["TcpServer"]["port"] = int(self.ui.leTcpPort.text())

        parts = []
        try:
            self.ui.leDownloadsPath.text().split()
            cfg["DownloadsPath"].clear()
            cfg["DownloadsPath"].append(parts[0])
            cfg["DownloadsPath"].append(getpass.getuser())
            cfg["DownloadsPath"].append(parts[2])
        except:
            cfg["DownloadsPath"].clear()
            cfg["DownloadsPath"].append(self.ui.leDownloadsPath.text())

        Configs().save_to_file(cfg)
        print(cfg)

        """
        Save MariaDB login and password
        """

        f = open( "".join((self.app_path, "servercred.tmp")), "w")
        cfg = {"MariaDB": {"login": self.MDBUser, "password": self.MDBPasswd}}
        config = pObj()
        config.cfg = cfg
        json.dump(config.cfg, f)
        f.close()

        DES3_encrypt_file("".join((self.app_path,"servercred.tmp")), "".join((self.app_path,"servercred.dat")), 16,
                                  AppKeys().get_config_key()["key"], AppKeys().get_config_key()["IV"])
        os.remove("".join((self.app_path,"servercred.tmp")))


    def load_config(self):
        """
        Load and parse json config file "Config.cgf" and
        Load database login and password from crypted cfg file "servercred.dat"
        """
        cfg = Configs()
        try:
            self.MDBServer = cfg.db_config()["ip"]
            self.TCPServer = cfg.tcp_config()["ip"]
            self.TCPPort = cfg.tcp_config()["port"]
            self.MDBBase = cfg.db_config()["base"]
            self.ui.leMDBBase.setText(cfg.db_config()["base"])
            self.ui.leDownloadsPath.setText(cfg.downloads_path())
        except:
            Log().local("Error reading config file")
            QtGui.QMessageBox.critical(self, 'Ошибка', 'Ошибка чтения конфигурационного файла!',
                                           QtGui.QMessageBox.Yes)

        if not os.path.isfile( "".join((self.app_path, "servercred.dat")) ):
            Log().local("Auth file not exists")
            QtGui.QMessageBox.critical(self, 'Ошибка', 'Отсутствует файл аутинтификации!', QtGui.QMessageBox.Yes)
            QtGui.QApplication.quit()
            return

        """
        Load database login and password
        """

        try:
            DES3_decrypt_file("".join((self.app_path,"servercred.dat")), "".join((self.app_path,"servercred.tmp")), 16,
                                  AppKeys().get_config_key()["key"], AppKeys().get_config_key()["IV"])

            f = open( "".join((self.app_path, "servercred.tmp")), "r")
            cfg = json.load(f)
            self.MDBUser = cfg["MariaDB"]["login"]
            self.MDBPasswd = cfg["MariaDB"]["password"]
            f.close()
            os.remove("".join((self.app_path,"servercred.tmp")))
        except:
            Log().local("Error reading auth file")
            QtGui.QMessageBox.critical(self, 'Ошибка', 'Ошибка чтения файла аутинтификации!', QtGui.QMessageBox.Yes)

    def on_send_msg(self):
        send_msg(self, self.ui.teMsg.document().toPlainText(), False, self.passwd, self.ui.lbAlias.text())

    def on_sendall_msg(self):
        send_msg(self, self.ui.teMsg.document().toPlainText(), True, self.passwd, None)

    def on_sendfiles_clicked(self):
        flist = list()
        items = self.ui.lwFiles.count()

        if items == 0:
            QtGui.QMessageBox.warning(self, 'Error', 'Добавьте файлы для передачи', QtGui.QMessageBox.Yes)
            return

        for i in range(items):
            flist.append(self.ui.lwFiles.item(i).text())

        self.send_files.send(self, flist, self.ui.lbAlias.text())

    def minimize_app(self):
        self.hide()

    def on_clear_files(self):
        self.ui.lwFiles.clear()

    def on_add_file(self):
        cfg = Configs()
        op_path = ""
        if platform.system() == "Linux":
            op_path = AppPath().home()
        else:
            op_path = "C:/"

        filenames = QtGui.QFileDialog.getOpenFileNames(self, 'Open file', op_path)

        items = self.ui.lwFiles.count()
        for f in filenames:
            flag = False
            for i in range(items):
                fname = self.ui.lwFiles.item(i).text()
                if fname == f:
                    QtGui.QMessageBox.warning(self, 'Error', 'Файл "' + f + '" уже добавлен в очередь передачи',
                                                  QtGui.QMessageBox.Yes)
                    flag = True
                    break

            if not flag:
                parts = f.split('.')
                ext = parts[len(parts) - 1].lower()
                ico = ""
                try:
                    ico = cfg.get_icons()["FileIcons"][ext]
                except:
                    ico = cfg.get_icons()["FileIcons"]["default"]

                item = QtGui.QListWidgetItem()
                item.setIcon(QtGui.QIcon( "".join((self.app_path, "images/ext/", ico)) ))
                item.setText(f)
                self.ui.lwFiles.insertItem(0, item)