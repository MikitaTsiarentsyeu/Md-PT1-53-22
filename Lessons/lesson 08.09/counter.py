
# def counter(n): DEPENDENT COUNTERS
#     global storage
#     storage = 0
#     def inner():
#         global storage
#         storage += 1
#         return n+storage
#     return inner

def counter(n):
    def inner():
        nonlocal n
        n += 1
        return n
    return inner

from_10 = counter(10)
from_100 = counter(100)

print(from_10())
print(from_10())
print(from_10())
print(from_100())
print(from_100())
print(from_100())
print(from_10())
print(from_10())
print(from_10())
print(from_100())
print(from_100())
print(from_100())