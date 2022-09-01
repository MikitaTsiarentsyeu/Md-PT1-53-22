def sum(a, b, p):
    def sq(x):
        nonlocal b
        b = 10
        print(f"from sq - {b}")
        return x*x
    def pw(x, y):
        return x**y
    res = sq(a)+pw(b, p)
    print(f"from sum - {b}")
    return res

print(sum(2, 3, 3))