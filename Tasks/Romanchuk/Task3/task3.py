from datetime import datetime

data = {0: ['двенадцать'], 1: ['одна', 'одной', 'первого'], 2: ['две', 'двух', 'второго', 'два'],
        3: ['три', 'трёх', 'третьего'], 4: ['четыре', 'четырёх', 'четвёртого'], 5: ['пять', 'пяти', 'пятого'],
        6: ['шесть', 'шести', 'шестого'], 7: ['семь', 'семи', 'седьмого'], 8: ['восемь', 'восьми', 'восьмого'],
        9: ['девять', 'девяти', 'девятого'], 10: ['десять', 'десяти', 'десятого'],
        11: ['одиннадцать', 'одиннадцати', 'одиннадцатого'], 12: ['двенадцать', 'двенадцати', 'двенадцатого'],
        13: ['тринадцать', 'тринадцати'], 14: ['четырнадцать', 'четырнадцати'], 15: ['пятнадцать', 'пятнадцати'],
        16: ['шестнадцать'], 17: ['семнадцать'], 18: ['восемнадцать'], 19: ['девятнадцать'], 20: ['двадцать'],
        30: ['тридцать'], 40: ['сорок']}

print('\n\t\tMENU\n1. Output the current time\n2. Output the entered time')

while True:
    option = input('\nChoose the option: ')
    if option == '1' or option == '2':
        break
    else:
        print('\tThere is no such option')

if option == '1':
    hour, minute = datetime.now().strftime("%H:%M").split(':')
else:
    while True:
        try:
            hour, minute = input('\nEnter the time (hh:mm): ').split(':')
            if hour.isdigit() and minute.isdigit() and -1 < int(hour) < 24 and -1 < int(minute) < 60:
                break
            else:
                print("\tInput Error: Impossible time value")
        except ValueError:
            print("\tInput Error: Incorrect format")

hour, minute = int(hour), int(minute)
hour = hour - 12 if hour >= 12 else hour

if minute % 10 == 1 and minute < 45:
    minute_str = 'минута'
elif (1 < minute % 10 < 5 and minute < 45) or minute == 59:
    minute_str = 'минуты'
else:
    minute_str = 'минут'

if minute == 0:
    if hour == 1:
        print(f'час ровно')
    elif hour == 2:
        print(f'{data[hour][3]} часа ровно')
    elif 2 < hour < 5:
        print(f'{data[hour][0]} часа ровно')
    else:
        print(f'{data[hour][0]} часов ровно')
elif minute == 30:
    print(f'половина {data[hour + 1][2]}')
elif 0 < minute < 21 or minute == 40:
    print(f'{data[minute][0]} {minute_str} {data[hour + 1][2]}')
elif 20 < minute < 45:
    print(f'{data[minute - minute % 10][0]} {data[minute % 10][0]} {minute_str} {data[hour + 1][2]}')
else:
    if hour == 0:
        print(f'без {data[60 - minute][1]} {minute_str} час')
    elif hour == 1:
        print(f'без {data[60 - minute][1]} {minute_str} {data[hour + 1][3]}')
    else:
        print(f'без {data[60 - minute][1]} {minute_str} {data[hour + 1][0]}')
