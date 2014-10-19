#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import platform
from ctypes import cdll
from paths import AppPath


def zlib_compress_file(filename, outfile):
    """
    Compress files by zlib alorithm.

    Call C-language dlls from python app

    If system linux - call .so libs, if Windows call .dll libs and change

    encoding to cp1251 for russian language.
    """
    lib = None
    if platform.system() == "Linux":
        if not os.path.exists("".join((AppPath().libs(), "libcompress.so"))):
            return False

        lib = cdll.LoadLibrary("".join((AppPath().libs(), "libcompress.so")))

    elif platform.system() == "Windows":
        if not os.path.exists("".join([(os.getcwd()), ("/libcompress.dll")])):
            return False
        lib = cdll.LoadLibrary("".join([(os.getcwd()), ("/libcompress.dll")]))

    try:
        if platform.system() == "Linux":
            lib.file_compress(filename.encode("utf-8"), outfile.encode("utf-8"))
        elif platform.system() == "Windows":
            lib.file_compress(filename.encode("cp1251"), outfile.encode("cp1251"))
        return True
    except:
        return False


def zlib_decompress_file(filename, outfile):
    """
    Decompress files by zlib alorithm.

    Call C-language dlls from python app

    If system linux - call .so libs, if Windows call .dll libs and change

    encoding to cp1251 for russian language.
    """
    lib = None

    if platform.system() == "Linux":
        if not os.path.exists("".join((AppPath().libs(), "libcompress.so"))):
            return False
        lib = cdll.LoadLibrary("".join((AppPath().libs(), "libcompress.so")))

    elif platform.system() == "Windows":
        if not os.path.exists("".join([(os.getcwd()), ("/libcompress.dll")])):
            return False
        lib = cdll.LoadLibrary("".join([(os.getcwd()), ("/libcompress.dll")]))

    try:
        if platform.system() == "Linux":
            lib.file_decompress(filename.encode("utf-8"), outfile.encode("utf-8"))
        elif platform.system() == "Windows":
            lib.file_decompress(filename.encode("cp1251"), outfile.encode("cp1251"))
        return True
    except:
        return False