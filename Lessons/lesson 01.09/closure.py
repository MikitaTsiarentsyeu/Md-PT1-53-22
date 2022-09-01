def maker(n, isPow=True):
    def action(x):
        if isPow:
            return x**n
        else:
            return x*n
    return action

def pw(x, y):
    return x**y

sq = maker(2)
print(sq, type(sq))
print(sq(3), sq(4), sq(5))
cube = maker(3)
print(cube(3), cube(4), cube(5))
for i in range(10):
    print(maker(i, False)(2))
