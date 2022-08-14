data = {
    9103976271: [("Reina", "Meinhard"), ("Memphis", "Tennessee")],
    4199392609: [("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
    9099459979: [("Ermes", "Angela"), ("Dallas", "Texas")],
    6123479367: [("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
    7548993768: [("Margarete", "Quintin"), ("Raleigh", "North Carolina")]
}

phone_number = input('input phone number\n')
if len(phone_number) == 10 and phone_number.isdigit():
    obj = data.get(int(phone_number))
    print(f'{obj[0][0]} {obj[0][1]} from {obj[1][0]}, {obj[1][1]}')
else:
    print('The number was not found')