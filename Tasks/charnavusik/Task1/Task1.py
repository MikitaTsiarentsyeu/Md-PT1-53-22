a = int(input('Enter amount \n'))
b = int(input('Enter time period(years) \n'))
c = float(input('Enter rate \n'))                       
capitalization = input('Enter y or n \n')
if capitalization == 'n':
    years_per_day = b * 365
    money = (a * c * (years_per_day / 365)) / 100
    money += a
    print(f'After {b} years you are get {money} glass bottles')        
elif capitalization == 'y':
    years_per_day = b * 365
    term_per_month = b * 12
    money = int(a * (1 + (c / 100) / 12) ** term_per_month) 
    print(f'After {b} years you are get {money} glass bottles')
#a=initial amount of money
#b=a period of time
#c=your percent