def list_sum(l, res=0):

    for i in l:

        if isinstance(i, int):
            res+=i
        else:
            res+=list_sum(i)
    return res            

def fib(n, i=1, x=1, l=[0]):

    if n == 1:
        return str(l).strip('[]')
    l.append(x)

    return fib(n-1, i+1, x+l[i-1])
