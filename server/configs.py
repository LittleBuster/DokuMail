__author__ = 'sergey'
import json
from logger import *


class Configs:
    def load(self):
        try:
            f = open("config.cfg", "r")
            config = json.load(f)
            f.close()
            return config
        except:
            Log().local("SERVER", "Error of reading config file", LOG_CRITICAL)
            return {}


class PacketHeader(object):
    """
    Packets header for exchanging messaging between client and server
    """
    def new(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance

    def header(self):
        return "DokuMail 2.0 Header - p1.0.0"