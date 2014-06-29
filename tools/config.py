def main():
	f = open("config.dat", "wb")
	cfg = "94.232.48.110$ssde$School184$"
	f.write(cfg.encode("utf-8"))
	f.close()

if __name__ == '__main__':
	main()
