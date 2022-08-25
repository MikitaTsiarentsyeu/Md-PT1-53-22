""""
{9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

дана структура данных, нужно дать пользователю возможность искать по номеру телефона
вывод в случае совпадения - "{имя} {фамилия} from {город}, {штат}"
в случае несовпадения - "the number was not found"

предусмотреть валидацию по длине введённой строки и по её символам (должны быть числа) 
"""
from types import NoneType


d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

ph_num = input("Enter phone number ")

if ph_num.isdigit() !=True or len(ph_num)!= 10:
    print("Enter integer number with 10 symbols length")
elif d.get(int(ph_num)) == None:
    print("Phone number wasn't found")
else:
    ph_num = int(ph_num)
    print (f"{d.get(ph_num)[0][0]} {d.get(ph_num)[0][1]} from {d.get(ph_num)[1][0]}, {d.get(ph_num)[1][1]}.")

