def canonical_mult(a, b):
    res = 0
    if b < 0:
        a = -a
        b = -b
    for i in range(b):
        res += a
    return res


print(canonical_mult(2, 3))
print(canonical_mult(3, 2))
print(canonical_mult(-2, 3))
print(canonical_mult(2, -3))
print(canonical_mult(-2, -3))
print(canonical_mult(2, 0))
print(canonical_mult(0, 3))