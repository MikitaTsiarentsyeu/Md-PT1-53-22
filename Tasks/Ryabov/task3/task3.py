import datetime


d1={0:("полночь", "двенадцатого"), 1:("один", "первого"), 2:("два", "второго"), 3:("три", "третьего"), 4:("четыре", "четвертого"), 5:("пять", "пятого"), 6:("шесть", "шестого"), 7:("семь", "седьмого"), 8:("восемь", "восьмого"), 9:("девять", "девятого"), 10:("десять", "десятого"), 11:("одинадцать", "одинатцатого"), 12:("двенадцать", "дванадцатого"), 13:("один", "первого"), 14:("два", "второго"), 15:("три", "третьего"), 16:("четыре", "четвертого"), 17:("пять", "пятого"), 18:("шесть", "шестого") , 19:("семь", "седьмого"), 20:("восемь", "восьмого"), 21:("девять", "девятого"), 22:("десять", "десятого"), 23:("одинадцать", "одинатцатого")}
d2={1:("одна", "одной"), 2:("две", "двух"), 3:("три", "трех"), 4:("четыре", "четырех"), 5:("пять", "пяти"), 6:("шесть", "шести"), 7:("семь","семи"), 8:("восемь", "восьми"), 9:("девять", "девяти"), 10:("десять", "десяти"), 11:("одинадцать", "одинадцати"), 12:("двенадцать", "двенадцати"), 13:("тринадцать", "тринадцати"), 14:("четырнадцать", "четырнадцати"), 15:("пятнадцать", "пятнадцати"), 16:("шестнадцать", "шестнадцати"), 17:("семнадцать", "семнадцати"), 18:("восемьнадцать", "восемьнадцати") , 19:("девятнадцать", "девятнадцати")}
d3={2:"двадцать", 3:("тридцать"), 4:("сорок"), 5:("пятьдесят")}

z = int(input("enter 1 if you want to enter the time, 0 if you want to display the time automatically"))
if z == int(1):
    t = input("the time hh:mm:\n")

    if ":" not in time or len (time) != 5:
        print ("input the time format hh:mm:\n")

    h, m = t.split(":")
    h=int(h)
    m=int(m)

else:
    current_date_time = datetime.datetime.now()
    current_time = current_date_time.time()
    h =current_time.hour
    m = current_time.minute

if m == 0:
    if h == 1 or h == 13:
        print(f"{d1[h][0]} час ровно")
    elif h >= 5 and h <= 12: 
        print(f"{d1[h][0]} часов ровно")
    elif h >= 17 and h <= 24: 
        print(f"{d1[h][0]} часов ровно")
    elif h == 0:
        print(f"{d1[h][0]}")
    else:
        print(f"{d1[h][0]} часа ровно")

if m > 4 and m < 20:
    print(f"{d2[m][0]} минут {d1[h+1][1]}")
if m > 1 and m < 5:
    print(f"{d2[m][0]} минуты {d1[h+1][1]}")
if m == 1:
    print(f"{d2[m][0]} минута {d1[h+1][1]}")
if m >= 20 and m < 30:
    print(f"{d3[2]} {d2[m%10][0]} минут {d1[h+1][1]}")

if m == 30:    
    print(f"половина {d1[h+1][1]}")

if m == 31:
    print(f"{d3[3]} {d2[m%10][0]} минута {d1[h+1][1]}")
if m > 31 and m < 34:
    print(f"{d3[3]} {d2[m%10][0]} минуты {d1[h+1][1]}")
if m > 34 and m < 40:
    print(f"{d3[3]} {d2[m%10][0]} минут {d1[h+1][1]}")
if m == 40:
    print(f"{d3[4]} минут {d1[h+1][1]}")
if m == 41:
    print(f"{d3[4]} {d2[m%10][0]} минута {d1[h+1][1]}")
if m > 41 and m < 44:
    print(f"{d3[4]} {d2[m%10][0]} минуты {d1[h+1][1]}")
if m >= 45:
    print(f"без {d2[60-m][1]} минут {d1[h+1][0]}")
    


   
    



  



 


    