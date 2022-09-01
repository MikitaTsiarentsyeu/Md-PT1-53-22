x, y = 'x value', 'y value'

def sum(x, y):
    return x+y

def mult(x, y):
    return x*y

print(sum(2, 3))
print(mult(5, 6))
print(x, y)

def evaluate(value1, value2, value3):
    return value1+value2*value3

print(evaluate(2,3,4))
print(evaluate(value2=2,value3=3,value1=4))
print(evaluate(2,value3=3,value2=4))

def send_email(from_name, to_name="smbd@gmail.com", text="greetimgs. friend!"):
    print(f"sending an email from {from_name} to {to_name} with text '{text}'")

send_email("test@te.st", "smbd@gmail.com", "greetimgs. friend!")
send_email("test@te.st")
send_email("test@te.st", text="hello again!")

print(1,2,3,4,5,6,7,8,9)

def sum(*args):
    print(args, type(args))
    res = 0
    for i in args:
        res+=i
    return res

print(sum(1,2,3,4,5,6,7,8,9))
l = [4,5,6,7]
print(sum(*l))
print(*l)


def sum(**kwargs):
    print(kwargs, type(kwargs))
    res = 0
    for k, v in kwargs.items():
        res += v
    return res


print(sum(value1=2, value2=1, x=3, y=6))

def my_print(*args, **kwargs):
    print(*args, sep=kwargs['sep'], end=kwargs['end'])

my_print(1,2,3,4,5,6,7,8,9,10,sep=',',end='.\n')

def my_print(x, y, *args, **kwargs):
    print(x, y)
    print(*args, sep=kwargs['sep'], end=kwargs['end'])

my_print(1,2,2,3,3,4,4,5,5,6,sep=',',end='.\n')