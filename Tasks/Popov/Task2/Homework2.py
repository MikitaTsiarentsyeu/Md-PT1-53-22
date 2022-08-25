d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

number = input("\nPlease enter the number: ")
if number.isdigit():
    if len(number) == 10:        
       number = int(number)
    else:
        ('Only 10 digits')
else: 
    print('Phone number must contain only digits')

if number in d:
    print(f'{d[number][0][0]} {d[number][0][1]} from {d[number][1][0]}, {d[number][1][1]}')
else:
    print('The number was not found') 

     


