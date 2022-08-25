d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

number = input('Input the phone number: ')
if number.isdigit() and len(number) == 10:
   number = int(number)  
elif not number.isdigit():
   print ('The phone number must be numeric!')
else: 
    print('The lenth of phone number must be 10 symbols!')

if number in d:
   print(f'{d[number][0][0]} {d[number][0][1]} from {d[number][1][0]}, {d[number][1][1]}')
else:
    print('The number was not found!')