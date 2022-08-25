d={9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
    4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
    9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
    6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
    7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
print(d)
x = int(input("Enter phone number"'\n'))
if x in d.keys():
    a = d[x]
    b1 = a[0]
    b2 = a[1]
    print(f"{b1[0]} {b1[1]} from {b2[0]}, {b2[1]}")
else:
    print(d.get("", "nothing was found"))

