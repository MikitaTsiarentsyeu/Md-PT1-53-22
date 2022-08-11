


from decimal import Decimal
start_sum = Decimal(input("Enter start sum"))
interest_rate = Decimal(input("Enter interest rate"))
deposit_term_years = Decimal(input("Enter deposit term years"))
capit_times_in_year = Decimal(input("Enter capit times in year"))
z = int(input("Enter 1 if you are interested in calculating the deposit with monthly capitalization, 0 if you are not interested in interest capitalization"))
if z == int(1):
    final_sum = start_sum * (1 + interest_rate/(100*capit_times_in_year))**(capit_times_in_year*deposit_term_years)
    print (round(final_sum, 2))
else:
    final_sum = start_sum * (1 + (deposit_term_years*interest_rate)/100)
    print (round(final_sum, 2))

