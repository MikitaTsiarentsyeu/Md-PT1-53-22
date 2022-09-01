x, y = "global x", 'global y'

for i in range(10):pass

print(x, y, i)

def scopes_test(y):
    print(y)
    x = "value from scopes_test"
    print(x, y)

def global_test():
    print(x, y)

global_test()
scopes_test("y value from parameters")
print("after calls:")
print(x, y)