import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == 'linux':
	base = 'Console'

setup(name = 'DokuMail',
version = '1.0.1',
executables = [Executable('dokuserver.py', base=base)])
