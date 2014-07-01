import zlib
import os
import platform
from ctypes import cdll
from Crypto.Cipher import AES


class AES_KEY():
	key = b''
	key4 = b''

def AES256_cert_create( fname ):
	key = os.urandom(32)
	key4 = os.urandom(16)

	f = open(fname, "wb")
	f.write("-----BEGIN CERTIFICATE-----".encode("utf-8"))
	f.write(key)
	f.write(key4)
	f.write("-----END CERTIFICATE-----".encode("utf-8"))
	f.close()

def AES256_cert_read( fname ):
	a_key = AES_KEY()	

	f = open(fname, "rb")
	f.read(27)
	a_key.key = f.read(32)
	a_key.key4 = f.read(16)
	f.close()

	return a_key

def AES256_encode_file(filename, outfile, certFile):
	lib = None

	a_key = AES256_cert_read(certFile)

	if platform.system() == "Linux":
		lib = cdll.LoadLibrary("".join([(os.getcwd()), ("/libcrypt.so")]))
	else:
		lib = cdll.LoadLibrary("".join([(os.getcwd()), ("/libcrypt.dll")]))
	lib.do_crypt(filename.encode("utf-8"), outfile.encode("utf-8"), a_key.key, a_key.key4)

def AES256_decode_file(filename, outfile, certFile):
	lib = None

	a_key = AES256_cert_read(certFile)

	if platform.system() == "Linux":
		lib = cdll.LoadLibrary("".join([(os.getcwd()), ("/libcrypt.so")]))
	else:
		lib = cdll.LoadLibrary("".join([(os.getcwd()), ("/libcrypt.dll")]))
	lib.do_decrypt(filename.encode("utf-8"), outfile.encode("utf-8"), a_key.key, a_key.key4)

def AES256_encode_msg( message, certFile ):
	a_key = AES256_cert_read(certFile)

	obj = AES.new(a_key.key, AES.MODE_CBC, a_key.key4)
	l = len(message.encode("utf-8"))
	pl = 16 - divmod(l, 16)[1]
	
	while pl > 0:
		message = message + "|"
		pl = pl - 1
	
	ciphertext = obj.encrypt(message.encode("utf-8"))
	cdata = zlib.compress(ciphertext, 9)
	return cdata

def AES256_decode_msg( message, certFile ):
        a_key = AES256_cert_read(certFile)

        obj = AES.new(a_key.key, AES.MODE_CBC, a_key.key4)
        data = zlib.decompress(message)
        return obj.decrypt(data).decode("utf-8").split("|")[0]