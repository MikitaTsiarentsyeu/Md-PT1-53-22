l = []
l = [1,2,3,4,5,6,7,8,9]
print(type(l), l)

print(str(l))
s = str(l)
l = list(s)
print(l)

s = "my test string"
l = list(s)
print(l)

l = [1,2,3,4,5,6,7,8,9,"0",[]]

print([1,2,3]+[4,5,6])
print([1]*5)

print(l[0])
print(l[len(l)-1])
print(l[1:6:2])
print(l[::-1])

l[0] = 1.0
print(l)

l[0:3] = [-3,-2,-1,0,1,2,3]

l.append("new elem")
print(l)

l.extend("test")
print(l)

l.extend([11,12,131,4])
print(l)

l.insert(0, "new first element")
print(l)

l.insert(11, "new 12th element")
print(l)

l.remove('0')
print(l)

print('t' in l)
print(8 in l)

print(l.pop())
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)


print(l.pop(0))
print(l)
print(l.pop(0))
print(l)
print(l.pop(0))
print(l)
print(l.pop(0))
print(l)


# print(l.pop(10))
# print(l)
# print(l.pop(10))
# print(l)
# print(l.pop(10))
# print(l)
# print(l.pop(10))
# print(l)

del l[0]
print(l)

del l[-1]
print(l)

del l[0:8]
print(l)

# del l
l.clear()
print(l)

