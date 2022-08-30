import datetime

hh_data = {
    1:['один','первого']
    , 2:['два','второго']
    , 3:['три','третьего']
    , 4:['четыре','четвертого']
    , 5:['пять','пятого']
    , 6:['шесть','шестого']
    , 7:['семь','седьмого']
    , 8:['восемь', 'восьмого']
    , 9:['девять', 'девятого']
    , 10:['десять', 'десятого']
    , 11:['одинадцать','одинадцатого']
    , 12:['двенадцать', 'двенадцатого']
      }

mm_data = {
    1:['одна','одной']
    , 2:['две','двух']
    , 3:['три','трех']
    , 4:['четыре','четырех']
    , 5:['пять','пяти']
    , 6:['шесть','шести']
    , 7:['семь','семи']
    , 8:['восемь', 'восьми']
    , 9:['девять', 'девяти']
    , 10:['десять', 'десяти']
    , 11:['одинадцать','одинадцати']
    , 12:['двенадцать', 'двенадцати']
    , 13:['тринадцать','тринадцати']
    , 14:['четырнадцать','четырнадцати']
    , 15:['пятнадцать','пятнадцати']
    , 20:['двадцать', 'двадцати']
    , 30:['тридцать', 'тридцати']
    , 40:['сорок', 'сорока']
      }

str_data = {
    1:['час','минута']
    , 2:['часа','минуты']
    , 3:['часа','минуты']
    , 4:['часа','минуты']
    , 0:['часов','минут']
}
# check

print('Select the option \nEnter 1 or 2 \n1 - Current time\n2 - Entered time')

while True:
    option = input('\nChoose the option: ')
    if option == '1' or option == '2':
        break
    else:
        print('\tError: try again')

if option == '1':
    hh_mm = datetime.datetime.now().strftime("%H:%M")
else:
    while True:
        try:
            hh_mm = str(input('Enter time in format hh:mm '))
            if hh_mm[0:2].isdigit() ==True and hh_mm[3:5].isdigit() ==True and hh_mm[2:3] == ':' and int(hh_mm[0:2]) < 24 and int(hh_mm[3:5]) <60 and len(hh_mm)== 5:
                break
            else:
                print("\nError: Enter time in format hh:mm")
        except ValueError:
            print("\nError: Enter time in format hh:mm")

if int(hh_mm[0:2]) - 12 > 0:
     hh = int(hh_mm[0:2]) - 12
else:
    hh = int(hh_mm[0:2])
min = int(hh_mm[3:5])

 # min == 0: такое-то значение часа ровно (15:00 - три часа ровно)

if min == 0 and hh == 1:
    print(f"{hh_data.get(hh)[0]} {str_data.get(hh)[0]} ровно")
if min == 0 and 2 <= hh <= 4:
     print(f"{hh_data.get(hh)[0]} {str_data.get(hh)[0]} ровно")
if min == 0 and hh >= 5:
    print(f"{hh_data.get(hh)[0]} {str_data.get(0)[0]} ровно")

# min == 30: половина такого-то (15:30 - половина четвёртого)

if min == 30 and hh < 12:
    print(f"половина {hh_data.get(hh+1)[1]}")
if min == 30 and hh == 12:
     print(f"половина {hh_data.get(hh-12+1)[1]}")

# min >= 45 без min такого-то (08:54 - без шести минут девять)

if (60 - min) == 1 and hh < 12:
    print(f"без {mm_data.get(60-min)[1]} {str_data.get((60 - min))[1]} {hh_data.get(hh+1)[0]}")
if (60 - min) == 1 and hh == 12:
    print(f"без {mm_data.get(60-min)[1]} {str_data.get((60 - min))[1]} {hh_data.get(1)[0]}")

if 2 < (60 - min) <= 15 and hh < 12:
    print(f"без {mm_data.get(60-min)[1]} {str_data.get(0)[1]} {hh_data.get(hh+1)[0]}")
if 2 < (60 - min) <= 15 and hh == 12:
    print(f"без {mm_data.get(60-min)[1]} {str_data.get(0)[1]} {hh_data.get(1)[0]}")

# min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)  
# min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)

if 1 <= min <= 4 and hh < 12:
     print(f"{mm_data.get(min)[0]} {str_data.get(min)[1]} {hh_data.get(hh+1)[1]}")
if 1 <= min <= 4 and hh == 12:
    print(f"{mm_data.get(min)[0]} {str_data.get(min)[1]} {hh_data.get(hh-12+1)[1]}")

if 4 < min <= 15 and hh < 12:
    print(f"{mm_data.get(min)[0]} {str_data.get(0)[1]} {hh_data.get(hh+1)[1]}")
if 4 < min <= 15 and hh == 12:
    print(f"{mm_data.get(min)[0]} {str_data.get(0)[1]} {hh_data.get(hh-12+1)[1]}")

if 15 < min < 20 and hh < 12:
    mm = min % 10
    print(f"{mm_data.get(mm)[0][:-1]+'надцать'} {str_data.get(0)[1]} {hh_data.get(hh+1)[1]}")
if 15 < min < 20 and hh == 12:
    mm = min % 10
    print(f"{mm_data.get(mm)[0][:-1]+'надцать'} {str_data.get(0)[1]} {hh_data.get(hh-12+1)[1]}")

if  (min == 20 or min == 40) and hh < 12:
    print(f"{mm_data.get(min)[0]} {str_data.get(0)[1]} {hh_data.get(hh+1)[1]}")
if (min == 20 or min == 40)  and hh == 12:
    print(f"{mm_data.get(min)[0]} {str_data.get(0)[1]} {hh_data.get(hh-12+1)[1]}")
    
if 20 < min < 45 and hh < 12 and min % 10 <=4:
    m =  min // 10*10
    mm = min % 10
    print(f"{mm_data.get(m)[0]} {mm_data.get(mm)[0]} {str_data.get(mm)[1]} {hh_data.get(hh+1)[1]}")
if 20 < min < 45 and hh == 12 and min % 10 <=4:
    m =  min // 10*10
    mm = min % 10
    print(f"{mm_data.get(m)[0]} {mm_data.get(mm)[0]} {str_data.get(mm)[1]} {hh_data.get(hh-12+1)[1]}")

if 20 < min < 45 and hh < 12 and min % 10 >4:
    m =  min // 10*10
    mm = min % 10
    print(f"{mm_data.get(m)[0]} {mm_data.get(mm)[0]} {str_data.get(0)[1]} {hh_data.get(hh+1)[1]}")
if 20 < min < 45 and hh == 12 and min % 10 >4:
    m =  min // 10*10
    mm = min % 10
    print(f"{mm_data.get(m)[0]} {mm_data.get(mm)[0]} {str_data.get(0)[1]} {hh_data.get(hh-12+1)[1]}")