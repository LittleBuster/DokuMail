def main():
	import platform
	if platform.system() == "Windows":
		import os
		import win32api
		os.chdir("..")
		win32api.ShellExecute(0, 'open', 'doku.exe', '', '', 1)

if __name__ == '__main__':
	main()