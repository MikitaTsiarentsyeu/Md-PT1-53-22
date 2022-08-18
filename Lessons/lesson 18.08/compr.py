l = [str(x) for x in range(100) if x < 50 and x > 25]
# print(l)

l = []
for x in range(100):
    if x < 50:
        if x > 25:
            l.append(str(x)*10)
# print(l)

print([int(x)*10 for x in "123456789"])

l1 = [1,2,3,4,5]
l2 = [0,1,2]

l = [x*y for x in l1 for y in l2]
print(l)

l = []
for x in l1:
    for y in l2:
        l.append(x*y)
print(l)


l = [[1,2,3], [4,5,6], [7,8,9]]
l = [y for x in l for y in x]
print(l)

d = {str(x):x*x for x in l}
print(d)