"""Реализовать:
1.текстовый вывод текущего времени
2.текстовый вывод времени, введённого с консоли (пользователь должен вводить данные в формате hh:mm).
Дать пользователю возможность выбрать режим работы программы, время выводить числительными на русском языке.

Для получения текущего времени использовать модуль datetime.

min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
min == 30: половина такого-то (15:30 - половина четвёртого)
min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
min >= 45 без min такого-то (08:54 - без шести минут девять)"""

import datetime

data_hour = {1:["один", "первого"],2:["два", "второго"],3:["три", "третьего"],4:["четыре", "четвертого"],5:["пять", "пятого"],
6:["шесть", "шестого"],7:["семь", "седьмого"],8:["восемь", "восьмого"],9:["девять", "девятого"],10:["десять", "десятого"],
11:["одиннадцать", "одиннадцатого"],12:["двенадцать", "двенадцатого"],0:["двенадцать", "двенадцатого"]}
data_minute = {1:["одна", "одной"],2:["две", "двух"],3:["три", "трёх"],4:["четыри", "четырёх"],5:["пыть", "пяти"],6:["шесть", "шести"],
7:["семь", "семи"],8:["восемь", "восьми"],9:["девять", "девяти"],10:["десять", "десяти"],11:["одиннадцать", "одиннадцати"],
12:["двенадцать", "двенадцати"],13:["тринадцать", "тринадцати"],14:["четырнадцать", "четырнадцати"],15:["пятнадцать", "пятнадцати"],
16:["шестнадцать", "шестнадцати"],17:["семнадцать", "семнадцати"],18:["восемнадцать", "восемнадцати"],19:["девятнадцать", "девятнадцати"],
20:"двадцать",30:"тридцать",40:"сорок"}

def validation_check(user_time):
    try:
        datetime.datetime.strptime(user_time, '%H:%M')
    except:
        return "Invalid input format.\n"

print("Do you want to enter time?") 
while True:
    ct = input("Please enter Y (yes) or N (no) \n")
    if (ct.lower().strip() == "y" or ct.lower().strip() == "n"):
        break

if (ct.lower().strip() == "y"):    
    while True:
            user_time = input("Please enter time in hh:mm format:\n")
            validation = validation_check(user_time)
            if validation:
                print (validation)
                continue
            else:
                break  
    hh = int(user_time.split(":")[0]) 
    mm = int(user_time.split(":")[1])    
else:
    hh = datetime.datetime.now().hour
    mm = datetime.datetime.now().minute
    
if hh >= 12:
    hh -= 12

if mm == 0:
    if hh == 1:
        print(f"{data_hour[hh][0]} час ровно")
    elif hh>=2 and hh<5:
        print(f"{data_hour[hh][0]} часа ровно")
    else:
        print(f"{data_hour[hh][0]} часов ровно")
elif mm < 20:
    print(f" {data_minute[mm][0]} минут {data_hour[hh+1][1]}")
elif mm == 30:
    print(f"половина {data_hour[hh+1][1]}")
elif mm >= 20 and mm < 45: 
    if mm == 20 or mm == 40:
        print(f" {data_minute[mm]} минут {data_hour[hh+1][1]}")
    else:
        print(f" {data_minute[mm-mm%10]} {data_minute[mm%10][0]} минут {data_hour[hh+1][1]}")
elif mm >= 45: 
    mm = 60 - mm
    if mm == 1:
        print(f"без {data_minute[mm][1]} минуты {data_hour[hh+1][0]}")
    else:
        print(f"без {data_minute[mm][1]} минут {data_hour[hh+1][0]}")














# print(hh,mm)
# print(user_time.split(":")[0], type(user_time.split(":")[0]))