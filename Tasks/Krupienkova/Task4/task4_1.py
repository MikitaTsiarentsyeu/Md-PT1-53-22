def input_line_width():
    """Returns the number of characters entered by the user in a string."""
    while True:
        line_width = input("Enter the maximum number of characters "
                           "per line (must be more than 35):\n")
        if not line_width.isdigit() or int(line_width) < 35:
            print("Incorrect format! Try again!")
            continue
        break
    return int(line_width)

def read_words(line_width, f):
    """Returns a list of words of a single line."""
    piece_of_text = f.read(line_width)
    if not piece_of_text:
        return

    new_line_index = piece_of_text.find('\n')
    if new_line_index != -1:
        extra_text = piece_of_text[new_line_index + 1:]
        # It's important to use encode() here, because seek() operates with
        # bytes, and we can't assume that 1 char is 1 byte. e.g. text.txt has
        # symbol “ which is 3 bytes long - 0xe2 0x80 0x9c
        f.seek(f.tell() - len(extra_text.encode()))
        return [piece_of_text[:new_line_index]]

    if piece_of_text[-1] == ' ':
        return piece_of_text.split()

    next_character = f.read(1)
    if not next_character:
        return [piece_of_text]

    if next_character.isspace():
        return piece_of_text.split()

    word_list = piece_of_text.split()
    f.seek(f.tell() - len(word_list.pop().encode()) - len(next_character.encode()))
    return word_list

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
    while word_list := read_words(line_width, in_f):
        # The representation of spaces as a list of numbers allows to avoid
        # multiple creation of objects of the string class.
        space_list = get_space_list(word_list, line_width)
        for i in range(len(word_list) - 1):
            out_f.write(word_list[i])
            out_f.write(space_list[i] * ' ')
        out_f.write(word_list[-1])
        out_f.write("\n")

print("The formatted file is text_chars.txt")