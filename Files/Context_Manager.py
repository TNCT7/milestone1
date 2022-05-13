#Note : We can add vales in dictionary like Rolfs individual record,Jose individual record  but first we need to a that dictionary to list


# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:


import json

with open("csv_file.txt", "r") as File_Questions:
    File_Questions_Content = File_Questions.readlines()

#print(File_Questions_Content)

Data_altered = [file.strip() for file in File_Questions_Content]
#print(Data_altered)

Teams = []
counter = 0
for data in Data_altered:
    Loop_data = data.split(",")
    data_list = {
        'club': Loop_data[0],
        'city': Loop_data[1],
        'country': Loop_data[2]
    }
    Teams.append(data_list)

print(Teams)

with open("json_file.txt","w") as file_teams:
    json.dump(Teams,file_teams)


