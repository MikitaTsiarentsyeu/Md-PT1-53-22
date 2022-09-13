while True:

   str_length = input('Input the lenght of line (must be more than 35 elements:\n')
   if str_length.isdigit():
        if int(str_length) > 35 :
            str_length = int(str_length)
            break
        else:
            print('The length of line must be more than 35 elements')
   else:
        print('Input only digits')
  
with open('text.txt','r', encoding= 'utf-8') as f:
    line = f.readlines()
with open('new_text.txt','w',encoding= 'utf-8') as f:
    text = " "
    counter = 0
    for i in line:
        for j in i.split():
            new_count = counter+len(j)
            if counter !=0:
                new_count +=1
            if new_count >= str_length :
                text += "\n"
                counter = 0
            if counter !=0:
                text += ' '
                counter += 1 
            text += j
            counter += len(j)
    txt_new = text.split('\n')
    for l in txt_new: 
       count = l.count(' ')
       if len(l) < str_length and count !=0:
            miss = str_length-len(l)
            ratio = miss//count
            rem = miss%count
            if ratio > 0:
                l=l.replace(' ',(' ') + (' ') *ratio)
            if rem > 0:
                l=l.replace((' ') + (' ') *ratio,(' ') + (' ')*ratio + (' '),rem)
            l = l + '\n'
            f.writelines(l)
print("'new_text.txt'is ready!")