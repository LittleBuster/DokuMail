__author__ = 'sergey'

import pymysql


class MariaDB():
    def connect(self, ip, usr, pwd, database):
        """
        Connect to DokuMail SQL server
        """
        self.conn = None
        try:
            self.conn = pymysql.connect(host=ip, port=3306, user=usr, passwd=pwd, db=database, charset='utf8')
            return True
        except:
            return False

    def get_users_tasks(self):
        taskList = list()

        cur = self.conn.cursor()
        cur.execute("SELECT id,name,typeTask,dateTask,status FROM tasks")

        for row in cur:
            task = {}
            task["id"] = str(row[0])
            task["name"] = row[1]
            task["type"] = row[2]
            task["date"] = row[3]
            task["status"] = row[4]
            taskList.append(task)

        return taskList

    def get_signal(self):
        cur = self.conn.cursor()
        cur.execute("SELECT status FROM tasks WHERE status='Нет'")

        for row in cur:
            return True
        return False

    def close(self):
        """
        Disconnect from database
        """
        self.conn.close()