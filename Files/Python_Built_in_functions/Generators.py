
# Prime number function  without generator
# def Prime_number(bound):
#     for n in range(2,bound):
#         for x in (2,n):
#             if n%x == 0 and n!=x:
#                 print(f"{n} is divisible by {x} and is not a prime number")
#                 break
#             else:
#                 print(f"{n} is a prime number")
#                 break

# Prime number function  with generator
def Prime_number(bound):
    for n in range(2,bound):
        for x in (2,n):
            if n%x == 0 and n!=x:
                # print(f"{n} is divisible by {x} and is not a prime number")
                break
            else:
                yield n
                break

g = Prime_number(100)

print(next(g))
print(next(g))
print(next(g))
print(next(g))

