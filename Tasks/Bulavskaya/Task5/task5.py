def check_str(s: str):
    lower=0
    upper=0
    for i in s:
        if i.islower():
            lower+=1

        if i.isupper():
            upper+=1

    return print(f"{upper} upper case, {lower} lower case")

def is_prime(x: int):
    y = 2
    while x % y != 0:
        y+=1

        if y == x:
            return True
    
    return False


def get_ranges(l):
    x = [l[0]]
    y = []
    for i in range(len(l)-1):
   
        if l[i+1]-l[i] != 1:
            x.append(l[i+1])
            y.append(l[i])
    y.append(l[-1])

    return ",".join([f"{x[i]}" if x[i] == y[i]  else (f"{x[i]}-{y[i]}") for i in range(len(x))])




            
 




        






