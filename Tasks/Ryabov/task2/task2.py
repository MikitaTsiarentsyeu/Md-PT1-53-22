d={9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
print(d)

x = int(input("Enter phone namber"))
if x in d.keys():
    l = d[x]
    t1 = l[0]
    t2 = l[1]
    print(f"{t1[0]} {t1[1]} from {t2[0]}, {t2[1]}")
else:
    print(d.get("", "nothing was found"))





