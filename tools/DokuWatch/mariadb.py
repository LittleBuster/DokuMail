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
        info = {}
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

        cur = self.conn.cursor()
        cur.execute("SELECT * FROM data")

        logList = []
        for row in cur:
            log = {}
            log["id"] = str(row[0])
            log["name"] = row[1]
            log["type"] = row[2]
            log["from"] = row[3]
            log["to"] = row[4]
            log["date"] = row[5]
            log["time"] = row[6]
            logList.append( log )

        info["tasks"] = taskList
        info["log"] = logList
        return info

    def get_current_task(self, task):
        cur = self.conn.cursor()
        cur.execute("SELECT task FROM tasks WHERE id='" + task["id"] + "' and name='" + task["name"]
                    + "' and typeTask='" + task["type"] + "'")
        for row in cur:
            return row[0]

    def set_status(self, task, value):
        cur = self.conn.cursor()
        cur.execute("UPDATE tasks SET status='" + value + "' WHERE id='" + task["id"] + "' and name='" + task["name"]
                    + "' and typeTask='" + task["type"] + "'")

        self.conn.commit()

    def get_signal(self):
        cur = self.conn.cursor()
        cur.execute("SELECT status FROM tasks WHERE status='Нет'")

        for row in cur:
            return True
        return False

    def clear_data(self):
        unused_users = []
        cur = self.conn.cursor()
        cur.execute("SELECT name FROM users WHERE enable='0'")
        for row in cur:
            unused_users.append(row[0])

        for user in unused_users:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM data WHERE toUsr='" + user + "'")
            self.conn.commit()
            print ("Delete to user" + user)

    def close(self):
        """
        Disconnect from database
        """
        self.conn.close()