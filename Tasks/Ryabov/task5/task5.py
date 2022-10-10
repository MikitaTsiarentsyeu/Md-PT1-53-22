


def check_str(s):
    d = {'up' : 0, 'lo' : 0}
    if s == '':
        return print('string is empty')
    for i in s:
        if i.isupper():
            d['up']+=1  
        elif i.islower():
            d['lo']+=1   
        else: pass
    return print ("Original String : ", s, "No. of Upper case characters : ", d["up"], "No. of Lower case Characters : ", d["lo"])

check_str('The quick Brown Fox')


def is_prime(x):
    if x % 2 == 0:
        return x == 2 
    y = 3
    while y*y <= x:
        y +=1
    return y*y > x

print(is_prime(8))

def get_rangers(l):
    x = str(l[0])
    
    for i in range(len(l)-1):
        
        
        if l[i]+1 == l[i+1]:
            if x[-1] !='-':
                x +='-'
            else:
                pass

        elif l[i]+1 != l[i+1]:
            if not f'{l[i]}' in x:
                x += f'{l[i]}, {l[i+1]}'
            else:
                x += f', {l[i+1]}'
            

    if x[-1] == '-':
        x += f'{l[-1]}'
    

    return x  

print(get_rangers([1, 2, 3, 4, 7, 8, 10, 12, 13, 15]))  


            
           
    
