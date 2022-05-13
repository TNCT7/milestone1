import addition


print("Enter choice 1.Add 2.Sub 3.Mul 4.Div 5.Exit")

choice = input("Enter choice ")
while choice != "Exit":
    if choice == "Add":
        object = addition.Addition()
        list_add = ["2", "3", "4", "5", "6"]
        print(object.add(list_add))
    elif choice == "Sub":
        print(object.sub(4, -2))
    elif choice == "Mul":
        print(object.mul(4, 2))
    elif choice == "Div":
        print(object.div(4,2))
    elif choice == "Exit":
        exit()
    print("Enter choice 1.Add 2.Sub 3.Mul 4.Div 5.Exit")
    choice = input("Enter choice ")








