"""1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
2. Написать рекурсивную функцию для вычисления n первых чисел Фибоначчи."""


def total_sum(l, sum=0): 
    for i in range(len(l)):
        if isinstance(l[i], int):
            sum = sum + l[i] 
        else:
            sum = total_sum(l[i], sum)   
    return sum
   

def rec_fib(n,i1=0,i2=1,l=[0]):
    if n==0:
        return l
    else:
        l.append(i1+i2)
        return rec_fib(n-1,i1+i2,i1,l)
        

print(total_sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))
print(rec_fib(5,l=[0]))
print(rec_fib(10,l=[0]))