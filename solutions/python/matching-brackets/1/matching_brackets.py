bracket_mapping = {
    ']': '[',
    '}': '{',
    ')': '('
}


def is_paired(input_string):

    right = list(bracket_mapping.keys())
    left = list(bracket_mapping.values())

    result = []

    for character in input_string:
        if character in left:
            result.append(character)
        elif character in right:
            if not result or result[-1] != bracket_mapping[character]:
                return False
            result.pop()

    return not result # result must be empty if the input_string has all bracket types paired
