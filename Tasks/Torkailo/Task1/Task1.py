import decimal
import math

first_sum=decimal.Decimal(input('Enter initial deposit amount (ex. 1000) '))
year=int(input('Enter deposit terms in years (ex. 5) '))
perc=decimal.Decimal(input('Enter annual deposit persentage (ex. 15) '))
cap=str(input('Press "Y" - to enable monthly capitalization or Press "N" - to disable monthly capitalization '))

if cap.upper() !='Y' and cap.upper() !='N':
    print ('Error: try again - press Y or N')
else:
    print (f'Initial deposit amount {first_sum} BYN')
    print (f'Deposit terms in years {year} years.')
    print (f'Annual deposit persentage {perc}%')

    if cap.upper() == 'Y':
        print ('Monthly capitalization - YES')
        print (f'Total income: {round(first_sum*((1 + perc / 12 / 100)**(year*12)),2)} BYN')
    else:
        print ('Monthly capitalization - NO')
        print (f'Total income: {round(first_sum *(1 + perc / 100*year),2)} BYN')
        