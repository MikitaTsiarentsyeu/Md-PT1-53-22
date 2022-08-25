
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 5 == 0:
        print ("Buzz")
    elif x % 3 == 0:
        print("Fizz")  
    else:
        print(x)
    
for x in range(0, 100):
    print(("fizz"*(x%3 == 0) + "buzz"*(x%5 ==0)) or x)

[print(("fizz"*(x%3 == 0) + "buzz"*(x%5 ==0)) or x) for x in range(0, 100)]