amount = float(input('input amount of money \n'))
time = int(input('input time in years \n'))
rate_deposit = float(input('input rate deposit \n'))
capitalisation = input('do you want to enable monthly capitalisation? (yes/no)')
if capitalisation == 'yes':
    money = round(amount * pow((1 + rate_deposit / 1200), (time * 12)), 2)
    print(f'in the end of deposit you will get back {money}, your profit is {money - amount}')
elif capitalisation == 'no':
    money = round(amount + amount * rate_deposit / 100 * time, 2)
    print(f'in the end of deposit you will get back {money}, your profit is {money - amount}')
