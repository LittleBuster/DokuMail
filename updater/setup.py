import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'console'

setup(name = 'DokuMail Updater',
      version = '0.0.1',
      executables = [Executable('update.py', icon='update.ico', base=base)],
      options = {'build_exe': {'includes': ['sip']}})
