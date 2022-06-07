import sqlite3
from database_connection import database_conn
Books = 'books.txt'


def create_book_table():
    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()

    with database_conn('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS BOOKS(name text primary key,author text,read integer)')



    # connection.commit()
    # connection.close()

def Add(name,author):
    with database_conn('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO BOOKS VALUES(?,?,0)",(name,author))


def List():
    with database_conn('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM BOOKS")
        book = [{"name":row[0],"author":row[1],"read":row[2]} for row in cursor.fetchall()]
    return book

def Read(bread):

    with database_conn('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE BOOKS SET read=1 WHERE name=?",(bread,))






def delete(dbook):
    with database_conn('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM BOOKS WHERE name=?", (dbook,))
