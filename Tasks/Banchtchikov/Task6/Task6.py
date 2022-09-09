def sum_numbers(n, sum = 0):
    for i in range(len(n)):
        sum = sum + n[i] if isinstance(n[i], int) else sum_numbers(n[i], sum)   
    return sum

print(sum_numbers([1,4,5,6,[1,2,2,[4,11,15],5,8],11]))



def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(1,6):
    print(f"{i} : {fibonacci(i)}")
