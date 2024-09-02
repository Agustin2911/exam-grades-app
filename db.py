import mysql.connector
class database:

    def __init__(self):
        self.base=mysql.connector.connect(
            host="host",
            user="user",
            password="password",
            database="db",
            port="3306",
            auth_plugin='mysql_native_password'
        )
        self.cursor=self.base.cursor()

    def cerrar(self):
        self.cursor.close()
        self.base.close()
    
    def getCursor(self):
        return self.cursor
    
    def getBase(self):
        return self.base
    
    