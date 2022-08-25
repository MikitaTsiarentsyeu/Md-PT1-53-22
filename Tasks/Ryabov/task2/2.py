s = "five four ten twenty sixteen fifteen eleven ten six four"
d= {"five":5, "four":4, "ten": 10, "twenty":12, "sixteen":16, "fifteen":15, "eleven":11, "six":6}

l=[d[x] for x in s.split()]
print(l)

#for x in s.split():
    #l=d[x]
    #print(l)

l=sorted(l)
print(l)
l=list(set(l))
print(l)

flag = True
odd_sum =0 
for i in range(len(l)):
    if l[i] % 2 == 1:
        odd_sum += l[i]
    if i == len(l)-1:
        break
    if flag:
        print(l[i]+l[i+1])
    else:
        print(l[i]*l[i+1])
    flag = not flag

print(odd_sum)

    

