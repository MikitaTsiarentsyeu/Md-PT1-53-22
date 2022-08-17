deposit_amount = float(input('Enter deposit amount:\n'))
deposit_term = float(input('Enter deposit term in years:\n'))
annual_percent = float(input('Enter annual percent:\n'))
switchcap = input('Choose N or Y to enable capitalization:\n')

if switchcap == 'Y' or switchcap == 'y':
    total_amount = round(deposit_amount*((1+(annual_percent/100)/12)**(12*deposit_term)), 2)
    print('Account balance at the end of the term:', total_amount)
elif switchcap == 'N' or switchcap == 'n':
    total_amount = round(deposit_amount*(1+annual_percent/100)**deposit_term, 2)
    print('Account balance at the end of the term:', total_amount)
else:
    print('Choose N or Y')