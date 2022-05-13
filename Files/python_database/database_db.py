import sqlite3
Books = 'books.txt'


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS BOOKS(name text primary key,author text,read integer)')
    connection.commit()
    connection.close()

def Add(name,author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO BOOKS VALUES(?,?,0)",(name,author))
    connection.commit()
    connection.close()


def List():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM BOOKS")
    connection.commit()
    connection.close()


def Read(bread):
    getbooks = List()
    #Trainers solution
    # for book in getbooks:
    #     if bread == book['name']:
    #         book['read'] = '1'
    # _save_all_books(getbooks)

    #My solution
    for book in getbooks:
        if bread == book['name']:
            book['read'] = '1'
            _save_all_books(getbooks)
        else:
            _save_all_books(getbooks)


def _save_all_books(getbooks):
    with open(Books,'w') as File:
        for book in getbooks:
            File.write(f"{book['name']},{book['author']},{book['read']}\n")



def delete(dbook):
    getbooks = List()
    with open(Books, 'w') as File1:
        pass
    for book in getbooks:
        if dbook != book['name']:
            with open(Books, 'a') as File:
                File.write(f"{book['name']},{book['author']},{book['read']}\n")

