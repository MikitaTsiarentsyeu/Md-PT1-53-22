def test_sum(a, b):
    print(id(a), id(b))
    res = a + b
    return res

x = test_sum(3, 2)
print(x)

def test_print(x):
    print(x.upper())

x = test_print("my new function")
print(x)

print(type(test_print))

x, y = 555, 777
print(id(x), id(y))
test_sum(x, y)

def test_return(val):
    if val:
        return val

    print("the rest of the function goes here")

test_return(False)