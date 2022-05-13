
Input_friends = input("Enter friends in comma separated format")
Input_friends_List=Input_friends.split(",")

print(Input_friends_List)

File_Friends = open("Friends.txt","r")
File_Friends_Content = File_Friends.readlines()
File_Friends.close()

friends_altered = []
for friends in File_Friends_Content:
    if friends.find("\n") != -1:
        friends = friends.replace("\n", "")
        print(friends)
        friends_altered.append(friends)

print(friends_altered)

friends_altered_1 = set(friends_altered)
Input_friends_List_1 = set(Input_friends_List)


Close_friends=friends_altered_1.intersection(Input_friends_List_1)

File_Write = open("Nearby_Friends.txt","w")
counter = 1
for cfriend in Close_friends:
    if counter != len(Close_friends):
        File_Write.write(cfriend+"\n")
        counter=counter+1
    else:
        File_Write.write(cfriend)
File_Write.close()
