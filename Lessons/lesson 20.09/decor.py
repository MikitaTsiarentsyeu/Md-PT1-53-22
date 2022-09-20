from datetime import datetime

def do_twice(f):
    def wrapper():
        f()
        f()
    return wrapper

def comment(f):
    def wrapper():
        print("the function started")
        f()
        print("the function was executed")
    return wrapper

@do_twice
@comment
def print_hello():
    print("hello")



@comment
@do_twice
def print_time():
    print(datetime.now())

print_hello()
print("----------------")
print_time()