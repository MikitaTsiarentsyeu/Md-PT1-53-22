str_length = input('input max string length (>35) ')
while True:
    if int(str_length) <= 35:
        str_length = input('number must me more than 35. input again ')
    else:
        break

''' when i tried to read file i got some problems with file encoding (like TIOBEвЂ™s instead of TIOBE’s),
so i decided to find a way to encode it with python'''
result = ''
symbol_counter = 0
edited_line = []
str_length = int(str_length)
with open('text.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.split(' ')
        for i in range(len(line)):
            if symbol_counter + len(line[i]) + 1 > str_length:
                spaces = str_length - symbol_counter
                while spaces > 0:
                    for j in range(len(edited_line) - 1):
                        edited_line[j] += ' '
                        spaces -= 1
                        if spaces == 0:
                            symbol_counter = 0
                            break
                symbol_counter = 0
                result += ' '.join(edited_line) + '\n'
                edited_line = []
            if '\n' in line[i]:
                edited_line.append(line[i])
                symbol_counter = 0
                result += ' '.join(edited_line)
                edited_line = []
                break
            symbol_counter += len(line[i]) + 1
            edited_line.append(line[i])
    result += ' '.join(edited_line)

with open('result.txt', 'w', encoding='utf-8') as file:
    file.write(result)
