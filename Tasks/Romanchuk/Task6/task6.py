def sum_list(l):
    return sum(sum_list(i) if isinstance(i, list) else i for i in l)

def fib(n):
    cache = {}
    def fib_rec(n):
        if n == 1 or n == 2:
            cache[n] = n - 1
        elif n not in cache:
            cache[n] = fib_rec(n - 1) + fib_rec(n - 2)
        return cache[n]
    fib_rec(n)
    for i in range(1, len(cache) + 1):
        print(cache[i])

