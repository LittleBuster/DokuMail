__author__ = 'Denisov Sergey (C) 2014'

import sys
from PyQt4 import QtGui
from watch import WatchWindow

def main():
    """
    Main App function
    """
    app = QtGui.QApplication(sys.argv)

    w = WatchWindow()
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()