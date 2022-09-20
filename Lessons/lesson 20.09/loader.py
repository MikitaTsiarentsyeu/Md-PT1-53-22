import timer

timer.finish()
timer.start()

for i in range(10000000):
    i=i*i

print(timer.finish())