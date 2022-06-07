Movies =[
    {"name":"Avengers Infinity War","Director":"Ruso"},
    {"name":"Avengers Endgame","Director":"Ruso"},
    {"name":"Captain America","Director":"Marvels"},
    {"name":"Spider man","Director":"Sony"}
]

def Movie_details_finder(expected_val, finder):
    Movie_list = []
    for mov in Movies:
        # if expected_val == finder(mov):
        if finder(mov) == expected_val:
            Movie_list.append(mov)

    return Movie_list

looking_for_property = input("Propperty type? ")
looking_for_value = input("Detailed name? ")


val = Movie_details_finder(looking_for_value,lambda movie : movie[looking_for_property])

print(val or "Wrong movie details")