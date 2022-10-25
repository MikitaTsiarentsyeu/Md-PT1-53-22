"""1. Подготовиться к чтению содержимого файла text.txt
2. Дать пользователю ввести с клавиатуры параметр "максимальное количество символов в строке", который должен быть больше 35
3. Отформатировать текст с учётом максимального количества символов, при этом если слово целиком не умещается в строке, оно должно быть перенесено на следующую, а отступы между словами равномерно увеличены (по аналогии с функцией "Выровнять по ширине" текстовых редакторов)
4. Записать получившийся текст в новый файл и оповестить об этом пользователя.
(модуль textwrap использовать нельзя)"""

def validation_check(max_char):
    try:
        int(max_char)
        if int(max_char) < 35:
            raise RuntimeError ("The value you enter must be more then 35.")
    except (ValueError, RuntimeError):
        return "The input value must be numeric and be more then 35.\n"

while True:
    max_char = input("Enter the maximum number of characters per line (more then 35): \n")
    # max_char=40
    validation = validation_check(max_char)
    if validation:
        print (validation)
        continue
    else:
        max_char=int(max_char)
        break

with open ("text.txt", "r") as f, open ("formatted_text.txt", "w") as f_formatted:
    
    line = f.readline()
    # print(line)
    while line != '':
        # temp1 = line.read(max_char)
        # print(temp1)
        # end1 = temp1.find("\n")
        while len(line) > max_char:
            end = line.rfind(' ', 0, max_char)
            # print(end)
            if end != max_char:                       
                new_line=line[:end].strip()
            else:
                 new_line=line[:max_char].strip()
            if end != max_char:                       
                line=line[end:].strip()
            else:
                 line=line[max_char:].strip()

            while True:
                if len(new_line) < max_char:
                    count = max_char-len(new_line)
                    new_line = new_line.replace(" ", "  ", count)
                    continue    
                if len(new_line) == max_char:
                    break
            f_formatted.write(new_line + '\n')
            # print(new_line, len(new_line))
            new_line = line[end+1:]
        f_formatted.write(line + '\n')
        line = f.readline()
print("New text document created successfully as formatted_text.txt")
        
