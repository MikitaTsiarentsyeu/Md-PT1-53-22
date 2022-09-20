
import time

def log(f):
    def wrapper(*args, **kwargs):
        print(f"Function name: {f.__name__}")
        print(f"Function args: {' '.join(map(str, args))}")
        print(f"Function kwargs: {kwargs.items()}")
        start = time.time()
        output = f(*args, **kwargs)
        finish = time.time() - start
        print(f"Function result: {output}")
        print(f"Function time: {finish}")
        return output
    return wrapper

@log
def double(*args, **kwargs):
    args = [x*2 for x in args]
    kwargs = {k:w*2 for k,w in kwargs.items()}
    return args, kwargs
@log
def print_everything(*args, **kwargs):
    [print(x) for x in args]
    [print(x) for x in kwargs.items()]


double(2,3,4,test=5,value=6)

print_everything(2,3,4,test=5,value=6)