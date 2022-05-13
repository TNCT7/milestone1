File = open("csv_data.txt","r")
File_Content = File.readlines()
File.close()
print(File_Content)


File_Content=[lines.strip() for lines in File_Content[1:]]

print(File_Content)

for data in File_Content:
     person_data=data.split(",")
     name = person_data[0].title()
     Age = person_data[1]
     University = person_data[2].title()
     Degree = person_data[3].capitalize()

     print(f'{name} of {Age} is studying {Degree} in {University}')

     csv_data = ",".join([name,Age,University,Degree])
     print(csv_data)
