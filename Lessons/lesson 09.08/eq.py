data = {9103976271: [("Reina", "Meinhard"), ("Memphis", "Tennessee")],
        4199392609: [("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
        9099459979: [("Ermes", "Angela"), ("Dallas", "Texas")],
        6123479367: [("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
        7548993768: [("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

while True:
    s = input("\nPlease enter the number: ")
    if s.isdigit() and len(s) == 10:
        number = int(s)
        break
    else:
        print('\tIncorrect number')

if number in data:
    print(f'\t{data[number][0][0]} {data[number][0][1]} from {data[number][1][0]}, {data[number][1][1]}')
else:
    print('\tThe number was not found')