l = [3,4,5,7,8,9,5,2,3,5]

# print(sorted(l))
# l.sort()
# print(l)


# bubble sort
count = 0
for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            count += 1
    print(l)

print(count)


l = [3,4,5,7,8,9,5,2,3,5]

# selection sort
for current in range(len(l)-1):
    min = current
    for i in range(current,len(l)):
        if l[i] < l[min]:
            min = i

    l[min], l[current] = l[current], l[min]
    print(l)

