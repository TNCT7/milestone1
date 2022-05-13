import database




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

        book_detail = {'book_name': book_name,'book_Author': book_Author,'book_Release': book_Release,'read': False}
        #obj_add = database.Database_Manipulate(book_detail)
        obj_add = database.Database_Manipulate()
        obj_add.Add(book_detail)

        user_choice = input("""
                Enter
                'a' for adding books
                'l' for listing books
                'd' for deleting books
                'f' for finding books
                'q' for quit

                Your Choice : """)

    elif user_choice == 'l':
        obj_list = database.Database_Manipulate()
        obj_list.List()

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

        obj_read = database.Database_Manipulate()
        obj_read.Read(book_read)

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

        obj_del = database.Database_Manipulate()
        obj_del.delete(book_del)

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