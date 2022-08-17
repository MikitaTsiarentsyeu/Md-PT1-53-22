data = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
num = input("Input the number:\n")

if num.isdigit() and len(num)==10:

    num = int(num)    
    x = data.get(num, 'The number was not found')
    if x == 'The number was not found':
        print(x)
    elif x == data.get(num):
        print(f'{data.get(num)[0][0]} {data.get(num)[0][1]} from {data.get(num)[1][0]}, {data.get(num)[1][1]}')
else:
    print('Incorrect number! Try again!')  