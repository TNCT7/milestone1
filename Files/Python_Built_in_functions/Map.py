friends = ['Tejas','David','Tanmai','Akshay']

def start_T(friend):
    if friend.startswith("T"):
        return friend


starts_with_T = map(start_T,friends)
# lambda a : a + 10
# starts_with_T = map(lambda friend : friend.startswith("T"),friends)


# Generator comprehension which i similar to list comprehension only [] is replaced with ()
another_starts_with_T = (friend.lower() for friend in friends if friend.startswith("T"))

print(next(starts_with_T))
print(next(starts_with_T))
print(next(starts_with_T))
print(next(starts_with_T))

print(next(another_starts_with_T))
print(next(another_starts_with_T))