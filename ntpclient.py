import json
import socket
from configs import PacketHeader
from logger import Log
from paths import AppPath


class NtpClient(object):
    """
    Class for low-level communication with a NtpServer by socket
    """

    def __init__(self):
        super(NtpClient, self).__init__()
        self.app_path = AppPath().main()
        self.header = PacketHeader().header()

    def connect(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((ip, int(port)))
        except:
            Log().local("Ntp Client: error connection to server: " + ip)
            return False

    def get_datetime(self):
        data = {"header": self.header, "cmd": "get-datetime"}
        self.sock.send(json.dumps(data).encode("utf-8"))

        answ = self.sock.recv(1024).decode("utf-8")
        return json.loads(answ)

    def close(self):
        self.sock.close()