import unittest
from compress import *


class CompressTest(unittest.TestCase):
    def setUp(self):
        self.fdata = "Тестовый файл"

    def test_file(self):
        f = open("test.txt", "w")
        f.writelines( self.fdata )
        f.close()

        zlib_compress_file("test.txt", "test.z")
        zlib_decompress_file("test.z", "test2.txt")

        f = open("test2.txt", "r")
        result = f.readline()
        f.close()

        os.remove("test.txt")
        os.remove("test2.txt")
        os.remove("test.z")

        self.assertEqual(self.fdata, result)

    def tearDown(self):
        del self.fdata

if __name__ == "__main__":
    unittest.main()