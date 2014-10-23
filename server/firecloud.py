__author__ = 'sergey'
from ntpclient import NtpClient
from logger import *
from mediafire import MediaFireClient


class MediaFire():
    client = None
    cfg = {}

    def set_config(self, cfg):
        self.cfg = cfg

    def connect(self, login, pwd, id):
        self.client = MediaFireClient()
        self.client.login(email=login, password=pwd, app_id=id)

    def upload_msg(self, path):
        try:
            self.client.create_folder("mediafire:/Messages/")
        except:
            pass

        answ = {}
        try:
            ntp = NtpClient()
            ntp.connect(self.cfg["NtpServer"]["ip"], self.cfg["NtpServer"]["port"])
            answ = ntp.get_datetime()
            ntp.close()
        except:
            Log().local("NTP", "Could not connect to NTP server", LOG_CRITICAL)
            return

        try:
            self.client.create_folder("mediafire:/Messages/" + answ["date"] + "/")
        except:
            pass

        try:
            self.client.upload_file(path, "mediafire:/Messages/" + answ["date"] + "/")
        except:
            Log().local("MEDIAFIRE", "Error upload message.", LOG_CRITICAL)
            return