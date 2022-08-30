while True:
    length = input('\nEnter the desired string length (must be >35): ')
    if length.isdigit() and int(length) > 35:
        length = int(length)
        break
    else:
        print("\tInput Error: Impossible length value")

with open("text.txt", 'r', encoding='utf-8') as text, open("formatted_text.txt", 'w') as new_text:
    line = text.readline()
    while line != '':
        while len(line) > length:
            end = line.rfind(' ', 0, length)
            new_line = line[:end] if end != length else line[:length]
            line = line[end + 1:] if end != length else line[length + 1:]
            required = length - len(new_line) - 1
            exist = new_line.count(' ')
            count = 2
            while len(new_line) != length - 1:
                if required <= exist:
                    new_line = new_line.replace(' ' * (count - 1), ' ' * count, required)
                else:
                    new_line = new_line.replace(' ' * (count - 1), ' ' * count, exist)
                    count += 1
                    required -= exist
            new_text.write(new_line + '\n')
        new_text.write(line)
        line = text.readline()
    print('\nThe text has been successfully formatted and written to formatted_text.txt')
