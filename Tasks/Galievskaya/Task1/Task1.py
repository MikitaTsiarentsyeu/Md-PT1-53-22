P0 = int(input("Input deposit amount: \n"))
t = float(input("Input term of deposit in years: \n")) 
r = float(input("Input annual interest rate: \n"))

if (P0<=0 or t<=0 or r<=0):
    print("Oops, looks like you entered invalid data, please try again.")
    exit()

mc = input("Do you want to enable monthly capitalization? y/n \n") 
r0 = r / 100

if (mc.lower() == "n"):
    x = P0 * r0 * t
    Px = P0 + x
else:
    n = 12
    Px = round( (P0 * (1 + r0/n)**(n*t)), 2)

print(f"Amount at the end of the period: {Px}")