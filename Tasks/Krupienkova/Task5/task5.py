#1
def check_str(str):
    count_upper = 0
    count_lower = 0
    for i in str:
        if i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
    return f'{count_upper} upper case, {count_lower} lower case'

print(check_str('The quick Brown Fox'))

#2
def is_prime(numb):
    for i in range(2, int(numb**0.5)+1):
        if numb % i == 0:
            return False
    return True

print(is_prime(787))
print(is_prime(777))

#3
def get_ranges(l):
    ranges = [[l[0], l[0]]]
    for i in range(1, len(l)):
        if l[i] - l[i-1] == 1:
            ranges[-1][1] = l[i]
        else:
            ranges.append([l[i], l[i]])
    return ', '.join(f'{begin}' if begin == end else f'{begin}-{end}' for begin, end in ranges)

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))
