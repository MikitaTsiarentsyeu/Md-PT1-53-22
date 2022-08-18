s = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"

#перейти к списку чисел
d = {"one":1, "two":2, "four":4, "five":5, "eight":8, "ten":10, "eleven":11, "thirteen":13, "seventeen":17, "nineteen":19}
l = [d[numeral] for numeral in s.split()]
print(l)

#исключить дубликаты

#отсортировать по возрастанию

print(set(l))
l = list(set(l))
print(l)

# all other interesting stuff

odd_sum = 0
flag = True

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