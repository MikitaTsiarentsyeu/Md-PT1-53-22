from functools import reduce


def apply(l, f, i=0):
    if i == len(l):
        return
    f(l[i])
    apply(l, f, i+1)

l = [1,2,3,4,5]
apply(l, print)

def print_sq(x):
    print(x*x)

apply(l, print_sq)
apply(l, lambda x: print(x*x))

add_2 = lambda x: x+2
print(add_2(2))

print((lambda a, b, c: a+b+c)(2,3,4))

test_str = "Abc Aac aaa ttt kit kot"
print(sorted(test_str.split()))
print(sorted(test_str.split(), key=lambda x: x.lower()))
print(sorted(test_str.split(), key=str.lower))

l = [("one", 1), ("two", 2), ("three", 3)]
print(sorted(l))
print(sorted(sorted(l), key=lambda x: x[1]))

# def get_second(x):
#     return x[1]

d = {"one":1, "two":2, "three":3}
print(sorted(d))
print(sorted(d.items(), key=lambda x: x[1]))

l = [1,2,3,4,5,6,7,8,9,10]
# map_res = (print, l)
# print(map_res, type(map_res))
# for i in map_res: pass

print(list(map(lambda x: chr(x*10), l)))
# print([(lambda x: chr(x*10))(elem) for elem in l])
print(list(filter(lambda x: x>4, l)))

print(list(map(lambda x: chr(x*10), filter(lambda x: x>4, l))))

print(reduce(lambda x, y: x+y, l))

print(reduce(lambda x, y: f"{x}-{y}", l))

print(reduce(lambda x, y: x if x > y else y, l))

l = ['1', '11', '12', '22', '2', '13', '30', '33'] 

print(sorted(l, key=lambda x: int(x)))

print(list(filter(lambda x: int(x) % 2 == 0, l)))

print(sorted(filter(lambda x: int(x) % 2 == 0, l), key=int))