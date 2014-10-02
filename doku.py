#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Denisov Sergey 2014'

import sys
import os
from PyQt4 import QtGui
from login import LoginWindow
from main import MainWindow


def main():
    """
    Main function for start app
    """
    app = QtGui.QApplication(sys.argv)

    mw = MainWindow()
    mw.load_config()

    wlogin = LoginWindow()
    wlogin.set_wnds(mw)

    """
    Auto hide main window if key exists
    """
    if len(sys.argv) > 1:
        if sys.argv[1] == "-auto":
            wlogin.isAuto = True
        else:
            wlogin.isAuto = False
    else:
        wlogin.isAuto = False

    wlogin.show()
    app.exec_()


if __name__ == '__main__':
    main()
