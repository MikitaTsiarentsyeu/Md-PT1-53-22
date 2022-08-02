import decimal
import fractions
import math
import random

x = 3
print(type(x), x)

print(5+10//5)

print(round(3.7777777777, 3))
print(round(2.5))
print(round(3.5))
print(round(4.5))
print(round(5.5))

print(int(5.6))
print(int(-5.6))
print(int('5'))

print(2+2)
print(2*2)
print(2-2)
print(2/2)
print(2//2)
print(2**2)
print(10%2)

x = 3.3
print(type(x), x)

print(10+4*3.5)

print(float(3))
print(float('3.4'))

print(3.3 == 3.3)
print(1.1+1.1+1.1 == 3.3)
print(1.1+1.1+1.1)

x = decimal.Decimal(1.1)
y = decimal.Decimal(3.3)
print(x+x+x == y)
print(x+x+x)
print(x)


x = decimal.Decimal('1.1')
y = decimal.Decimal('3.3')
print(x, y)
print(x+x+x == y)


print(fractions.Fraction(2.8))
print(fractions.Fraction(1.1))
print(fractions.Fraction('1.1'))
print(fractions.Fraction('2.8'))
print(fractions.Fraction(1, 4))
print(fractions.Fraction(2, 4))


print(math.pi, math.inf)
print(type(math.pi), type(math.inf))

print(math.sin(math.pi))
print(math.log10(100000000000))
print(math.factorial(6))

print(random.randrange(1, 10))
print(random.randint(1, 10))

l = [1,2,3,4,5,6,7,8,9,10]
print(random.choice(l))
random.shuffle(l)
print(l)