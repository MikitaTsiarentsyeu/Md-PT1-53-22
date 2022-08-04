x = 10

if x == 0 or x == 1:
    print("the value is zero or one")
    if x == 0:
        print("the value is zero")
    else:
        print("the value is one")

if x == 0:
    print("the value is zero")
elif x == 1:
    print("the value is one")
elif x == 2:
    print("the value is two")
elif x == 3:
    print("the value is three")
else:
    print("I don't know")

x = -3

if x >= 0:
    if x == 0:
        print("the value is zero")
    else:
        print("the value is positive")
else:
    print("the value is negative")


if x == 0:
    print("the value is zero")
elif x > 0:
    print("the value is positive")
else:
    print("the value is negative")


if True:
    print("some logic")
    print("some logic")
    print("some logic")
    print("some logic")


print("it's true") if True else print("it's not")
val = "it's true" if True else "it's not"
print("it's true" if True else "it's not")
print(val)


print("it's positive") if x > 0 else print("it's zero") if x == 0 else print("it's negative")