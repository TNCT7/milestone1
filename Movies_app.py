Movies = [
{"Name":"KGF2" ,"Actor":"Yash", "Release":2022}
]

print("Welcome to Movie Collection!!")
choice = input("Please enter your choice a for add l for list & f for find: ")

while choice != 'q':
    if choice == 'a':
        movie_name = input("Enter movie name: ")
        movie_actor = input("Enter movie actor: ")
        movie_date = input("Enter movie release date: ")

        Movie_new = {
            "Name":movie_name ,"Actor":movie_actor, "Release":movie_date
        }
        Movies.append(Movie_new)
    elif choice == 'l':
        print(Movies)
    elif choice == 'f':
        fname = input("Enter movie name to be found: ")
        for movie in Movies:
            if fname.lower() == movie["Name"].lower():
                mname = movie["Name"]
                mactor = movie["Actor"]
                mdate = movie["Release"]
                print(f"Movie name is {mname} and actor is {mactor} & release date is {mdate}")
    elif choice == 'q':
        print("Quitting application")
        quit()
    else:
        print("Improper input please try again!!")
    choice = input("Please enter your choice a for add l for list & f for find: ")


