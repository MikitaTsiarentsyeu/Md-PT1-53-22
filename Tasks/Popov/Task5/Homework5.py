import string

def check_str(s):
    return (sum(map(s.count, string.ascii_uppercase)),
            sum(map(s.count, string.ascii_lowercase)))
u, l = check_str('The quick Brown Fox')
print("Upper case characters : {}\nLower case Characters : {}".format(u, l))


def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a
print(is_prime(int(input("Enter a number: "))))


def get_ranges(lst):
    start = end = None                
    new_list = []
    for i in lst:
        if start is None:
            start = end = i
        elif i == end or i == end + 1:
            end = i
        else:
            new_list.append((start, end))
            start = end = i
    if start is not None:
        new_list.append((start, end))
    return new_list
print(get_ranges([1,2,3,4,7,8,10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))