from string import ascii_uppercase

def calculate_length(letter):
    index = ascii_uppercase.index(letter)
    return (index, (2*index + 1))

def determine_space(letter):
    index = ascii_uppercase.index(letter)
    return 2*index - 1

def rows(letter):
    result = []
    index, length = calculate_length(letter)
    letters = ascii_uppercase[:(index + 1)]
    space = " "
    for ii in letters:
        if determine_space(ii) < 0:
            entry = space * (length//2) + ii + space * (length//2)
            result.append(entry)
        else:
            in_between = determine_space(ii)
            remaining = length - in_between - 2 # 2 spaces for the letter to appear
            entry = space * (remaining//2) + ii + space * in_between + ii + space * (remaining//2)
            result.append(entry)
    # now reverse result and extend it, only if the letter is not A
    if letter != 'A':
        reverse = result[::-1]
        reverse.pop(0)
        result.extend(reverse)

    return result