# n – the number of performed operations for transferring interest to the body of the deposit during the full term of the contract;
# S – the amount of the deposit on the expiration date of the deposit, which the depositor will receive in his hands;;
# Р – initially deposited amount with the possibility of capitalization;
# N - % rate (annual);
# d – equals 30 - the number of days for which % is charged before capitalization;
# D – days in a year.


P = 20000
N = 15
d = 30
D = 365
n = 60
z = int(input("Enter 1 if you are interested in calculating the deposit with monthly capitalization, 0 if you are not interested in interest capitalization"))
if z == 1:
    print("deposit balance", round(P *(1 + (N*d)/(100*D))**n, 2))
else:
    print("deposit balance", round(P *(N * 5 /100 + 1)), 2)
    