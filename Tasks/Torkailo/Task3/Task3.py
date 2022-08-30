# ...IN PROGRESS...

hh_d = {
    1:['один','первого','одной']
    , 2:['два','второго', 'двух', 'двадцать']
    , 3:['три','третьего', 'трех', 'тридцать']
    , 4:['четыре','четвертого','четырех', 'сорок']
    , 5:['пять','пятого']
    , 6:['шесть','шестого']
    , 7:['семь','седьмого']
    , 8:['восемь', 'восьмого']
    , 9:['девять', 'девятого']
    , 10:['десять', 'десятого']
    , 11:['одинадцать','одинадцатого']
    , 12:['двенадцать', 'двенадцатого']
    , 13:['тринадцать', 'тринадцати']
    , 14:['четырнадцать','четырнадцати']
    , 15:['пятнадцать', 'пятнадцати']
    }


# check

hh_mm = str(input('Введите время в формате hh:mm '))
if hh_mm[0:2].isdigit() !=True or hh_mm[3:5].isdigit() !=True or hh_mm[2:3] != ':'  or int(hh_mm[0:2]) > 24 or int(hh_mm[3:5]) >60 or len(hh_mm)!= 5:
    print('Введите время в формате hh:mm ')

else:
    if int(hh_mm[0:2]) - 12 > 0:
        hh = int(hh_mm[0:2]) - 12
    else:
        hh = int(hh_mm[0:2])
    min = int(hh_mm[3:5])

    # min == 0: такое-то значение часа ровно (15:00 - три часа ровно)

    if min == 0 and hh == 1:
        print(f"{hh_d.get(hh)[0]} час ровно")
    if min == 0 and 2 <= hh <= 4:
        print(f"{hh_d.get(hh)[0]} часа ровно")
    if min == 0 and hh >= 5:
        print(f"{hh_d.get(hh)[0]} часов ровно")

    # min == 30: половина такого-то (15:30 - половина четвёртого)

    if min == 30 and hh < 12:
        print(f"половина {hh_d.get(hh+1)[1]}")
    if min == 30 and hh == 12:
        print(f"половина {hh_d.get(hh-12+1)[1]}")

    # min >= 45 без min такого-то (08:54 - без шести минут девять)

    if (60 - min) == 1 and hh < 12:
        print(f"без {hh_d.get(60-min)[2]} минуты {hh_d.get(hh+1)[0]}")
    if (60 - min) == 1 and hh == 12:
       print(f"без {hh_d.get(60-min)[2]} минуты час")

    if (60 - min) <= 4 and hh < 12:
        print(f"без {hh_d.get(60-min)[2]} минут {hh_d.get(hh+1)[0]}")
    if (60 - min) <= 4 and hh == 12:
       print(f"без {hh_d.get(60-min)[2]} минут час")

    if 4 < (60 - min) <= 15 and hh < 12:
        print(f"без {hh_d.get(60-min)[0][:-1]+'и'} минут {hh_d.get(hh+1)[0]}")
    if 4 < (60 - min) <= 15 and hh == 12:
       print(f"без {hh_d.get(60-min)[0][:-1]+'и'} минут час")

    # min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)  
    # min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)

    if min == 1 and hh < 12:
        print(f"одна минута {hh_d.get(hh+1)[1]}")
    if min == 1 and hh == 12:
       print(f"одна минута {hh_d.get(hh-12+1)[1]}")

    if min == 2 and hh < 12:
        print(f"две минуты {hh_d.get(hh+1)[1]}")
    if min == 2 and hh == 12:
       print(f"две минуты {hh_d.get(hh-12+1)[1]}")
    
    if min == 3 and hh < 12:
        print(f"три минуты {hh_d.get(hh+1)[1]}")
    if min == 3 and hh == 12:
       print(f"три минуты {hh_d.get(hh-12+1)[1]}")

    if min == 4 and hh < 12:
        print(f"четыри минуты {hh_d.get(hh+1)[1]}")
    if min == 4 and hh == 12:
       print(f"четыри минуты {hh_d.get(hh-12+1)[1]}")
    
    if 4 < min <= 15 and hh < 12:
        print(f"{hh_d.get(min)[0]} минут {hh_d.get(hh+1)[1]}")
    if 4 < min <= 15 and hh == 12:
       print(f"{hh_d.get(min)[0]} минут {hh_d.get(hh-12+1)[1]}")

    if 15 < min < 20 and hh < 12:
        mm = min % 10
        print(f"{hh_d.get(mm)[0][:-1]+'надцать'} минут {hh_d.get(hh+1)[1]}")
    if 15 < min < 20 and hh == 12:
        mm = min % 10
        print(f"{hh_d.get(mm)[0][:-1]+'надцать'} минут {hh_d.get(hh-12+1)[1]}")

    if 20 <= min < 30 and hh < 12:
        mm = min % 10
        print(f"{hh_d.get(mm)[0][:-1]+'надцать'} минут {hh_d.get(hh+1)[1]}")
    if 20 <= min < 30 and hh == 12:
        mm = min % 10
        print(f"{hh_d.get(mm)[0][:-1]+'надцать'} минут {hh_d.get(hh-12+1)[1]}")