import random

my_number = random.randint(1, 10)

your_number = int(input("Guess a number from 1 to 10:\n"))

if my_number == your_number:
    print("correct!")
else:
    print("looooooser!")
