from math import prod 

def factors(value):
    result = []
    ii = 2
    quotient = value
    while prod(result) != value:
        if quotient%ii == 0:
            quotient = quotient//ii
            result.append(ii)
        else:
            ii += 1
    return result