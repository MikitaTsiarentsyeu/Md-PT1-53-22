print("Hello, thank you very much for choosing to use the services of our online banking.")
a = int(input('Enter the value of the deposit \n'))
b = int(input('Enter time period(years) \n'))
c = float(input('Enter rate \n'))                        
capitalization = input('Enter y or n \n')
if capitalization == 'n':
    year = b * 365
    total = (a * c * (year / 365)) / 100
    total = a
    print(f'After {b} years you are get {total} glass bottles')        
elif capitalization == 'y':
    year = b * 365
    term_per_month = b * 12
    total = int(a * (1 + (c / 100) / 12) ** term_per_month) 
    print(f'After {b} years you are get {total} glass bottles')
#a-how much money to put in the deposit
#b-for how long time
#c-what percent do you want