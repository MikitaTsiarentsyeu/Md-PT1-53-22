import math

# Formula for calculating the amount without including capitalization

# S = P + (P * I * t / K) / 100

# Name
  
'''S - the final amount received upon completion of the deposit;
   P - the amount initially deposited;
   I - the size of the % rate (per year);
   t - number of days of accrual%;
   K - number of days per calendar year.'''

P = 20000
I = 15
t = 1825
K = 365

S = P + (P * I * t / K) / 100
print(int(S),'$')

# Formula for deposits with monthly capitalization

# S = S = P * (1 + (N / 1200))**n

# Name
 
'''n - the number of performed operations for transferring interest to the body of the deposit during the full term of the agreement;
   S - the amount of the deposit on the expiration date of the deposit, which the depositor will receive in his hands;
   P - initially deposited amount with the possibility of capitalization;
   N - % rate (annual).'''

n = 60
P = 20000
N = 15
S = P * (1 + (N / 1200))**n
print(int(S),'$')