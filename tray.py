import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
	def __init__(self, mw):
		super(SystemTrayIcon, self).__init__(QtGui.QIcon("images/cmp16.ico"))
		self._mw = mw

		menu = QtWidgets.QMenu()
		
		shAction = menu.addAction("Показать")
		shAction.setIcon(QtGui.QIcon("images/cmp.ico"))
		shAction.triggered.connect(self.show_main)

		shAction2 = menu.addAction("О программе")
		shAction2.setIcon(QtGui.QIcon("images/elena8d89.png"))
		shAction2.triggered.connect(self.show_about)

		shAction3 = menu.addAction("Выход")
		shAction3.setIcon(QtGui.QIcon("images/exit.png"))
		shAction3.triggered.connect(self.close_app)

		self.setContextMenu(menu)
		self.show()

	def show_main(self):
		self._mw.show()

	def show_about(self):
		None

	def close_app(self):
		sys.exit()
