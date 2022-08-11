t = (1,2,3,4,5,"test",[])
print(t, type(t))

# t = (1,)
# print(t, type(t))

print(t[0], t[1], t[-1])
print(t[::-1])
print(len(t))

print((t+t)*3)
print(t.index([]))

# t[0] = 1.0 error

# t.append(10) error

del t


d = {}
print(d, type(d))

d = {"one": 1, "two": 2, "three": 3, 4: "four", 5: [5]}
print(d, type(d))

print(d["one"], d[5])

# print(d["test"]) error

d["one"] = 1.0
print(d["one"])

d["test"] = "test"
print(d)

print(d["test"])
print(d.get("test"))
print(d.get("", "nothing was found"))

if "test" in d:
    print("it is in my dictionary")

print(d.keys())
print(d.values())

if 'four' in d.values():
    print("it is in my dictionary")

print(list(d.items())[0])

print(d.pop(5))
print(d)

print(d.popitem())
print(d)
print(d.popitem())
print(d)
print(d.popitem())
print(d)

s = {}
print(s, type(s))

s = set()
print(s, type(s))

s = {1,3,5,'a','b','c'}
print(s)

s = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}
print(s)

l = [1,2,3,3,3,4,4,5,6,7,8,'a','b','c']
l = list(set(l))
print(l)

s = "test new string for the set"
s = set(s)
print(s)
s = "".join(s)
print(s)

l1 = [1,2,3,3,3,3,3,3,3]
l2 = [3,2,1]
print(l1 == l2, set(l1) == set(l2))

# {1,2,3,[]} error

s = {1,2,3,4,5,'a','b'}
s.add(1)
s.add(6)
print(s)

s.update([5,6,7,8,9])
print(s)

s.remove('a')
print(s)

# s.remove('a') error
s.discard('a')
s.discard(9)
print(s)

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

s.clear()
print(s)

s1 = {1,2,3,4}
s2 = {3,4,5,6}

print(s1.union(s2))
print(s1.intersection(s2))

print({1,2,3}.issubset({0,1,2,3,4,5}))
print({0,1,2,3,4,5}.issuperset({4,5}))