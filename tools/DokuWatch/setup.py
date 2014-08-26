import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'linux':
    base = 'Console'

setup(name = 'DokuMail',
      version = '0.0.1',
      executables = [Executable('main.py', base=base)],
      options = {'build_exe': {'includes': ['sip']}})
