import string

def is_pangram(sentence):
    alphabets = set(string.ascii_lowercase)
    sentence_alphabets = set(sentence.lower())
    return alphabets.issubset(sentence_alphabets)
