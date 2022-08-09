import math

first_sum=int(input('Enter initial deposit amount (ex. 1000) '))
year=int(input('Enter deposit terms in years (ex. 5) '))
perc=int(input('Enter annual deposit persentage (ex. 15) '))
cap=str(input('Press "Y" - to enable monthly capitalization or Press "N" - to disable monthly capitalization '))

if cap.upper() !='Y' and cap.upper() !='N':
    print ('Error: try again - press Y or N')
else:
    print ('Initial deposit amount', first_sum, sep = ' ', end = '. \n')
    print ('Deposit terms in years', year, sep = ' ', end = '. \n')
    print ('Annual deposit persentage', perc, sep = ' ', end = '. \n')

    if cap.upper() == 'Y':
        print ('Monthly capitalization - YES', sep = ' ', end = '. \n')
        print ('Total income:' , str(math.ceil(first_sum*((1 + perc / 12 / 100)**(year*12)))), sep = ' ', end = '.')
    else:
        print ('Monthly capitalization - NO', sep = ' ', end = '. \n')
        print ('Total income:' , str(math.ceil(first_sum * (1 + perc / 100*year))), sep = ' ', end = '.')
        