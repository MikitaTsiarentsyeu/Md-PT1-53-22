def times(a, b):
    return a*b

print(times(2, 3))
print(times([2], 3))
print(times('[2]', 3))


def times_for_int(a:int, b:int) -> int:
    "this is a function that wil multiply two int numbers"
    if isinstance(a, int) and isinstance(b, int):
        return a*b

times_for_int('str', [0])

[1,2,3] == [3,2,1]

def eq(c1, c2):
    for i in c1:
        if i not in c2:
            return False
    for i in c2:
        if i not in c1:
            return False
    return True

print(eq([1,2,3],(3,2,1)))
print(eq(["1","2","3"],"321"))


# def sum(a, b):
#     return a+b

# def sum(a, b, c):
#     return sum(sum(a, b), c)