__author__ = 'sergey'

import watchWnd
from PyQt4 import QtGui
from PyQt4 import QtCore
from mariadb import MariaDB


class WatchWindow(QtGui.QWidget):
    def __init__(self):
        super(WatchWindow, self).__init__()
        self.ui = watchWnd.Ui_WatchWindow()
        self.ui.setupUi(self)

        """
        Setup wnd on screen center
        """
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        wid = QtGui.QDesktopWidget()
        screenWidth = wid.screen().width()
        screenHeight = wid.screen().height()
        self.setGeometry((screenWidth/2)-(width/2),(screenHeight/2)-(height/2),width,height)

        """
        Set table options
        """
        lst = list()
        lst.append("№")
        lst.append("Клиент")
        lst.append("Тип проблемы")
        lst.append("Дата")
        lst.append("Решение")
        self.ui.tw1.setHorizontalHeaderLabels(lst)
        self.ui.tw1.horizontalHeader().resizeSection(0, 30)
        self.ui.tw1.horizontalHeader().resizeSection(1, 70)
        self.ui.tw1.horizontalHeader().resizeSection(2, 330)
        self.ui.tw1.horizontalHeader().resizeSection(3, 100)

        self.MDBServer = "94.232.48.110"
        self.MDBUser = "doku"
        self.MDBPasswd = "School184"

        self.isRead = False

        self.tmr = QtCore.QTimer()
        QtCore.QObject.connect(self.tmr, QtCore.SIGNAL("timeout()"), self.get_tasks)
        self.tmr.start(5000)

    def get_tasks(self):
        self.ui.tw1.setRowCount(0)

        mdb = MariaDB()
        mdb.connect(self.MDBServer, self.MDBUser, self.MDBPasswd, "DokuMail")
        task_list = mdb.get_users_tasks()

        for task in task_list:
            self.ui.tw1.setRowCount(self.ui.tw1.rowCount() + 1)
            item = QtGui.QTableWidgetItem(task["id"])
            self.ui.tw1.setItem(self.ui.tw1.rowCount() - 1, 0, item)

            item = QtGui.QTableWidgetItem(task["name"])
            self.ui.tw1.setItem(self.ui.tw1.rowCount() - 1, 1, item)

            item = QtGui.QTableWidgetItem(task["type"])
            self.ui.tw1.setItem(self.ui.tw1.rowCount() - 1, 2, item)

            item = QtGui.QTableWidgetItem(task["date"])
            self.ui.tw1.setItem(self.ui.tw1.rowCount() - 1, 3, item)

            item = QtGui.QTableWidgetItem(task["status"])
            self.ui.tw1.setItem(self.ui.tw1.rowCount() - 1, 4, item)

        if mdb.get_signal():
            if not self.isRead:
                self.show()
                QtGui.QMessageBox.information(self, "Задачи DokuMail", "У вас есть нерешённые проблемы!",
                                          QtGui.QMessageBox.Yes)
                self.isRead = True
        mdb.close()