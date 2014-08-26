#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import platform
from ctypes import cdll


def zlib_compress_file(filename, outfile):
    """
    Compress files by zlib alorithm.

    Call C-language dlls from python app

    If system linux - call .so libs, if Windows call .dll libs and change

    encoding to cp1251 for russian language.
    """
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


def zlib_decompress_file(filename, outfile):
    """
    Decompress files by zlib alorithm.

    Call C-language dlls from python app

    If system linux - call .so libs, if Windows call .dll libs and change

    encoding to cp1251 for russian language.
    """
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