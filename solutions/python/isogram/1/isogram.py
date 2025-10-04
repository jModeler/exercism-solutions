import string as s

def is_isogram(string):
    alphabets = list(s.ascii_lowercase)
    string_chars = list(string.lower())

    # check counts
    for ii in string_chars:
        if ii in alphabets: # ignores non alphabets
            if string_chars.count(ii) > 1:
                return False
    
    # if the loop has completed without triggering the return statement, the string is an isogram
    return True




