import json

file = open("friend_json.txt","r")
file_content = json.load(file) # reads file turm into dictionary
file.close()

print(file_content['friend'][0]['name'])

car =[
    {'make':'Ford','model':'Fiesta'},
    {'make':'Ford','model':'Focus'}
]

file_cars = open("cars_json.txt","w")
json.dump(car,file_cars)
file_cars.close()

json_string = '[{"make": "Ford", "model": "Fiesta"}]'

incorrect_cars = json.loads(json_string)
print(incorrect_cars)
print(incorrect_cars[0]['make'])