import math
import  decimal

print("Enter data to calculate the deposit")
deposit = input("Want to enable monthly capitalization? (yes/no):")
if deposit == "no":
  P = decimal.Decimal(input("The amount initially deposited"))
  I = decimal.Decimal(input("The size of the '%' rate (per year)"))
  t = decimal.Decimal(input("Number of days of accrual%"))
  K = decimal.Decimal(input("Number of days per calendar year"))

  P = 20000
  I = 15
  t = 1825
  K = 365

  deposit1 = (20000 + (20000 * 15 * 1825 / 365) / 100)
  print("The amount at the end of the term will be: '$'", decimal.Decimal(deposit1).quantize(decimal.Decimal("1.0000"), decimal.ROUND_DOWN))
elif deposit == "yes":
  n = decimal.Decimal(input("The number of performed operations for transferring interest to the body of the deposit during the full term of the agreement"))
  P = decimal.Decimal(input("Initially deposited amount with the possibility of capitalization"))
  N = decimal.Decimal(input( "'%' rate (annual)"))

  n = 60
  P = 20000
  N = 15
  deposit2 = (20000 * (1 + (15 / 1200))**60)
  print("The amount at the end of the term will be: '$'", decimal.Decimal(deposit2).quantize(decimal.Decimal("1.0000"), decimal.ROUND_DOWN))