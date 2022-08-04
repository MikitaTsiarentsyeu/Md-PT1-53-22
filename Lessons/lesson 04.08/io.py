x = 2
y = "test"
print(x)
print(x, y, "some other text", "and another", "and another", sep=';', end='.\n')
print(x, y, "some other text", "and another", "and another", sep='SOME SEPARATOR', end='THE END\n')
print(x, y, "some other text", sep=' ', end='\n') # equal to print(x, y, "some other text")

x = input("Please input your data:\n")
print("the data is", x)