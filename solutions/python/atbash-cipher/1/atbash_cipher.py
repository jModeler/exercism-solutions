from string import ascii_lowercase, punctuation

REVERSE = ascii_lowercase[::-1]

def encode(plain_text):
    encoded_text = ''
    text = plain_text.lower()
    # remove all spaces
    text = text.replace(" ", "")
    # remove punctuation
    translator = str.maketrans('', '', punctuation)
    text = text.translate(translator)

    for ii in range(len(text)):
        if ii != 0 and ii % 5 == 0:
            encoded_text = encoded_text + ' '
        if not text[ii] in punctuation and not text[ii].isdigit():
            character = text[ii]
            location = ascii_lowercase.index(character)
            encoded_character = REVERSE[location]
            encoded_text = encoded_text + encoded_character
        if text[ii].isdigit():
            encoded_text = encoded_text + text[ii]
    
    return encoded_text

def decode(ciphered_text):
    decoded_text = ''
    for character in ciphered_text:
        if character != " " and not character.isdigit():
            location = REVERSE.index(character)
            decoded_character = ascii_lowercase[location]
            decoded_text = decoded_text + decoded_character
        if character.isdigit():
            decoded_text = decoded_text + character
    return decoded_text