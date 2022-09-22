def list_sum(l, res = 0):
    for i in l:
        res = res + i if not isinstance(i, list) else res + list_sum(i)
    return res         
l = [1, 2, [2, 4, [[7, 8, 6], 4, ]]]
print(list_sum(l))

def fib(x):
    if x == 1:
        return [1]
    elif x == 2:
        return [0,1]
    l = fib(x-1)
    l.append(l[-1] + l[-2])
    return l

print(fib(56))



