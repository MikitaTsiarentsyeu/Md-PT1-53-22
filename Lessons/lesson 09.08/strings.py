x = "my new string"
y = 'my new string'
u = """my new string"""
v = '''my new string'''

print(id(x)==id(y), x==y==v==u)

x = """    my first line
    my second line
    my third line"""

print(x)
print(repr(x))

y = "\tmy first line\n\tmy second line\n\tmy third line"
print(y)

space = " "
empty = ""

print(type(empty), empty == space)

s = "my very long string"
print(len(s))
print(s[0], s[1], s[2], s[3], s[4], s[5])
print(s[0], s[-1], s[-2], s[-3], s[-4], s[-5])

print(s[len(s)-1])
print(s[-len(s)])

# print(s[10000]) error
# print(s[-len(s)-1]) error

print(s[0:7])
print(s[3:-3])

print(s[3:15:3])
print(s[-len(s):3])
print(s[::-1])
print(s[4:])

print('s' in s)
print('long' in s)
print('test' in s)

print(s.find('s'))
print(s.find('long'))
print(s.find('test'))

print(s.replace(' ', '_'))
print(s)

print(s.replace(' ', '_').replace("my", "your").replace("long", "short"))
print(s)

s = s.replace(' ', '_').replace("my", "your").replace("long", "short")
print(s)

s = "TesT StrinG"
print(s.upper())
print(s.lower().capitalize())
print(s.islower())
print("42".isdigit())
print("45365dfd7687guig".isalpha())
print("45365dfd7687guig".isalnum())

s = "ssssome new test string"
print(s.split())
print(s.split('s'))
print(s.split('st'))
print(s.split('new'))

s = "4567868431:adidas_superstar"
print(s.split(":")[1].split("_"))

print("   test                      ".strip())
print("!!test!!!!!!".strip("!"))


s = "ssssome new test string"
parts = s.split()
print('_'.join(parts))
print('THISISSPACE'.join(['some', 'not', 'so', 'long', 'text']))

print("test1"+"test2")
print("test"*10)
print(3*"test")
# print("3"*"test") error

c, d, p = "cat", "dog", "parrot"
"a cat, a dog, and a parrot"
s = "a " + c + ", a " + d + ", and a " + p
"a cat"
"a cat, a "
"a cat, a dog"
"a cat, a dog, and a "
"a cat, a dog, and a parrot"
print(s)

print("a {}, a {}, and a {}".format(c, d, p))
print("a {}, a {}, and a {}".format("dog", "duck", "fish"))
print("a {1}, a {2}, and a {0}".format("dog", "duck", "fish"))
print("a {c}, a {d}, and a {p}".format(p="dog", c="duck", d="fish"))

pattern = "a {}, a {}, and a {}"
pattern.format("dog", "duck", "fish")
pattern.format(c, d, p, "something else")

print(f"a {c}, a {d}, and a {p}")
print(f"the result is {12/3}")

# print("%s %d" % ("the result is", 88)) old style, do not use!!!