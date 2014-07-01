import os
import platform
from ctypes import cdll

def zlib_compress_file( filenme, outfile ):
	lib = None

	if platform.system() == "Linux":
		lib = cdll.LoadLibrary("".join([(os.getcwd()), ("/libcompress.so")]))
	else:
		lib = cdll.LoadLibrary("".join([(os.getcwd()), ("/libcompress.dll")]))

	try:
		lib.compress_file(filename.encode("utf-8"), outfile.encode("utf-8"))
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
		lib.decompress_file(filename.encode("utf-8"), outfile.encode("utf-8"))
		return True
	except:
		return False