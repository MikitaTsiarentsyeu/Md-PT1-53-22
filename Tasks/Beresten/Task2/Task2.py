


data = {9103976271: [("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609: [("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979: [("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367: [("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768: [("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}


phone_number = input('input phone number: ')
p = phone_number

if len(p) == 10 and p.isdigit():
    p = int(p)
    f = data.get(p, 'The number was not founding')
    if f == 'The number was not founding':
        print(f)
    elif f == data.get(p):
        print(f'{data.get(p)[0][0]} {data.get(p)[0][1]} from {data.get(p)[1][0]}, {data.get(p)[1][1]}')
else:
    print('The number was not founding')