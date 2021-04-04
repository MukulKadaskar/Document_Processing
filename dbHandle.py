import config
import sqlite3


def connectDB():
    return sqlite3.connect(config.DATABASE_NAME)


def authenticateUser(username, password):
    connection = connectDB()
    dbcursor = connection.cursor()
    userCount = dbcursor.execute(
        '''SELECT COUNT(*) from users WHERE username=? AND password=?''', (username, password)).fetchone()
    if userCount[0] > 0:
        config.CURRENT_USER=username
        return True
    else:
        return False
    connection.close()

def isLoggedIn():
    if config.CURRENT_USER != '':
        return True
    else:
        return False


if __name__ == '__main__':
    print(authenticateUser('pprathamesh98@gmail.com','qazwsxdc'))