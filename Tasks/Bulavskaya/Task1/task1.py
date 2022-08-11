import decimal

P = decimal.Decimal(input("Enter the initial amount: "))
I = decimal.Decimal(input("Enter the annual interest rate: "))
T = decimal.Decimal(input("Enter time of the investment: "))
C = input("Do you need monthly capitalization (y/n): ")

if C == "y":
    S = P * ((1 + (I/1200))**(T*12))
    print("Your final amount is", decimal.Decimal(S).quantize(decimal.Decimal("1.0000")))
elif C == "n":
    S = P + ((P * I * T)/100)
    print("Your final amount is", decimal.Decimal(S).quantize(decimal.Decimal("1.0000")))