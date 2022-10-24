"""дана структура данных, нужно дать пользователю возможность искать по номеру телефона
вывод в случае совпадения - "{имя} {фамилия} from {город}, {штат}"
в случае несовпадения - "the number was not found"

предусмотреть валидацию о длине введённой строки и по её символам (должны быть числа) """

data={9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

def validation_check(phone_number_search):
    try:
        int(phone_number_search)
        if len(phone_number_search) != 10:
            raise RuntimeError ("The value you enter must contain 10 digits.")
    except (ValueError, RuntimeError):
        return "The input value must be numeric and contain 10 digits.\n"

while True:
    phone_number_search = input("Please enter the phone number you are looking for: \n")
    validation = validation_check(phone_number_search)
    if validation:
        print (validation)
        continue
    else:
        break

number = int(phone_number_search)
if data.get(number):
    print(f"{data.get(number)[0][0]} {data.get(number)[0][1]} from {data.get(number)[1][0]} {data.get(number)[1][1]}.\n")
else:
    print("The number was not found.")
