import math

a = 3
b = -14
c = -5

D = b*b - 4*a*c
print(D)

print(math.sqrt(D))
print(D**0.5)

x1 = (-b + D**0.5) / (2*a)
x2 = (-b - D**0.5) / (2*a)

print(x1, x2)