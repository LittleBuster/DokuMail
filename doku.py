__author__ = 'Denisov Sergey 2014'

import sys
from PyQt5 import QtWidgets
from tray import SystemTrayIcon
from login import LoginWindow
from main import MainWindow


def main():
	app = QtWidgets.QApplication(sys.argv)
	
	mw = MainWindow()
	mw.load_config()
	
	wlogin = LoginWindow()
	wlogin.set_wnds(mw)
	wlogin.show()
	
	app.exec_()

if __name__ == '__main__':
	main()
