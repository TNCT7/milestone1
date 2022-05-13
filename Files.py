File_Open = open("data.txt","r")
File_Content = File_Open.read()
File_Open.close()

print(File_Content)

userdetails = input("Enter details : ")
File_Write = open("data.txt","w")
File_Write.write(userdetails)
File_Write.close()