user_input = input('Please, input the numeric value (min.36) \n')   # <class 'str'>
while True:
    if user_input.isdigit() == True and int(user_input) > 35:
        break
    else:
        user_input = input('Only numbers min. 36 \n')

with open("text.txt", 'r', encoding='utf-8') as fr, open("test.txt", 'w', encoding='utf-8') as fw:
    str_length = int(user_input)
    line = fr.readline()
    while line != '':
        while len(line) > str_length:
            end = line.rfind(' ', 0, str_length)
            new_line = line[:end] if end != str_length else line[:str_length] 
            line = line[end + 1:] if end != str_length else line[str_length + 1:]
            required = str_length - len(new_line) - 1
            exist = new_line.count(' ')
            count = 2
            while len(new_line) != str_length - 1:
                if required <= exist:
                    new_line = new_line.replace(' ' * (count - 1), ' ' * count, required)
                else:
                    new_line = new_line.replace(' ' * (count - 1), ' ' * count, exist)
                    count += 1
                    required -= exist
            fw.write(new_line + '\n')
        fw.write(line)
        line = fr.readline()
    print('Mission completed')
