import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(name = 'spamandeggs',
      version = '0.0.1',
      executables = [Executable('usde.pyw', base=base)],
      options = {'build_exe': {'includes': ['sip']}})