#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime
import platform


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
            path = "log.txt"

        logf = open(path, "a")
        date = datetime.datetime.now()
        txt = "".join(("[", str(date), "] ", text, "\n"))
        logf.writelines(txt)
        logf.close()
        print(txt.split("\n")[0])
