def input_line_width():
    """Returns the number of characters entered by the user in a string."""
    while True:
        line_width = input("Enter the maximum number of characters per line "
                           "(must be more than 35):\n")
        if not line_width.isdigit() or int(line_width) < 35:
            print("Incorrect format! Try again!")
            continue
        break
    return int(line_width)

def get_words(text_list, line_width):
    """Returns a list of words and reduces the list of the read string."""
    word_list = []
    amount_words_chars = 0
    while text_list:
        amount_words_chars += len(text_list[0])
        amount_chars = amount_words_chars + len(word_list)
        if amount_chars > line_width:
            return word_list

        word_list.append(text_list.pop(0))

    return [' '.join(word_list)]

def get_space_count(space_index, extra_spaces, numb_of_spaces):
    """Returns the number of spaces in one position."""
    if space_index < extra_spaces % numb_of_spaces:
        return extra_spaces // numb_of_spaces + 1
    return extra_spaces // numb_of_spaces

def get_space_list(word_list, line_width):
    """Returns a list of spaces."""
    space_list = [1 for i in range(len(word_list) - 1)]

    current_line_width = len(space_list) + sum(len(word) for word in word_list)
    if line_width == current_line_width:
        return space_list

    extra_spaces = line_width - current_line_width
    for i in range(len(space_list)):
        space_list[i] += get_space_count(i, extra_spaces, len(space_list))
    return space_list

line_width = input_line_width()

with open("text.txt", 'r') as in_f, open("text_chars.txt", 'w') as out_f:
    while text := in_f.readline():
        text_list = text.split()
        while text_list:
            word_list = get_words(text_list, line_width)
            space_list = get_space_list(word_list, line_width)
            for i in range(len(word_list) - 1):
                out_f.write(word_list[i])
                out_f.write(space_list[i] * ' ')
            out_f.write(word_list[-1])
            out_f.write("\n")

print("The formatted file is text_chars.txt")