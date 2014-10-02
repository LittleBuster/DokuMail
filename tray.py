#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore


class SystemTrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, mw, icon, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)

        self._mw = mw

        menu = QtGui.QMenu(parent)

        shAction = menu.addAction("Показать")
        shAction.setIcon(QtGui.QIcon("".join((self._mw.app_path, "images/cmp.ico"))))
        QtCore.QObject.connect(shAction, QtCore.SIGNAL("triggered()"), self.show_main)

        shAction2 = menu.addAction("О программе")
        shAction2.setIcon(QtGui.QIcon("".join((self._mw.app_path,"images/elena8d89.png"))))
        QtCore.QObject.connect(shAction2, QtCore.SIGNAL("triggered()"), self.show_about)

        shAction3 = menu.addAction("Выход")
        shAction3.setIcon(QtGui.QIcon("".join((self._mw.app_path, "images/exit.png"))))
        QtCore.QObject.connect(shAction3, QtCore.SIGNAL("triggered()"), self.close_app)

        self.setContextMenu(menu)
        QtCore.QObject.connect(self, QtCore.SIGNAL("activated()"), self.on_active)

    def on_active(self, reason):
        """
        If 1 click
        """
        if reason == 3:
            self._mw.show()

    def show_main(self):
        self._mw.show()

    def show_about(self):
        self._mw.show()
        self._mw.ui.stackedWidget.setCurrentIndex(5)

    def close_app(self):
        self._mw.show()
        result = QtGui.QMessageBox.question(self._mw, 'Закрытие', 'Вы действительно хотите выйти из программы?',
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                                QtGui.QMessageBox.No)
        if result == QtGui.QMessageBox.Yes:
            QtGui.QApplication.quit()
        else:
            self._mw.hide()
