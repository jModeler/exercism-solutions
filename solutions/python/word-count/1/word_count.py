from collections import Counter
import re

PATTERN = r"(?<![A-Za-z0-9])'|'(?![A-Za-z0-9])|[^A-Za-z0-9']+"

def count_words(sentence):
    
    word_list = re.split(PATTERN, sentence)

    # remove empty strings
    word_list = [p.lower() for p in word_list if p]

    freq = Counter(word_list)

    return dict(freq)
