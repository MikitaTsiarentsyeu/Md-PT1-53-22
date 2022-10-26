# This version should be better

while True:
    length = input("Enter the maximum number of characters in a string (more than 35)\n")
    if length.isdigit() and int(length) > 35:
        length = int(length)
        break
    else:
        print("Incorrect string lenght")

with open ("text.txt", "r", encoding='utf-8') as f, open ("result_text.txt", "w") as res_f:
    line = f.readline()
    while line != "":
        while len(line) > length:
            last_space = line.rfind(" ", 0, length)
            new_line = line[:last_space] if last_space != length else line[:length] 
            line = line[last_space + 1:] if last_space != length else line[length + 1:]
            space_amount = length - len(new_line) - 1
            spaces = new_line.count(" ")
            counter = 2
            while len(new_line) != length - 1:
                if space_amount <= spaces:
                    new_line = new_line.replace(" " * (counter - 1), " " * (counter), space_amount)  
                else:
                    new_line = new_line.replace(" " * (counter - 1), " " * (counter), spaces)
                    counter += 1
                    space_amount -= spaces
            res_f.write(new_line + "\n")
        res_f.write(line)
        line = f.readline()
    print("Text has been formatted and written to a new file - result_text.txt")
    