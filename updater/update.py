import os
import platform
import datetime
import shutil


class Log():
	"""
	Singleton class for loging updater
	"""
	def new(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Singleton, cls).__new__(cls)
			return cls.instance

	def local(self, text):
		"""
		Create local log file or append info in exists
		"""
		logf = open("update_log.txt", "a")
		date = datetime.datetime.now()
		logf.writelines("[" + str(date) + "] " + text + "\n")
		logf.close()


def start_doku():
	if platform.system() == "Windows":
		import win32api
		os.chdir("..")
		win32api.ShellExecute(0, 'open', 'doku.exe', '', '', 1)


def main():
	op_list = []

	try:
		f = open("data/doku_update.cfg", "r")
		while True:
			line = f.readline()
			if line == "":
				break
			else:
				op_list.append(line.split("\n")[0])
		f.close()
	except:
		Log().local("Error reading operations")

	print(str(len(op_list)) + " operations.")

	for action in op_list:
		op = action.split("$")

		if op[0] == "cd":
			try:
				os.chdir(op[1])
			except:
				Log().local("Error change directory " + op[1])

		if op[0] == "copy":
			try:
				print("Copy from " + op[1] + " to " + op[2])
				shutil.copy2(op[1], op[2])
			except:
				Log().local("Error copy file " + op[1])

		if op[0] == "rm":
			try:
				print("Remove " + op[1])
				os.remove(op[1])
			except:
				Log().local("Error remove file " + op[1])

		if op[0] == "exec":
			if platform.system() == "Windows":
				import win32api
				win32api.ShellExecute(0, 'open', op[1], '', '', 1)

		if op[0] == "mkdir":
			try:
				print("Make new dir: " + op[1])
				os.makedirs(op[1])
			except:
				Log().local("Error make dir " + op[1])

	start_doku()

if __name__ == '__main__':
	main()