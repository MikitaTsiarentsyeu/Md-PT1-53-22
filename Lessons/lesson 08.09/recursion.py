def level1():
    print("level1 started")
    level2()
    print("level1 finished")

def level2():
    print("level2 started")
    level3()
    print("level2 finished")


def level3():
    print("level3 started")
    level4()
    print("level3 finished")


def level4():
    print("level4 started")
    print("level4 finished")


# level1()

def left():
    print("left")
    right()

def right():
    print("right")
    left()

# left()

def print_n_times(n):
    if n == 0:
        return
    print(n)
    print_n_times(n-1)

# print_n_times(5)

def print_n_times(n):
    while True:
        if n == 0:
            break
        print(n)
        n = n-1

# print_n_times(5)

# 1! = 1
# 2! = 1*2 = 2
# 3! = 1*2*3 = 6
# 4! = 1*2*3*4 = 24
# 5! = 1*2*3*4*5 = 120

def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

def factorial(n):
    print(n)
    if n <= 1:
        return 1
    c = factorial(n-1)
    print(c)
    return n*c

print(factorial(5))
# for i in range(1, 6):
#     print(factorial(i))


def digit_sum(n):
    if n == 0:
        return 0
    return (n%10)+digit_sum(n//10)
    # rem = n % 10
    # sum = digit_sum(n//10)
    # print(rem, sum)
    # return rem + sum

def digit_sum(n, i=0, res=0):
    n = str(n) if isinstance(n, int) else n
    if i == len(n):
        return res
    res += int(n[i])
    return digit_sum(n, i+1, res + int(n[i]))

print(digit_sum(12345))


