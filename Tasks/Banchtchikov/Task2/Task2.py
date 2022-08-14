dict = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
number = input("Input the phone number (10 symbols, only numbers):\n")
if number.isdigit() == True and len(number) == 10:
    if number == "9103976271":
        print(list(dict.get(9103976271))[0], "from", list(dict.get(9103976271))[1])
    elif number == "4199392609":
        print(list(dict.get(4199392609))[0], "from", list(dict.get(4199392609))[1])
    elif number == "9099459979":
        print(list(dict.get(9099459979))[0], "from", list(dict.get(9099459979))[1])
    elif number == "6123479367":
        print(list(dict.get(6123479367))[0], "from", list(dict.get(6123479367))[1])
    elif number == "7548993768":
        print(list(dict.get(7548993768))[0], "from", list(dict.get(7548993768))[1])
    else:
        print("The number was not found")
else:
    print("Incorrect nubmer")
    
    
