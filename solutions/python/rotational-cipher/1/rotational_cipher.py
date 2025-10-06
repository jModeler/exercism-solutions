import string 

def new_char_value(char, string_list, key):
    char_index = string_list.index(char) + key
    if char_index > 25:
        char_index = (char_index % 25) - 1
    return string_list[char_index]    

def rotate(text, key):
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    rotated = ''
    for char in text:
        if char.isupper():
            new_char = new_char_value(char, upper, key)
        elif char.islower():
            new_char = new_char_value(char, lower, key)
        else:
            new_char = char
        rotated = ''.join([rotated, new_char])
    return rotated