import sqlite3
Books = 'books.txt'



def Add(name,author,release):
    with open(Books, "a") as File:
        File.write(f'{name},{author},{release},0\n')


def List():
    with open(Books, "r") as File:
        fdatas = [fdata.strip().split(',') for fdata in File.readlines()]
        return [
            {'name':fdin[0],'author':fdin[1],'read':fdin[2]}
            for fdin in fdatas
        ]


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

