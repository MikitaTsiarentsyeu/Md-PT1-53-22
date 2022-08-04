a, b, c = int(input("Enter the a value:\n")), int(input("Enter the b value:\n")), int(input("Enter the c value:\n"))

D = b*b - 4*a*c

if D > 0:
    print("the first root is", (-b + D**0.5)/(2*a))
    print("the second root is", (-b - D**0.5)/(2*a))
elif D == 0:
    print("the root is", (-b )/(2*a))
else:
    print("there are no roots")