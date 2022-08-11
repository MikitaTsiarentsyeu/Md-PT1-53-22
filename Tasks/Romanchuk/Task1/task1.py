import decimal


def input_check(message):
    try:
        value = decimal.Decimal(input(message))
    except decimal.InvalidOperation:
        print("\tInput Error: Not a number entered")
        return False
    if value <= 0:
        print("\tInput Error: Invalid value")
        return False
    return value


print("\n\t\tDEPOSIT CALCULATION")
while True:
    deposit = input_check("\nEnter the deposit amount in $: ")
    if deposit:
        break

while True:
    period = input_check("\nEnter the deposit term in years: ")
    if period:
        break

while True:
    percent = input_check("\nEnter the annual rate in %: ")
    if percent:
        break

cap_type = input("\nIf you want to enable monthly capitalization enter 2, if not enter any other: ")

if cap_type == '2':
    total_amount = deposit * (1 + percent / 100 / 12) ** (12 * period)
else:
    total_amount = deposit * (1 + percent * period / 100)

print(f'\n\t\tTOTAL AMOUNT: {round(total_amount, 2)} $')
