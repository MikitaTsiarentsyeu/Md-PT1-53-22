def digit_sum(l):
    sum = 0
    for i in l:
        if  isinstance(i, int):
            sum += i
        else:
            sum += digit_sum(i) 
    return sum
digit_sum([1, 2, [2, 4, [[7, 8], 4, 6]]])

def fib(n):
    def fib_sum(n):        
        if (n <= 1):
            return n
        else:
            return(fib_sum(n-1) + fib_sum(n-2))
    l = []
    for i in range(n):
        l.append(str(fib_sum(i))) 
        str_l = ','.join(l)
    print(str_l)
       
    
fib(5)