import mysql.connector
class DbFixture:

    def __init__(self, host, database, user, passwd):
        self.host = host,
        self.database = database,
        self.user = user,
        self.passwd = passwd
        self.connection = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

    def destroy(self):
        self.connection.close()