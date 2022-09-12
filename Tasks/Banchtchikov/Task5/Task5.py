def check_str(str_input: str):
    upperSTR = []
    lowerSTR = []
    while True:
        if str_input != " " and str_input.isalpha():
            break
        else:
            print("Incorrect string")
            str_input = input("Enter new string:\n")
    for i in range(len(str_input)):
        if ord(str_input[i]) in range(65,91):
            upperSTR.append(str_input[i])
        if ord(str_input[i]) in range(97,123):
            lowerSTR.append(str_input[i])
    return print(f"'{len(upperSTR)} upper case, {len(lowerSTR)} lower case'")




def is_prime(number: int):
    while True:
        if number < 0:
            print("Incorrect number")
            number = int(input("Enter number:\n"))
        else:
            break       
    d = 2
    while number % d != 0:
        d += 1
    return print(d == number)
    



def get_ranges(l: list): 
    start = None
    end = None           
    l1 = []
    for i in l:
        if start == None:
            start = i
            end = i
        elif end == i or end + 1 == i:
            end = i
        else:
            l1.append((start, end))
            start = i
            end = i
    l1.append((start, end))
    return l1
        

