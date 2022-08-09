eq = input("input your equation in format y=kx+b:\n")
x = int(input("input the x value:\n"))

print(eq, x)

eq = eq.replace(" ", "").replace("y=", "")
print(eq)

coeff = eq.split('x')
print(coeff)

res = x*int(coeff[0])+int(coeff[1])
print(f"the result is {res}")