import datetime
from ntpath import join

d = {(1, 13):["один", "второго"], (2, 14):["два", "третьего"], (3, 15):["три", "четвертого"], (4, 16):["четыре", "пятого"], (5, 17):["пять", "шестого"], 
(6, 18):["шесть", "седьмого"], (7, 19):["семь", "восьмого"], (8, 20):["восемь", "девятого"], (9, 21):["девять","деcятого"], (10, 22):["десять", "одиннадцатого"], 
(11, 23):["одиннадцать", "двенадцатого"], (12, 24, 00):["двенадцать", "первого"]}


d2 = {1:["одна", "одной"], 2:["две", "двух"], 3:["три", "трех", "тридцать"], 4:["четыре", "четырех", "сорок"], 5:["пять", "пяти"], 6:["шесть", "шести"], 7:["семь", "семи"], 
8:["восемь", "восьми"], 9:["девять", "девяти"], 10:["десять", "десяти"], 11:["одиннадцать", "одиннадцати"], 12:["двенадцать", "двенадцати"], 13:["тринадцать", "тринадцати"], 
14:["четырнадцать", "четырнадцати"], 15:["пятнадцать", "пятнадцати"], 16:["шестнадцать"], 17:["семнадцать"], 18:["восемнадцать"], 19:["девятнадцать"], 
20:["двадцать"]}


q = input("Do you want to enter the time (y/n):\n")

if q == "n":
    
    h = int(str(datetime.datetime.now().time()).split(":")[0])
    m = int(str(datetime.datetime.now().time()).split(":")[1])

elif q == "y":

        while True:
            time = input("Input your time in format hh:mm:\n")
            if len(time) != 5:
                print("Incorrectly data!")
                continue

            if time[2] != ":":
                print("Incorrectly data!")
                continue
            
            if not time.split(":")[0].isdigit():
                print("Incorrectly data!")
                continue

            if not time.split(":")[1].isdigit():
                print("Incorrectly data!")
                continue

            h = int(time.split(":")[0])
            m = int(time.split(":")[1])            
            break

if h >= 0 and h < 24:
    if m == 0:
    
        hh = "".join([d[n][0] for n in d for x in n if x == h])

        if h == 1 or h == 13:
            print(f"{hh} час ровно")
            
        if h > 1 and h < 5 or h > 13 and h < 17:
            print(f"{hh} часа ровно")

        if h > 4 and h < 13 or h > 16 and h < 24 or h == 00:
            print(f"{hh} часов ровно")
        

    if m == 30:
       
        hh = "".join([d[n][1] for n in d for x in n if x == h])
        print(f"половина {hh}")

    if m < 30:

        hh = "".join([d[n][1] for n in d for x in n if x == h])

        if m > 0 and m < 21:

            mm = "".join([d2[n][0] for n in d2 if n ==  m])

            if m == 1:
                print(f"{mm} минута {hh}")
            elif m > 1 and m < 5:
                print(f"{mm} минуты {hh}")
            else:
                print(f"{mm} минут {hh}")

        elif m > 20 and m < 30:

            m2 = int(str([m])[2])
        
            m3 = "" .join([d2[n][0] for n in d2 if n == m2])
            if m2 == 1:
                print(f"двадцать {m3} минутa {hh}")
            elif m2 > 1 and m2 < 5:
                print(f"двадцать {m3} минуты {hh}")
            else:
                print(f"двадцать {m3} минут {hh}")

    if m > 30 and m < 45:

        hh = "".join([d[n][1] for n in d for x in n if x == h])

        m1 = int(str([m])[1])
        m2 = int(str([m])[2])
    
        m1 = "" .join([d2[n][2] for n in d2 if n == m1])
        m3 = "" .join([d2[n][0] for n in d2 if n == m2])
        if m2 == 1:
            print(f"{m1} {m3} минута {hh}")
        elif m2 > 1 and m2 < 5:
            print(f"{m1} {m3} минуты {hh}")
        else:
            print(f"{m1} {m3} минут {hh}")

    if m >= 45:        
        hh = "".join([d[n][0] for n in d for x in n if x == h+1])

        m1 = 60-m
        mm = "".join([d2[n][1] for n in d2 if n == m1])
        if m1 == 1:
            print(f"без {mm} минуты {hh}")
        else:
            print(f"без {mm} минут {hh}")
else:
    print("Incorrect time!")