def find_in(data,expected):
    for i in data:
        if i == expected:
            return f"{expected} found"
    raise Nodatafounderror(f"{expected} NOT found")

class Nodatafounderror(Exception):
    pass


print(__name__)
