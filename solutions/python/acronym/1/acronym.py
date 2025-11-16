from string import punctuation

punct_remove_hyphen = punctuation.replace("-", "")

def remove_punctuation(words):
    translator = str.maketrans("", "", punct_remove_hyphen)
    clean_words = words.translate(translator)
    return clean_words

def abbreviate(words):
    clean_words = remove_punctuation(words)
    clean_words = clean_words.replace("-", " ")
    words_list = clean_words.split()
    result = ""
    for ii in words_list:
        result += ii[0].upper()
    return result