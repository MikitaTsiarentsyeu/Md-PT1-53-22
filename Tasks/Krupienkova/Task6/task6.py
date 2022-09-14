# 1
def get_sum_elements(l):
    result = 0
    for n in l:
        if isinstance(n, int):
            result += n
        else:
            result += get_sum_elements(n)
    return result


print(get_sum_elements([1, 2, [2, 4, [[7, 8], 4, 6]]]))


# 2
def fib(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    numb_list = fib(n-1)
    numb_list.append(numb_list[-1] + numb_list[-2])
    return numb_list


print(fib(10))


