l = [1,2,3]

# def outer_error_f():
#     error_f()

# def error_f():
#     raise NameError("name error from error_f function")

# outer_error_f()

try:
    raise NameError("something went wrong")
    print("before the error")
    print(new_var)
    print(l[100])
    print("after the error")
except (IndexError, ZeroDivisionError):
    print("incorrect index was used or somethin was divided by zero")
except NameError as error:
    print(error)
    try:
        print("the variable does not exist")
        4/0
    except:
        print("inner error")
except:
    print("something went wrong")
else:
    print("")
finally:
    print("this part runs in every situation")


print("the end")

# with open("test.txt") as f:
#     f.read()

# try:
#     f = open("test.txt")
#     f.read()
# finally:
#     f.close()