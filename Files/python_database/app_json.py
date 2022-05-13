import database_json




user_choice = input("""
Enter
'a' for adding books
'l' for listing books
'd' for deleting books
'f' for finding books
'q' for quit

Your Choice : """)

while user_choice != 'q':
    if user_choice == 'a':
        book_name = input("Enter book name : ")
        book_Author = input("Enter book Author : ")
        book_Release = input("Enter book Release date : ")

        # book_detail = {'book_name': book_name,'book_Author': book_Author,'book_Release': book_Release,'read': False}
        #obj_add = database.Database_Manipulate(book_detail)

        database_json.Add(book_name,book_Author,book_Release)

        user_choice = input("""
                Enter
                'a' for adding books
                'l' for listing books
                'd' for deleting books
                'f' for finding books
                'q' for quit

                Your Choice : """)

    elif user_choice == 'l':

        print(database_json.List())

        user_choice = input("""
        Enter
        'a' for adding books
        'l' for listing books
        'd' for deleting books
        'f' for finding books
        'q' for quit

        Your Choice : """)

    elif user_choice == 'r':
        book_read = input("Enter book name : ")


        database_json.Read(book_read)

        user_choice = input("""
        Enter
        'a' for adding books
        'l' for listing books
        'd' for deleting books
        'f' for finding books
        'q' for quit

        Your Choice : """)

    elif user_choice == 'd':
        book_del = input("Enter book name to be deleted : ")


        database_json.delete(book_del)

        user_choice = input("""
        Enter
        'a' for adding books
        'l' for listing books
        'd' for deleting books
        'f' for finding books
        'q' for quit

        Your Choice : """)

    elif user_choice == 'q':
        exit()

    else:
        print("Invalid choice Please try again!")
        user_choice = input("""
                Enter
                'a' for adding books
                'l' for listing books
                'd' for deleting books
                'f' for finding books
                'q' for quit

                Your Choice : """)