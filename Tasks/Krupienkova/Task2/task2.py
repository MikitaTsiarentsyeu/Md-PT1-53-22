import sys

phone_book = {
    9103976271: [("Reina", "Meinhard"), ("Memphis", "Tennessee")],
    4199392609: [("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
    9099459979: [("Ermes", "Angela"), ("Dallas", "Texas")],
    6123479367: [("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
    7548993768: [("Margarete", "Quintin"), ("Raleigh", "North Carolina")],
    }

phone_number = input("Enter the phone number:\n")
if not phone_number.isdigit() or len(phone_number) != 10:
    sys.exit("Incorrect number format!")

info = phone_book.get(int(phone_number))
if not info:
    sys.exit("The number was not found!")

name, surname = info[0]
city, state = info[1]
sys.exit(f"{name} {surname} from {city}, {state}")

