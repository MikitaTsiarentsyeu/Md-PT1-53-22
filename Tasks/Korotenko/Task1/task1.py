amount = int(input('Enter amount \n'))
term = int(input('Enter time period(years) \n'))
rate = float(input('Enter rate \n'))
                        #currens = input('Enter currency \n')
capitalization = input('Enter y or n \n')

if capitalization == 'n':
    years_per_day = term * 365
    total = (amount * rate * (years_per_day / 365)) / 100
    total += amount
    print(f'After {term} years your income will be {total} usd')
        
elif capitalization == 'y':
    years_per_day = term * 365
    term_per_month = term * 12
    total = int(amount * (1 + (rate / 100) / 12) ** term_per_month) 
    print(f'After {term} years your income will be {total} usd')

    
