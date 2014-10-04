#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
import getpass
import platform


class pObj(object):
    """
    JSON temp class
    """
    pass

class AppPath():
    """
    Singleton class for set windows location parameters
    """

    def new(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance

    def main(self):
        if  platform.system() == "Linux":
            return os.path.join("/home", getpass.getuser(), ".doku/")
        elif platform.system() == "Windows":
           return "./"

    def home(self):
        if  platform.system() == "Linux":
            pth = "".join(("/home/", getpass.getuser(), "/"))
            return pth
        elif platform.system() == "Windows":
           return "./"

    def libs(self):
        return "/usr/lib/"