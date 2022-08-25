import os

print(os.name)

print(type(os.sep), os.sep)

print(os.sep.join(["test level 1", "test level 2"]))

x = os.path.join("test level 1", "test level 2", "test level 3", "test level 4")

print(os.getcwd())

# os.makedirs(x)

# os.chdir(x)
# print(os.getcwd())
# open("test.txt", 'w')

print(os.listdir())

print(os.walk(os.getcwd()))
for l in os.walk(os.getcwd()):
    print(l)

# os.remove("test.txt")

os.removedirs(x)