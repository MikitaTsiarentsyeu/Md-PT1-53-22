def apply(target, func):
    for i in target:
        print(func(i))

def sq(x):
    return x*x

l = [1,2,3,4,5,6,7]

apply(l, sq)
apply(l, str)
apply(l, float)

def sum(a, b):
    return a+b

sum(2, 3)
sum(2.0, 6.8)