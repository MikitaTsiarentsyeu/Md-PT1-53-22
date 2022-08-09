deposit = int(input('Enter deposit amount:\n'))
rate = float(input('Enter interest rate\n'))
n = int(input('Enter the number of years\n'))
c_type = int(input('Select the type of capitalization. Enter 1 for monthly, enter 2 for annual.\n'))
if c_type == 1:
    sum = deposit * ((1 + rate/100/12)**(n*12))
    print('In', n , 'year(s) you will get:' , sum)
elif c_type == 2:
    sum = deposit * ((1 + rate/100))**n
    print('In' , n , 'year(s) you will get:' , sum)
else:
    print('Incorrect type of capitalization')
        