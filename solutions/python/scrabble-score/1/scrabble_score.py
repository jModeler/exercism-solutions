
VALUES = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X' ],
    10: ['Q', 'Z']
}

def score(word):
    result = 0
    for character in word:
        capitalized = character.upper()
        for key, value in VALUES.items():
            if capitalized in value:
                result += key 
    return result
