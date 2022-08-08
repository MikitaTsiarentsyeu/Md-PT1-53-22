from decimal import Decimal
import sys

print("Welcome to the Deposit calculator!")

MONTH_IN_YEAR = 12

try:
    initial_amount = Decimal(input("Enter the deposit amount, EUR:\n"))
    if initial_amount < 0:
        sys.exit("Incorrect deposit amount! Try again!")

    years = Decimal(input("Enter the term in years:\n"))
    if years < 0:
        sys.exit("Incorrect term in years! Try again!")

    percent = Decimal(input("Enter the annual percent:\n"))
    if percent < 0:
        sys.exit("Incorrect annual percent! Try again!")

    capitalization = input("Use monthly capitalization? (Enter y/n)\n")

    if capitalization == "n":
        total_multiplier = 1 + percent / 100 * years
        total_amount = initial_amount * total_multiplier
        print("The total amount is " + str(round(total_amount, 2)) + " EUR")
    elif capitalization == "y":
        monthly_multiplier = 1 + percent / 100 / MONTH_IN_YEAR
        months = years * MONTH_IN_YEAR
        capital_amount = initial_amount * monthly_multiplier ** months
        print("The total amount with capitalization is " +
              str(round(capital_amount, 2)) + " EUR")
    else:
        sys.exit("Incorrect capitalization information! Try again!")

except Exception:
    sys.exit("Incorrectly entered data! Try again!")



