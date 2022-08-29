data = {9103976271: [("Reina", "Meinhard"), ("Memphis", "Tennessee")],
        4199392609: [("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
        9099459979: [("Ermes", "Angela"), ("Dallas", "Texas")],
        6123479367: [("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
        7548993768: [("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
        
number = input("Enter the phone number in 10 characters:\n")

if len(number) == 10 and number.isdigit() == True:
    phone_number = int(number)
    d = data.get(phone_number)
    #print(f"{data.get(phone_number)[0][0]} {data.get(phone_number)[0][1]} from {data.get(phone_number)[1][0]}, {data.get(phone_number)[1][1]}.")
    print(f"{d[0][0]} {d[0][1]} from {d[1][0]}, {d[1][1]}.")
elif len(number) != 10 or number.isdigit() != True:
    print("Enter the correct phone number.")
else:
    print("The number was not found")