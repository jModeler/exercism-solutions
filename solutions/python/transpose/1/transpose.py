from itertools import zip_longest

def transpose(text):
    words = text.split("\n")
    result = list(zip_longest(*words, fillvalue=" "))
    result = ["".join(ii).rstrip() for ii in result]
    lengths = list(map(len, result))
    result = resize(result, lengths)
    result = "\n".join(result)
    return result

def resize(result, lengths):
    n = len(result)
    for ii in range(n):
        resize_val = max(lengths[ii:])
        if len(result[ii]) != resize_val:
            result[ii] = result[ii].ljust(resize_val)
    return result
        
        