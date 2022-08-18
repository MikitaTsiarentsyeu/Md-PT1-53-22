# FIZZ BUZZ

"""Вывести на экран числа от 1 до 100. 
Если число кратно 3, то вместо него вывести FIZZ.
Если число кратно 5, то вместо него вывести BUZZ.
Если число кратно и 3, и 5, то вместо него вывести FIZZBUZZ.
"""

for x in range(1, 101):
    # fizz = "FIZZ" if x % 3 == 0 else ""
    # buzz = "BUZZ" if x % 5 == 0 else ""
    # print(f"{fizz}{buzz}" or x)
    print(("FIZZ"*(x % 3 == 0) + "BUZZ"*(x % 5 == 0)) or x)

[print(("FIZZ"*(x % 3 == 0) + "BUZZ"*(x % 5 == 0)) or x) for x in range(1, 101)]