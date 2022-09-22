    
while True:
    
    length = input('Enter target string length (number 36+): ')
    if not length.isdigit():
        print ('enter digit please')
        continue
        
    length = int(length)  
    if length <=35:
        print('string length is less than minimum (36 symbols)')
        continue
        
    break


with open('text.txt', 'r', encoding='utf-8') as f:
    with open('new_text.txt', 'w') as f_new:
        line = f.readline()
        while line != '':
            while len(line) > length:
                end = line.rfind(' ', 0, length)
                new_line = line[:end] if end != length else line[:length] 
                line = line [end+1:] if end !=length else line[length+1]
                miss = length-1 - len(new_line)
                count = new_line.count(' ')
                ratio = miss//count
                spaces = ' '*(ratio+1)
                rem = miss % count
                while len(new_line) != length-1:
                    
                    if rem > 0:
                        new_line = new_line.replace(' ', spaces)
                        new_line = new_line.replace(spaces, spaces+' ', rem)
                    else:
                        new_line = new_line.replace(' ', spaces)
                        
            
      
            
                    
                f_new.write(new_line + '\n')
            f_new.write(line)
            line = f.readline()
        print('\n The text formatted in new document new_text.txt')

        
      
   













