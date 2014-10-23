__author__ = 'sergey'
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime

LOG_WARNING = 100
LOG_CRITICAL = 101
LOG_INFO = 102


class Log():
    """
    Singleton class for loging app
    """

    def new(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance

    def local(self, user, text, type):
        """
        Create local log file or append info in exists
        """
        tp = ""
        float()
        if type == LOG_WARNING:
            tp = "warning"
        elif type == LOG_CRITICAL:
            tp = "critical"
        elif type == LOG_INFO:
            tp = "info"

        logf = open("log.txt", "a")
        date = str(datetime.datetime.now()).split(".")[0]
        txt = "".join(("[", date, "][", user, "][", tp, "]: ", text, "\n"))
        logf.writelines(txt)
        logf.close()

        print(txt.split("\n")[0])