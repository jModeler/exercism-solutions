from string import punctuation
from math import sqrt

def cipher_text(plain_text):
    normalized_text = normalize(plain_text)
    r, c = determine_rc(normalized_text)
    cipher_list = create_matrix(normalized_text, r, c)
    cipher = create_cipher(cipher_list, c)
    return " ".join(cipher)

def normalize(plain_text):
    remove_text = punctuation + " "
    # remove spaces and punctuation
    result = plain_text.translate(str.maketrans("", "", remove_text))
    return result.lower()

def determine_rc(normalized_text):
    l = len(normalized_text)
    # determine r and c
    r = round(sqrt(l))
    if r*r >= l:
        r = c = int(r)
    else:
        r = int(r)
        c = r + 1
    return r, c

def create_matrix(normalized_text, r, c):
    result = []
    ii = 0
    for _ in range(r):
        text = normalized_text[ii:(ii + c)]
        if len(text) < c:
            padding = c - len(text)
            text = text + " " * padding 
        result.append(text)
        ii += c 
    return result

def create_cipher(cipher_list, c):
    result = []
    for ii in range(c):
        text = ""
        for jj in cipher_list:
            text = "".join([text, jj[ii]])
        result.append(text)
    return result
    