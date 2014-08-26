#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime


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
        logf = open("log.txt", "a")
        date = datetime.datetime.now()
        logf.writelines("[" + str(date) + "] " + text + "\n")
        logf.close()