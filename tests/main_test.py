import unittest
from test_crypto import CryptoTest
from test_compress import CompressTest
from test_configs import ConfigsTest
from test_login import LoginTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(CryptoTest))
    suite.addTest(unittest.makeSuite(CompressTest))
    suite.addTest(unittest.makeSuite(ConfigsTest))
    suite.addTest(unittest.makeSuite(LoginTest))


if __name__ == "__main__":
    unittest.main()