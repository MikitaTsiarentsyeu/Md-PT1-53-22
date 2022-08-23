# f = open("test\\test.txt", 'w')
# f = open(r"test\test.txt", 'w')
# import os
# print(os.getcwd())

# f = open("test.txt", 'w')
# f.write("test content")
# f.close()


with open("test.txt", 'w') as f:
    # print(f, type(f))
    f.write("test content from with\n")
    f.writelines(["line 1\n", "line 2\n", "line 3\n"])
    # f.read() error

with open("test.txt", 'r') as f:
    # f.write("test") error
    for line in f:
        print(repr(line))

    # print(f.readlines())

    # print(repr(f.readline()))
    # print(repr(f.readline()))
    # print(repr(f.readline()))

    # f.seek(5)
    # print(repr(f.read(10)))
    # print(repr(f.read(10)))

    # content = f.read()
    # print(repr(content), len(content))
    # f.seek(0)
    # print(repr(f.read()))

with open("test.txt", 'a') as f:
    # f.read() error
    f.write("appended content\n")
    # f.seek(0)
    # f.write("prepended content\n") # writing to the end anyway


with open("test.txt", 'a+') as f:
    f.write("appended content\n")
    f.seek(0)
    f.write("prepended content\n")
    f.seek(0)
    print(repr(f.read()))

with open("test.txt", 'r+') as f:
    f.write("prepended content from the r+ mode")
    print(repr(f.read()))

with open("test.txt", 'w+') as f:
    f.write("totally new content from the w+ mode")
    f.seek(0)
    f.write("after moving to zero")
    print(repr(f.read()))