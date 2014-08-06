import json

class pObj(object):
	"""
	JSON temp class
	"""
	pass

def main():
	MDBServer = input("MariaDB Server: ")
	MDBUser = input("MariaDB User: ")
	MDBPasswd = input("MariaDB Password: ")
	TCPServer = input("TCP Server: ")
	TCPPort = input("TCP Port:")

	print("Writing configs...")
	f = open("config.dat", "w")
	cfg = pObj()
	cfg.config = {}
	cfg.config["mdbserver"] = MDBServer
	cfg.config["mdbuser"] = MDBUser
	cfg.config["mdbpasswd"] = MDBPasswd
	cfg.config["tcpserver"] = TCPServer
	cfg.config["tcpport"] = TCPPort
	json.dump(cfg.config, f)
	f.close()
	print("Complete.")

if __name__ == '__main__':
	main()
