def my_func1():
    my_func2()
    print("hello from my func 1")

def my_func2():
    print("hello from my func 2")

my_func1()


# sign = '*'
# if sign == '+':
#     def func(a, b):
#         return a+b
# elif sign == '*':
#     def func(a, b):
#         return a*b  VERY BAD APPROACH


def func(a, b, sign):
    if sign == '+':
        return a+b
    elif sign == '*':
        return a*b

print(func(2, 3, '*'))


def check_int(x):
    print(id(x))
    x += 2
    print(id(x))
    return x

target_int = 5

print(id(target_int))
check_int(target_int)
print(id(target_int))
print(target_int)


def check_list(x):
    print(id(x))
    x[0] += 2
    print(id(x))
    return x

target_list = [5]

print(id(target_list))
check_list(target_list)
print(id(target_list))
print(target_list)


a = [3,2,5]
print(sorted(a))
print(a)
a.sort()
print(a)