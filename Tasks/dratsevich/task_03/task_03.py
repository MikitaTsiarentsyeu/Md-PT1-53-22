import datetime

hours_map = {0: ['двеннадцать', 'двеннадцатого'], 1: ['час', 'первого'], 2: ['два', 'второго'], 3: ['три', 'третьего'],
             4: ['четыре', 'четвертого'],
             5: ['пять', 'пятого'], 6: ['шесть', 'шестого'], 7: ['семь', 'седьмого'], 8: ['восемь', 'восьмого'],
             9: ['девять', 'девятого'], 10: ['десять', 'десятого'], 11: ['одиннадцать', 'одиннадцатого'],
             12: ['двеннадцать', 'двеннадцатого'], }

minutes_map = {1: ['одна', 'одной'], 2: ['две', 'двух'], 3: ['три', 'трех'], 4: ['четыре', 'четырех'],
               5: ['пять', 'пяти'], 6: ['шесть', 'шести'], 7: ['семь', 'семи'], 8: ['восемь', 'восьми'],
               9: ['девять', 'девяти'], 10: ['десять', 'десяти'], 11: ['одиннадцать', 'одиннадцати'],
               12: ['двеннадцать', 'двеннадцати'], 13: ['тринадцать', 'тринадцати'],
               14: ['четырнадцать', 'четырнадцати'], 15: ['пятнадцать', 'пятнадцати'],
               16: ['шестнадцать', ], 17: ['семнадцать', ],
               18: ['восемнадцать', ], 19: ['девятнадцать', ],
               20: ['двадцать', ], 30: ['тридцать', ], 40: ['сорок', ], 50: ['пятьдесят', ], }
mode = input('1.текстовый вывод текущего времени\n'
             '2.текстовый вывод времени, введённого с консоли (пользователь должен вводить данные в формате hh:mm).\n'
             'Press 1 or 2\n')

while True:
    if mode == '1':
        current_time = str(datetime.datetime.now())[11:16]
        break
    elif mode == '2':
        current_time = input('input time in format hh:mm\n')
        break
    else:
        mode = input('Wrong input! Press 1 or 2\n')

while True:
    hours = current_time[:2]
    minutes = current_time[3:]
    if len(current_time) != 5 or not hours.isdigit() or not minutes.isdigit() or int(
            minutes) >= 60 or int(hours) >= 24:
        current_time = input('wrong input, try again\n')
    else:
        break

hours = int(hours)
minutes = int(minutes)

# cast to 12h format
if hours > 12:
    hours = hours - 12
if hours == 12:
    hours = 0

# main logic

# min==0
# 1 час, 2-4 часа,  5-12 часов
if minutes == 0:
    if hours == 1:
        print(f'{hours_map[hours][0]} ровно')
    elif 2 <= hours <= 4:
        print(f'{hours_map[hours][0]} часа ровно')
    elif 5 <= hours <= 12 or hours == 0:
        print(f'{hours_map[hours][0]} часов ровно')

# min == 30
elif minutes == 30:
    if hours == 12:
        hours = 0
    print(f'половина {hours_map[hours + 1][1]}')

# min == 45-60
elif 45 <= minutes < 60:
    if minutes == 59:
        print(f'без {minutes_map[60 - minutes][1]} минуты {hours_map[hours + 1][0]}')
    else:
        print(f'без {minutes_map[60 - minutes][1]} минут {hours_map[hours + 1][0]}')
# min 1-29, 31-44
# 1 минута, 2-4 минуты, 5-... минут, 21,31,41 минута

else:
    if minutes == 1:
        print(f'{minutes_map[minutes][0]} минута {hours_map[hours + 1][1]}')
    elif 2 <= minutes <= 4:
        print(f'{minutes_map[minutes][0]} минуты {hours_map[hours + 1][1]}')
    elif 5 <= minutes <= 20:
        print(f'{minutes_map[minutes][0]} минут {hours_map[hours + 1][1]}')
    elif 22 <= minutes <= 29:
        print(f'{minutes_map[20][0]} {minutes_map[minutes - 20][0]} минут {hours_map[hours + 1][1]}')
    elif 32 <= minutes <= 39:
        print(f'{minutes_map[30][0]} {minutes_map[minutes - 30][0]} минут {hours_map[hours + 1][1]}')
    elif minutes == 40:
        print(f'{minutes_map[40][0]} минут {hours_map[hours + 1][1]}')
    elif 42 <= minutes <= 44:
        print(f'{minutes_map[40][0]} {minutes_map[minutes - 40][0]} минут {hours_map[hours + 1][1]}')
    elif minutes == 21:
        print(f'{minutes_map[20][0]} {minutes_map[minutes - 20][0]} минута {hours_map[hours + 1][1]}')
    elif minutes == 31:
        print(f'{minutes_map[20][0]} {minutes_map[minutes - 20][0]} минута {hours_map[hours + 1][1]}')
    elif minutes == 41:
        print(f'{minutes_map[20][0]} {minutes_map[minutes - 20][0]} минута {hours_map[hours + 1][1]}')
