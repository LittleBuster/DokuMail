__author__ = 'sergey'
from crypt import *
import unittest


class CryptoTest(unittest.TestCase):
    def setUp(self):
        self.msg = "Тестовое сообщение"
        self.fdata = "Тестовый файл"
        self.key = AES256_cert_read("../transf.crt")

    def test_readkey(self):
        res = False

        if (type(self.key.key) == bytes) and (len(self.key.key) == 32):
            if (type(self.key.key4) == bytes) and (len(self.key.key4) == 16):
                res = True

        self.assertTrue(res)

    def test_message(self):
        binarr = AES256_encode_msg(self.msg, self.key)
        message = AES256_decode_msg(binarr, self.key)
        self.assertEqual(message, self.msg)

    def test_file(self):
        f = open("test.txt", "w")
        f.writelines( self.fdata )
        f.close()

        AES256_encode_file("test.txt", "test.bin", self.key)
        AES256_decode_file("test.bin", "test2.txt", self.key)

        f = open("test2.txt", "r")
        result = f.readline()
        f.close()

        os.remove("test.txt")
        os.remove("test2.txt")
        os.remove("test.bin")

        self.assertEqual(self.fdata, result)

    def tearDown(self):
        del self.msg
        del self.key
        del self.fdata

if __name__ == "__main__":
    unittest.main()