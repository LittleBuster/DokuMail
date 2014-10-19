#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime
import platform
from paths import AppPath


class Log():
    """
    Singleton class for loging app
    """

    def new(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance

    def local(self, text):
        """
        Create local log file or append info in exists
        """
        path = ""
        if platform.system() == "Linux":
            path = os.path.join(AppPath().main(), "log.txt")
        elif platform.system() == "Windows":
            path = "log.txt"

        logf = open(path, "a")
        date = datetime.datetime.now()
        logf.writelines("".join(("[", str(date), "] ", text, "\n")))
        logf.close()