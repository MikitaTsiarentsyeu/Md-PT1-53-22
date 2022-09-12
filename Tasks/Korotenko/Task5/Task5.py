def check_str(str): 
    counter_upper = 0
    counter_lower = 0
    for i in str:
        if i.isupper():
            counter_upper +=1
        if i.islower():
            counter_lower +=1
    return print(f'{counter_upper} upper case, {counter_lower} lower case')
check_str('VAdimKorotenko') #=> 3 upper case, 11 lower case

def is_prime(x: int):
    count = 0
    for i in range(2, x // 2+1):
        if (x % i == 0):
            count = count+1
    if (count <= 0):
        print("True")
    else:
        print("False")
is_prime(5) #is_prime

def get_ranges(lst):
    x = y = None                # x - start range, y - finish range
    new_list = []
    for i in lst:
        if x is None:
            x = y = i
        elif i == y or i == y + 1:
            y = i
        else:
            new_list.append((x, y))
            x = y = i
    if x is not None:
        new_list.append((x, y))
    return new_list
print(get_ranges([1,2,3,4,7,8,10,11]))