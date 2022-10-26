def sum1(lst):
    total = 0
    for element in lst:
        if type(element) == type([]):
            total = total + sum1(element)
        else:
            total = total + element
    return total


def fib(n):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    fib_list = []
    for i in range(n):
        list.append(fibonacci(n - 1))
        n = n - 1
    fib_list.reverse()
    return fib_list
