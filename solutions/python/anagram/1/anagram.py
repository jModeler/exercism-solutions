def get_char_counts(word):
    count_dict = {}
    for ii in word:
        count_dict[ii] = count_dict.get(ii, 0) + 1
    return count_dict 

def find_anagrams(word, candidates):
    result = []
    word_dict = get_char_counts(word.lower())
    for ii in candidates:
        if word.lower() != ii.lower() and word_dict == get_char_counts(ii.lower()):
            result.append(ii)
    return result

