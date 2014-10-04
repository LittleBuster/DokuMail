#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import random
import platform
from keys import AppKeys
from ctypes import cdll
from paths import AppPath
from Crypto.Cipher import AES
from Crypto.Cipher import DES3


class AES_KEY():
    """
    This class include 256 bit key and
    128 bit key IV4 for aes encrypting
    """
    key = b''
    key4 = b''


def DES3_encrypt_file(in_filename, out_filename, chunk_size, key, iv):
    des3 = DES3.new(key, DES3.MODE_CFB, iv)

    with open(in_filename, 'r') as in_file:
        with open(out_filename, 'wb') as out_file:
            while True:
                chunk = str(in_file.read(chunk_size))
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                out_file.write(des3.encrypt(chunk))


def DES3_decrypt_file(in_filename, out_filename, chunk_size, key, iv):
    des3 = DES3.new(key, DES3.MODE_CFB, iv)

    with open(in_filename, 'rb') as in_file:
        with open(out_filename, 'wb') as out_file:
            while True:
                chunk = in_file.read(chunk_size)
                if len(chunk) == 0:
                    break
                out_file.write(des3.decrypt(chunk))


def AES256_cert_create(fname):
    """
    This function create key file on disk, which
    include 256 bit aes random key and 128 bit
    aes IV4 random key and proect by 3DES
    """
    dictionary = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    key = ""
    key4 = ""

    for j in range(0, 32):
        key += dictionary[random.randrange(0, 62)]

    for j in range(0, 16):
        key += dictionary[random.randrange(0, 62)]

    f = open("".join((fname, ".tmp")), "w")
    f.write("-----BEGIN CERTIFICATE-----")
    f.write(key)
    f.write(key4)
    f.write("-----END CERTIFICATE-----")
    f.close()

    DES3_encrypt_file("".join((fname, ".tmp")), fname, 16, AppKeys().get_cert_key()["key"],
                      AppKeys().get_cert_key()["IV"])
    os.remove("".join((fname, ".tmp")))


def AES256_cert_read(fname):
    """
    This function read from disk file, which
    include 256 bit aes random key and 128 bit
    """
    DES3_decrypt_file(fname, "".join((fname, ".tmp")), 16, AppKeys().get_cert_key()["key"],
                      AppKeys().get_cert_key()["IV"])

    a_key = AES_KEY()

    f = open("".join((fname, ".tmp")), "rb")
    f.read(27)
    a_key.key = f.read(32)
    a_key.key4 = f.read(16)
    f.close()
    os.remove("".join((fname, ".tmp")))

    return a_key


def AES256_encode_file(filename, outfile, certFile):
    """
    This function encrypt files by aes256 alorithm.

    Call C-language dlls from python app

    If system linux - call .so libs, if Windows call .dll libs and change
    """
    lib = None

    a_key = AES256_cert_read(certFile)

    if platform.system() == "Linux":
        if not os.path.exists("".join((AppPath().libs(), "libcrypt.so"))):
            return False
        lib = cdll.LoadLibrary("".join((AppPath().libs(), "libcrypt.so")))
    elif platform.system() == "Windows":
        if not os.path.exists("".join([(os.getcwd()), ("\libcrypt.dll")])):
            return False
        lib = cdll.LoadLibrary("".join([(os.getcwd()), ("\libcrypt.dll")]))

    try:
        if platform.system() == "Linux":
            lib.do_crypt(filename.encode("utf-8"), outfile.encode("utf-8"), a_key.key, a_key.key4)
        elif platform.system() == "Windows":
            lib.do_crypt(filename.encode("cp1251"), outfile.encode("cp1251"), a_key.key, a_key.key4)
        return True
    except:
        return False


def AES256_decode_file(filename, outfile, certFile):
    """
    This function decrypt files by aes256 alorithm.

    Call C-language dlls from python app

    If system linux - call .so libs, if Windows call .dll libs and change
    encoding to cp1251 for russian language.
    """
    lib = None

    a_key = AES256_cert_read(certFile)

    if platform.system() == "Linux":
        lib = cdll.LoadLibrary("".join((AppPath().libs(), "libcrypt.so")))
    elif platform.system() == "Windows":
        lib = cdll.LoadLibrary("".join([(os.getcwd()), ("\libcrypt.dll")]))

    try:
        if platform.system() == "Linux":
            lib.do_decrypt(filename.encode("utf-8"), outfile.encode("utf-8"), a_key.key, a_key.key4)
        elif platform.system() == "Windows":
            lib.do_decrypt(filename.encode("cp1251"), outfile.encode("cp1251"), a_key.key, a_key.key4)
        return True
    except:
        return False


def AES256_encode_msg(message, certFile):
    """
    This function is used for encrypting messages,
    which send on server
    """
    a_key = AES256_cert_read(certFile)

    obj = AES.new(a_key.key, AES.MODE_CBC, a_key.key4)
    l = len(message.encode("utf-8"))
    pl = 16 - divmod(l, 16)[1]

    while pl > 0:
        message = message + "|"
        pl = pl - 1

    ciphertext = obj.encrypt(message.encode("utf-8"))
    return ciphertext


def AES256_decode_msg(binarr, certFile):
    """
    This function is used for encrypting messages,
    """
    a_key = AES256_cert_read(certFile)
    obj = AES.new(a_key.key, AES.MODE_CBC, a_key.key4)
    return obj.decrypt(binarr).decode("utf-8").split("|")[0]