ARABIC_TO_ROMAN = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}

KEYS = list(ARABIC_TO_ROMAN)

def get_digits(number):
    number_list = list(str(number))
    number_list = [int(x) for x in number_list]
    return number_list 

def get_keys(n):
    return [ii for ii in KEYS if len(str(ii)) == (n+1)]

def compose_part(part, base):
    max_base = max(base)
    min_base = min(base)
    if part in base:
        return ARABIC_TO_ROMAN[part]
    elif part < max_base:
        mult = part//min_base
        if mult <= 3:
            roman_part = mult*ARABIC_TO_ROMAN[min_base]
        else:
            mult = (max_base - part)//min_base
            roman_part = mult*ARABIC_TO_ROMAN[min_base] + ARABIC_TO_ROMAN[max_base]
    else:
        mult = (part - max_base)//min_base
        if mult <= 3:
            roman_part = ARABIC_TO_ROMAN[max_base] + mult*ARABIC_TO_ROMAN[min_base]
        else:
            new_base = KEYS[KEYS.index(max_base) + 1]
            mult = (new_base - part)//min_base 
            roman_part = mult*ARABIC_TO_ROMAN[min_base] + ARABIC_TO_ROMAN[new_base]
    return roman_part


def roman_part(digit, n):
    place = 10**n
    if n == 3:
        return digit * ARABIC_TO_ROMAN[place]
    else:
        base = get_keys(n)
        part = digit * place
        return compose_part(part, base)


def roman(number):
    number_list = get_digits(number)
    n = len(number_list) - 1
    result = ""
    for digit in number_list:
        part = roman_part(digit, n)
        result = result + part
        n -= 1
    return result