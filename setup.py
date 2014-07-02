import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(name = 'DokuMail',
      version = '0.0.1',
      executables = [Executable('doku.py', base=base)],
      options = {'build_exe': {'includes': ['sip']}})
