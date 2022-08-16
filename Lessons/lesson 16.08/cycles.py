# while True:
#     print("to infinity and beoynd!")

# x = 0
# while x < 10:
#     print("to infinity and beoynd!")
#     x += 1

x = 10
while x > 0:
    print("to infinity and beoynd!")
    x -= 1

i = 0

for i in [1,2,3,4,5,"test",[]]:
    print(f"the current elem is {i}")

s = "some test string"
for i in s:
    print(i)

print(f"the last value of i - {i}")

d = {1:"one", 2:"two", 3:"three"}
for i in d:
    print(i, d[i])

for i in d.values():
    print(i)

for k, v in d.items():
    print(k)
    print(k, v)

print("*********")

l = [1,2,3,4,5,6,7,8,9]
for i in l:
    print(l.pop())
    print(i)
    print(l)


l = [1,2,3,4,5,6,7,8,9]

i = 0
while i < len(l):
    print(f"the current elem is {l[i]}")
    i += 1

for i in range(1,11,2):
    print(f"the action number {i}")

for i, e in enumerate("some string"):
    print(f"the element {e} has index {i}")

l = [[1,2,3], [4,5,6], [7,8,9]]
for i in l:
    print(i)
    for j in i:
        print(j)

for i in [1,2,3,4,5]:
    for j in [1,2,3,4,5,6,7]:
        print(f"i {i}, j {j}")

print("the end")


for i in range(100):
    if i > 20:
        break
    if i%2 != 0:
        continue
    print(f"the current even number is {i}")
else:
    print("my work here is done")


x = -1
while True:
    x += 1
    if x > 20:
        break
    if x%2 != 0:
        continue
    print(f"the current even number is {x}")
