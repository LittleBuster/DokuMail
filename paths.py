#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import getpass
import platform


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
            return os.path.join("/home", getpass.getuser(), "/")
        elif platform.system() == "Windows":
           return "./"

    def libs(self):
        return "/usr/lib/"