def append(list1, list2):
    result = list1 
    list1_length = length(result)
    result[list1_length:] = list2 
    return result

def concat(lists):
    result = []
    for ii in lists:
        result = append(result, ii)
    return result


def filter(function, list):
    return [x for x in list if function(x)]


def length(list):
    result = 0
    for ii in list:
        result += 1
    return result


def map(function, list):
    return [function(x) for x in list]


def foldl(function, list, initial):
    result = initial
    if length(list) == 0:
        return result
    else:
        for ii in list:
            result = function(result, ii)
    return result


def foldr(function, list, initial):
    new_list = reverse(list)
    result = initial
    if length(list) == 0:
        return result 
    else:
        for ii in new_list:
            result = function(result, ii)
    return result


def reverse(list):
    return list[::-1]
