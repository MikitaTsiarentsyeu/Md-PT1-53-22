d={9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

phone_number = input("Enter phone namber")

if len(phone_number) != 10:
    print ("The number must consist of the 10 digits")

if not phone_number.isdigit():
    print ("The number must consist of some digits only")

phone_number = int(phone_number)
if phone_number in d:
    print(f"{d[phone_number][0][0]} {d[phone_number][0][1]} from {d[phone_number][1][0]}, {d[phone_number][1][1]}")
else:
    print("Nothing was found")





