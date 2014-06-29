__author__ = 'Denisov Sergey 2014'

import sys
from PyQt5 import QtWidgets
from tray import SystemTrayIcon
from login import LoginWindow
from main import MainWindow

import os
from ctypes import cdll

def main():
	#lib = cdll.LoadLibrary( "".join([(os.getcwd()), ("/libcrypt.so")]) )
	#lib.do_crypt("config.dat".encode("utf-8"), "config.crypt".encode("utf-8"))
	#lib.do_decrypt("config.crypt".encode('utf-8'), "config.decrypt".encode("utf-8"))

	app = QtWidgets.QApplication(sys.argv)
	
	mw = MainWindow()
	mw.load_config()
	
	wlogin = LoginWindow()
	wlogin.set_wnds(mw)
	wlogin.show()
	
	app.exec_()

if __name__ == '__main__':
	main()
