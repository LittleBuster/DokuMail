#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Denisov Sergey 2014'

import sys
from PyQt5 import QtWidgets
from login import LoginWindow
from main import MainWindow


def main():
	"""
	Main function for start app
	"""
	app = QtWidgets.QApplication(sys.argv)

	mw = MainWindow()
	mw.load_config()
	
	wlogin = LoginWindow()
	wlogin.set_wnds(mw)
	wlogin.show()
	
	app.exec_()

if __name__ == '__main__':
	main()
