import datetime
hours = {0 : ["двенадцатого","двенадцать", "двенадцать часов ровно"], 1 : ["первого","час","час ровно"], 2 : ["второго","два","два часа ровно"], 3 : ["третьего","три","три часа ровно"], 4 : ["четвертого","четыре", "четыре часа ровно"],
5 : ["пятого","пять","пять часов ровно"], 6 : ["шестого","шесть", "шесть часов ровно"], 7 : ["седьмого","семь","семь часов ровно"], 8 : ["восьмого","восемь","восемь часов ровно"], 9 : ["девятого","девять","девять часов ровно"],
10 : ["десятого","десять","десять часов ровно"], 11 : ["одиннадцатого","одиннадцать","одиннадцать часов ровно"], 12 : ["двенадцатого","двенадцать", "двенадцать часов ровно"]}
minutes = {1: ["одна", "одной"], 2: ["две", "двух"], 3: ["три", "трех"], 4: ["четыре", "четырех"],5: ["пять", "пяти"], 6: ["шесть", "шести"], 7: ["семь", "семи"], 8: ["восемь", "восьми"],9: ["девять", "девяти"], 10: ["десять", "десяти"], 
11: ["одиннадцать", "одиннадцати"], 12: ["двеннадцать", "двеннадцати"], 13: ["тринадцать", "тринадцати"], 14: ["четырнадцать", "четырнадцати"], 15: ["пятнадцать", "пятнадцати"], 16: ["шестнадцать", ], 17: ["семнадцать", ], 18: ["восемнадцать", ], 
19: ["девятнадцать", ], 20: "двадцать", 30: "тридцать", 40: "сорок", 50: "пятьдесят"}
input_type = input("Enter 1 or 2:\n"
"1 for Text output of the current time. 2 for text output of the time entered from the console (in format hh:mm)\n")

# 1 or 2
while True:
    if input_type == "1":
        current_time1 = datetime.datetime.now()
        hour = int(current_time1.time().strftime("%H"))
        minute = int(current_time1.time().strftime("%M"))

        # Condition

        if hour > 12:
            hour = hour - 12
        if hour == 12:
            hour = 0
        if minute == 0:
            print(f"Current time is: {hours[hour][2]}")
            break
        elif minute == 30:
            print(f"Current time is: половина {hours[hour + 1][0]}")
            break
        elif minute == 20 or minute == 40:
            print(f"Current time is: {minutes[minute]} минут {hours[hour + 1][0]}")
            break
        elif minute == 21:
            print(f"Current time is: {minutes[20]} {minutes[minute - 20][0]} минута {hours[hour + 1][0]}")
            break
        elif minute == 31:
            print(f"Current time is: {minutes[30]} {minutes[minute - 30][0]} минута {hours[hour + 1][0]}")
            break
        elif minute == 41:
            print(f"Current time is: {minutes[40]} {minutes[minute - 40][0]} минута {hours[hour + 1][0]}")
            break
        elif 2 <= minute <= 4:
            print(f"Current time is: {minutes[minute][0]} минуты {hours[hour + 1][0]}")
        elif 5 < minute < 20:
            print(f"Current time is: {minutes[minute][0]} минут {hours[hour + 1][0]}")
            break
        elif 22 <= minute < 30:
            if 22 <= minute <= 24:
                print(f"Current time is: {minutes[20]} {minutes[minute - 20][0]} минуты {hours[hour + 1][0]}")
            else:
                print(f"Current time is: {minutes[20]} {minutes[minute - 20][0]} минут {hours[hour + 1][0]}")
                break
        elif 32 <= minute < 40:
            if 32 <= minute <= 34:
                print(f"Current time is: {minutes[30]} {minutes[minute - 30][0]} минуты {hours[hour + 1][0]}")
            else:
                print(f"Current time is: {minutes[30]} {minutes[minute - 30][0]} минут {hours[hour + 1][0]}")
                break
        elif 42 <= minute <= 44:
            print(f"Current time is: {minutes[40]} {minutes[minute - 40][0]} минуты {hours[hour + 1][0]}")
        elif 45 <= minute <= 59:
            if minute == 59:
                print(f"Current time is: без одной минуты {hours[hour + 1][1]}")
                break
            else:
                print(f"Current time is: без {minutes[60 - minute][1]} минут {hours[hour + 1][1]}")
                break
        break

    elif input_type == "2":
        current_time = input("Enter time in format hh:mm\n")

        # Verification

        if len(current_time) == 5 and ":" in current_time and current_time.split(":")[0].isdigit() and current_time.split(":")[1].isdigit() and 0 <= int(current_time.split(":")[0]) <= 24 and 0 <= int(current_time.split(":")[1]) <= 59:
            current_time = current_time.split(":")
            hour = current_time[0]
            minute = current_time[1]
        else:
            print("Incorrect time format")
            break
        hour = int(hour)
        minute = int(minute)
        
        # Condition
        
        if hour > 12:
            hour = hour - 12
        if hour == 12:
            hour = 0
        if minute == 0:
            print(f"Current time is: {hours[hour][2]}")
            break
        elif minute == 30:
            print(f"Current time is: половина {hours[hour + 1][0]}")
            break
        elif minute == 20 or minute == 40:
            print(f"Current time is: {minutes[minute]} минут {hours[hour + 1][0]}")
            break
        elif minute == 21:
            print(f"Current time is: {minutes[20]} {minutes[minute - 20][0]} минута {hours[hour + 1][0]}")
            break
        elif minute == 31:
            print(f"Current time is: {minutes[30]} {minutes[minute - 30][0]} минута {hours[hour + 1][0]}")
            break
        elif minute == 41:
            print(f"Current time is: {minutes[40]} {minutes[minute - 40][0]} минута {hours[hour + 1][0]}")
            break
        elif 2 <= minute <= 4:
            print(f"Current time is: {minutes[minute][0]} минуты {hours[hour + 1][0]}")
        elif 5 < minute < 20:
            print(f"Current time is: {minutes[minute][0]} минут {hours[hour + 1][0]}")
            break
        elif 22 <= minute < 30:
            if 22 <= minute <= 24:
                print(f"Current time is: {minutes[20]} {minutes[minute - 20][0]} минуты {hours[hour + 1][0]}")
            else:
                print(f"Current time is: {minutes[20]} {minutes[minute - 20][0]} минут {hours[hour + 1][0]}")
                break
        elif 32 <= minute < 40:
            if 32 <= minute <= 34:
                print(f"Current time is: {minutes[30]} {minutes[minute - 30][0]} минуты {hours[hour + 1][0]}")
            else:
                print(f"Current time is: {minutes[30]} {minutes[minute - 30][0]} минут {hours[hour + 1][0]}")
                break
        elif 42 <= minute <= 44:
            print(f"Current time is: {minutes[40]} {minutes[minute - 40][0]} минуты {hours[hour + 1][0]}")
        elif 45 <= minute <= 59:
            if minute == 59:
                print(f"Current time is: без одной минуты {hours[hour + 1][1]}")
                break
            else:
                print(f"Current time is: без {minutes[60 - minute][1]} минут {hours[hour + 1][1]}")
                break
        break
    else:
        input_type = input("Incorrect input, enter 1 or 2:\n")

