dict = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
number = input("Input the phone number (10 symbols, only numbers):\n")
if number.isdigit() == True and len(number) == 10:
    number = int(number)
    if number in dict:
        print(f"{dict[number][0][0]} {dict[number][0][1]} from {dict[number][1][0]} {dict[number][1][1]}")
    else:
        print("The number was not found")
else:
    print("Incorrect nubmer")
# I thought i could't use int here   