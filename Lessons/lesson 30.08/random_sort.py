import random
l = [3,2,5,7,4,6,8]

def sort(l):
    counter = 0
    while not is_sorted(l):
        counter += 1
        print(counter)
        swap(l)

def swap(l):
    i = generate_index(l)
    j = i
    while i == j:
        j = generate_index(l)
    l[i], l[j] = l[j], l[i]

def generate_index(l):
    return random.randrange(0, len(l))

def is_sorted(l):
    # return l == sorted(l)
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True


sort(l)
print(l)