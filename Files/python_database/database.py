
Books = []

class Database_Manipulate():
    #def __init__(self,book_details):
        #self.book_details = book_details

    def Add(self,book_details):
        Books.append(book_details)


    def List(self):
        print(Books)

    def Read(self,bread):
        for book in range(len(Books)):
            if bread == Books[book]['book_name']:
                Books[book]['read'] = True

    def delete(self,dbook):
        for book in range(len(Books)):
            if dbook == Books[book]['book_name']:
                del Books[book]

