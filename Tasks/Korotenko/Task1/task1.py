from decimal import Decimal

amount = Decimal(input('Enter amount \n'))
term = Decimal(input('Enter time period(years) \n'))
rate = Decimal(input('Enter rate \n'))
capitalization = input('Enter y or n \n')

if capitalization == 'n':
    years_per_day = term * 365
    total = (amount * rate * (years_per_day / 365)) / 100
    total += amount
    print(f'After {term} years your income will be {total:0.2f} usd')
        
elif capitalization == 'y':
    years_per_day = term * 365
    term_per_month = term * 12
    total = (amount * (1 + (rate / 100) / 12) ** term_per_month) 
    print(f'After {term} years your income will be {total:0.2f} usd')


    
