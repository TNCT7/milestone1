# class FirstIteration:
#     def __init__(self):
#         self.number = 0
#
#     def __next__(self):
#         if self.number <100:
#             current = self.number
#             self.number += 1
#             return current
#         else:
#             raise StopIteration()
#
#
#
# myval = FirstIteration()
# print(next(myval))
# print(next(myval))
# print(next(myval))
# print(next(myval))
# print(next(myval))
# print(myval)



# Define a PrimeGenerator class
class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop    # stop defines the range (exclusive upper bound) in which we search for the primes
        self.start = 2

    def __next__(self):
        for n in range(self.start, self.stop):
            for x in (2, n):
                if n % x == 0:
                    # print(f"{n} is divisible by {x} and is not a prime number")
                    break
                else:
                    self.start = n+1
                    return n



PG = PrimeGenerator(20)
print(next(PG))
print(next(PG))


