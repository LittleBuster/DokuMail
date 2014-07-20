#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import platform
from ctypes import cdll

def zlib_compress_file( filename, outfile ):
	lib = None

	if platform.system() == "Linux":
		lib = cdll.LoadLibrary("".join([(os.getcwd()), ("/libcompress.so")]))
	else:
		lib = cdll.LoadLibrary("".join([(os.getcwd()), ("/libcompress.dll")]))

	try:
		if platform.system() == "Linux": 
			lib.file_compress(filename.encode("utf-8"), outfile.encode("utf-8"))
		else:
			lib.file_compress(filename.encode("cp1251"), outfile.encode("cp1251"))
		return True
	except:
		return False

def zlib_decompress_file( filename, outfile ):
	lib = None

	if platform.system() == "Linux":
		lib = cdll.LoadLibrary("".join([(os.getcwd()), ("/libcompress.so")]))
	else:
		lib = cdll.LoadLibrary("".join([(os.getcwd()), ("/libcompress.dll")]))

	try:
		if platform.system() == "Linux":
			lib.file_decompress(filename.encode("utf-8"), outfile.encode("utf-8"))
		else:
			lib.file_decompress(filename.encode("cp1251"), outfile.encode("cp1251"))
		return True
	except:
		return False