__author__ = 'sergey'
import unittest
import configs
from PyQt4 import QtGui
import sys


class ConfigsTest(unittest.TestCase):
    def setUp(self):
        self.app = QtGui.QApplication(sys.argv)
        self.path = "../config.cfg"

    def test_load(self):
        cfg = configs.Configs(self.path)
        self.assertNotEqual(cfg, {})

        isOk = True
        lst = []
        try:
            lst.append(cfg.cfg["MariaDB"])
            lst.append(cfg.cfg["TcpServer"])
            lst.append(cfg.cfg["DownloadsPath"])
            lst.append(cfg.cfg["FileManagers"])
            lst.append(cfg.cfg["UnzipFormats"])
            lst.append(cfg.cfg["UncryptFormats"])

            for item in lst:
                if item == "":
                    isOk = False
                    break
        except:
            isOk = False

        self.assertTrue(isOk)

    def tearDown(self):
        del self.path
        del self.app

if __name__ == "__main__":
    unittest.main()