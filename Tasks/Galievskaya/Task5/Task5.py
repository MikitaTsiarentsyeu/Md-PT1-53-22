"""1. Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию о количестве букв в верхнем и нижнем регистре.
check_str('The quick Brown Fox') -> '3 upper case, 13 lower case'
2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.
is_prime(787) -> True
is_prime(777) -> False
3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
отсортированных по возрастанию, и которая этот список “сворачивает” в набор отрезков."""


def check_str(str): 
    lower = 0
    upper = 0
    for i in str:
        if i.islower():
            lower+=1
        elif i.isupper():
            upper += 1
    return print(f"{upper} upper case, {lower} lower case\n")

def is_prime(number):
    counter = 0
    for i in range (2, number// 2):
        if number%i == 0:
            counter += 1
            break
    if counter == 0:
        return print("True\n")
    else:
        return print("False\n")

def get_ranges(list): 
    res = []
    start = 0 
    print(len(list))
    print(list)
    for i in range(len(list)):        
        if i == len(list)-1 or (list[i+1]-list[i]) != 1:
            if start == i:
                res.append(list[start])
            else:
                res.append(f"{list[start]}-{list[i]}")
            start = i+1
    return print(res)







"""Вдруг мы реально будем что-то вводить, тогда нужно раскомментить)) """

# def validation_str(str):
#     try:
#         if len(str) == "":
#             raise RuntimeError ("Invalid.\n")
#     except RuntimeError as error:
#         return error

# while True:
#     str = input("Enter string: \n")
#     validation = validation_str(str)
#     if validation:
#         print (validation)
#         continue
#     else:
#         break

# def validation_int(number):
#     try:
#         int(number)
#         if int(number) <= 0:
#             raise RuntimeError ("Invalid number.\n")
#     except (ValueError, RuntimeError):
#         return "Invalid number.\n"

# while True:
#     number = input("Enter number more then 0: \n")
#     validation = validation_int(number)
#     if validation:
#         print (validation)
#         continue
#     else:
#         number = int(number)
#         break

# def validation_list(list1):
#     try:
#         list1 = sorted(list(set(list1.split(","))))
#         if len(list1) == 0:
#             raise RuntimeError ("Empty list.\n")
#         for i in range(len(list1)-1):
#             if list1[i].isdigit() != True:
#                 raise ValueError ("Invalid data entered.\n")
#     except RuntimeError as error:
#         return error
#     except ValueError as error:
#         return error

# while True:
#     list1 = input("Enter list (separated by a space): \n")
#     validation = validation_list(list1)
#     if validation:
#         print (validation)
#         continue
#     else:  
#         list1 = list(set(list1.split(",")))      
#         for i in range(len(list1)):
#             list1[i]=int(list1[i])
#         list1 = sorted(list1)
#         break

check_str('The quick Brown Fox')
# check_str(str)

is_prime(787)
is_prime(777)
# is_prime(number)

get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4,7,10])
get_ranges([2, 3, 8, 9])
# get_ranges(list1)