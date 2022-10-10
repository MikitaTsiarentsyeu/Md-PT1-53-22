def sum1(lst):
    total = 0
    for element in lst:
        if (type(element) == type([])):
            total = total + sum1(element)
        else:
            total = total + element
    return total
print("Еhe sum of the elements is:", sum1([1, 2, [2, 4, [[7, 8], 4, 6]]]))

def f(n):
    if (n <= 1):
        return n
    else:
        return (f(n-1) + f(n-2))
n = int(input("Enter the number of members of the sequence:"))
print("Fibonacci sequence:")
for i in range(n):
    print(f(i))