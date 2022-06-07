import re

data_string = 'tejas.nerurkar@gmail.com'
data_re = '[A-z\.]*'

List_data = re.findall(data_re,data_string)

user_id = List_data[0]
Domain_name = List_data[1]

print(List_data)

for ld in List_data:
    if ld != '':
        if ld.__contains__('.com'):
            print(f"Domain name : {ld}")
        else:
            print(f"User id : {ld}")


price = "Price : $18,204.02"
expression = "Price : \$([0-9\.,]*)"

List_price = re.search(expression,price)

print(List_price.group(0))
print(List_price.group(1))
fload_number = List_price.group(1)
fload_number = fload_number.replace(",","")

fload_number = float(fload_number)


print(type(fload_number))
print(fload_number)


# print(List_price.group(1))