friends = ['Tejas','David','Tanmai','Akshay']

def start_T(friend):
    return friend.startswith("T")


starts_with_T = filter(start_T,friends)
# lambda a : a + 10
# starts_with_T = filter(lambda friend : friend.startswith('T'),friends)


# Generator comprehension which i similar to list comprehension only [] is replaced with ()
another_starts_with_T = (friend for friend in friends if friend.startswith('T'))

print(next(starts_with_T))
print(next(starts_with_T))

print(next(another_starts_with_T))
print(next(another_starts_with_T))