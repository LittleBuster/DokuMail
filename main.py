#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sqlite3
import mainWnd
import datetime
import platform
import subprocess
from send import *
from crypt import *
from PyQt4 import QtGui
from task import TaskWnd
from paths import AppPath
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

        self.cur_path = os.getcwd() + "/"

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

    TCPServer = property(getTcpServer, setTcpServer)
    TCPPort = property(getTcpPort, setTcpPort)
    MDBServer = property(getMDBServer, setMDBServer)
    MDBUser = property(getMDBUser, setMDBUser)
    MDBPasswd = property(getMDBPasswd, setMDBPasswd)

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
        if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "DokuMail"):
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
        if self.newsWnd.ui.leTitle.text() == "":
            QtGui.QMessageBox.warning(self.newsWnd, 'Error', 'Введите заголовок новости!',
                                          QtGui.QMessageBox.Yes)
            return

        if self.newsWnd.ui.teNews.document().toPlainText() == "" or \
                        self.newsWnd.ui.teNews.document().toPlainText() == "Напишите новость...":
            QtGui.QMessageBox.warning(self.newsWnd, 'Error', 'Введите текст новости!', QtGui.QMessageBox.Yes)
            return

        mdb = MariaDB()
        if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "DokuMail"):
            QtGui.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!',
                                           QtGui.QMessageBox.Yes)
            return
        date = datetime.date.today()
        if mdb.send_news(mdb.get_alias_by_user(self.user), self.newsWnd.ui.teNews.document().toPlainText(),
                         self.newsWnd.ui.leTitle.text(), str(date)):
            self.newsWnd.close()
            mdb.log(self.user, "".join(("Добавил новость [", self.newsWnd.ui.leTitle.text(), "]")))
            QtGui.QMessageBox.information(self, 'Complete', 'Новость успешно добавлена!', QtGui.QMessageBox.Yes)
        else:
            QtGui.QMessageBox.critical(self, 'Error', 'Ошибка добавления новости', QtGui.QMessageBox.Yes)
        mdb.close()

    def on_read_news(self):
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
        if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "DokuMail"):
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
        if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "DokuMail"):
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
            self.checker.set_configs(config, self.user)

            self.save_config()

    def on_downloads(self):
        if not os.path.exists("downloads"):
            QtGui.QMessageBox.warning(self, 'Ошибка', 'Нет загруженных файлов!', QtGui.QMessageBox.Yes)
            return

        if platform.system() == "Linux":
            f = open("".join((self.app_path, "wmanagers.cfg")), "r")
            managers = f.readline().split(',')
            f.close()

            for mngr in managers:
                if os.path.exists("".join(("/usr/bin/", mngr))):
                    subprocess.call("".join((mngr, " ", AppPath().home(), "downloads/")), shell=True)
                    break
        else:
            import win32api
            win32api.ShellExecute(0, 'open', 'downloads', '', '', 1)

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

    def on_lwnews_clicked(self, item):
        title = str(item.text()).split("]")[1]
        mdb = MariaDB()
        if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "DokuMail"):
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
        mdb = MariaDB()
        if not mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "DokuMail"):
            QtGui.QMessageBox.critical(self, 'Ошибка', 'Ошибка соединения с Базой Данных!',
                                           QtGui.QMessageBox.Yes)
            return
        aliases = mdb.get_alias_list()
        mdb.close()

        i = 0
        for alias in aliases:
            item = QtGui.QListWidgetItem()
            item.setIcon(QtGui.QIcon( os.path.join(self.app_path, "images", "cmp.ico")) )
            item.setText(alias)
            self.ui.lwUsers.insertItem(i, item)
            i += 1

        self.check_tasks()

        config = dict(TcpServer=self.TCPServer, TcpPort=self.TCPPort, MDBServer=self.MDBServer, MDBUser=self.MDBUser,
                      MDBPasswd=self.MDBPasswd)
        self.checker.set_configs(config, self.user)
        self.checker.start_timers()

    def save_config(self):
        f = open( "".join((self.app_path, "config.tmp")), "w")
        cfg = pObj()
        cfg.config = {"mdbserver": self.MDBServer, "mdbuser": self.MDBUser, "mdbpasswd": self.MDBPasswd,
                      "tcpserver": self.TCPServer, "tcpport": self.TCPPort}
        json.dump(cfg.config, f)
        f.close()

        DES3_encrypt_file("".join((self.app_path,"config.tmp")), "".join((self.app_path,"config.dat")), 16,
                          b'*', b'*')
        os.remove("".join((self.app_path,"config.tmp")))

    def load_config(self):
        if not os.path.isfile( "".join((self.app_path, "config.dat")) ):
            Log().local("Config file not exists")
            QtGui.QMessageBox.critical(self, 'Ошибка', 'Отсутствует файл конфигураций!', QtGui.QMessageBox.Yes)
            QtGui.QApplication.quit()
            return
        try:
            DES3_decrypt_file("".join((self.app_path,"config.dat")), "".join((self.app_path,"config.tmp")), 16,
                              b'*', b'*')

            f = open( "".join((self.app_path, "config.tmp")), "r")
            cfg = json.load(f)

            self.MDBServer = cfg["mdbserver"]
            self.MDBUser = cfg["mdbuser"]
            self.MDBPasswd = cfg["mdbpasswd"]
            self.TCPServer = cfg["tcpserver"]
            self.TCPPort = cfg["tcpport"]
            f.close()
            os.remove("".join((self.app_path,"config.tmp")))
        except:
            Log().local("Error reading config file")
            QtGui.QMessageBox.critical(self, 'Ошибка', 'Ошибка чтения конфигурационного файла!',
                                           QtGui.QMessageBox.Yes)

    def on_send_msg(self):
        try:
            send_msg(self, self.ui.teMsg.document().toPlainText(), False, self.passwd, self.ui.lbAlias.text())
        except:
            Log().local("Ошибка отправки сообщения")
            QtGui.QMessageBox.critical(self, 'Error', 'Ошибка отправки сообщения!', QtGui.QMessageBox.Yes)

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
                item = QtGui.QListWidgetItem()
                item.setIcon(QtGui.QIcon( "".join((self.app_path, "images/document_5907.png")) ))
                item.setText(f)
                self.ui.lwFiles.insertItem(0, item)