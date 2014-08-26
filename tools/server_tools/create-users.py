import pymysql
import os
import random
import hashlib

dictionary = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
dict_sz = 62


def main():
    ip = input("MariaDB ip: ")
    uname = input("MariaDB user: ")
    upasswd = input("MariaDB passwd: ")

    while True:
        print("\n[1] Create many users\n[2] Create single user\n[3] Exit\n")
        cmd = input("#>")

        if cmd == "1":
            count = int(input("How many users create?"))

            """
            Start creation users
            """
            conn = pymysql.connect(host=ip, port=3306, user=uname, passwd=upasswd, db="DokuMail", charset='utf8')

            fpasswds = open("passwds.txt", "a")

            for i in range(1, count + 1):
                user_id = str(i + 10)
                user_name = "user" + str(i)
                user_alias = "Кабинет" + str(i)
                user_password = ""

                for j in range(0, 16):
                    user_password += dicttionary[random.randrange(0, 62)]

                fpasswds.write(user_name + " - " + user_password + "\n")

                h = hashlib.sha512()
                h.update(user_password.encode('utf-8'))
                user_hash = h.hexdigest().upper()

                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO users(id, name, password, priv, alias, enable) VALUES ('" + user_id + "','"
                    + user_name + "','" + user_hash + "','user','" + user_alias + "', '0' )")
                conn.commit()

                cur.execute(
                    "INSERT INTO actions(id, name, isFiles, isMsg, isUpdate) VALUES ('" + user_id + "','" + user_name
                    + "', '0', '0', '1')")
                conn.commit()

                print("User: " + user_name + " created.")

            print("Complete!")
            fpasswds.close()
            conn.close()

        if cmd == "2":
            conn = pymysql.connect(host=ip, port=3306, user=uname, passwd=upasswd, db="DokuMail", charset='utf8')

            fpasswds = open("passwds.txt", "a")
            user_id = input("User ID: ")
            user_name = input("User Login: ")
            user_alias = input("User Alias: ")
            user_priv = input("User privilegies user/admin: ")
            user_password = ""

            for j in range(0, 16):
                user_password += dicttionary[random.randrange(0, 62)]

            fpasswds.write(user_name + " - " + user_password + "\n")

            h = hashlib.sha512()
            h.update(user_password.encode('utf-8'))
            user_hash = h.hexdigest().upper()

            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users(id, name, password, priv, alias, enable) VALUES ('" + user_id + "','" + user_name
                + "','" + user_hash + "','" + user_priv + "','" + user_alias + "', '0' )")
            conn.commit()

            cur.execute(
                "INSERT INTO actions(id, name, isFiles, isMsg, isUpdate) VALUES ('" + user_id + "','" + user_name
                + "', '0', '0', '1')")
            conn.commit()

            print("User: " + user_name + " created.")
            fpasswds.close()
            conn.close()

        if cmd == "3":
            break
    print("Goodbye!")


if __name__ == '__main__':
    main()