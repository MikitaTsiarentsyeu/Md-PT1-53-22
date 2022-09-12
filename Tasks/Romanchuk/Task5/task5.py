def check_str(s):
    upper = sum(1 for i in s if i.isupper())
    lower = sum(1 for i in s if i.islower())
    return f'{upper} upper case, {lower} lower case'


def is_prime(n):
    d = 2
    while d ** 2 <= n and n % d != 0:
        d += 1
    return d ** 2 > n


def get_ranges(l):
    start = [l[0]]
    end = []
    for i in range(0, len(l) - 1):
        if l[i + 1] - l[i] != 1:
            start.append(l[i + 1])
            end.append(l[i])
    end.append(l[len(l) - 1])
    return ', '.join([f'{start[i]}-{end[i]}' if start[i] != end[i] else f'{start[i]}' for i in range(len(start))])
