d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

x = (input('Please, enter phone number \n'))

if x.isdigit() == True:
    if len(x) == 10:
        x = int(x)
        if x in d:
            print(f'{d[x][0][0]} {d[x][0][1]} from {d[x][1][0]}, {d[x][1][1]}')
        else:
            print('the number was not found')
    else:
        print('not 10 digits')
else:
    print('Enter only number')
    
