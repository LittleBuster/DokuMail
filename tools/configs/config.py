import json
from crypt import *


class pObj(object):
    """
    JSON temp class
    """
    pass

def main():
    MDBUser = input("MariaDB User: ")
    MDBPasswd = input("MariaDB Password: ")

    cred = {}
    cred["login"] = MDBUser
    cred["password"] = MDBPasswd

    print("Writing configs...")
    f = open("servercred.tmp", "w")
    cfg = pObj()
    cfg.config = {}
    cfg.config["MariaDB"] = cred

    print(cfg.config)
    json.dump(cfg.config, f)
    f.close()

    DES3_encrypt_file("servercred.tmp", "servercred.dat", 16, b'1w1RTH2yaFIxk47D', b'4srgJfVo')
    os.remove("servercred.tmp")
    print("Complete.")

if __name__ == '__main__':
    main()
