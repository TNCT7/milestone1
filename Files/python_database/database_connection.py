import sqlite3

class database_conn:
    def __init__(self,file):
        self.connection = 'null'
        self.file = file

    def __enter__(self):
        self.connection = sqlite3.connect(self.file)
        return self.connection


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb or exc_type or exc_val:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
