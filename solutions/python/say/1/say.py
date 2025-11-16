LIMIT = 999_999_999_999

ones = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

tens_dict = {
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"
}

other_tens = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
}

place_value = {
    3: "hundred",
    4: "thousand",
    5: "thousand",
    6: "thousand",
    7: "million",
    8: "million",
    9: "million",
    10: "billion",
    11: "billion",
    12: "billion"
}

def process_part(number_string):
    if number_string in ones:
        return ones[number_string]
    elif number_string in tens_dict:
        return tens_dict[number_string]
    elif len(number_string) == 2:
        if number_string == "00":
            return ""
        elif number_string[0] == "0" and number_string[1] != "0":
            return ones[number_string[1]]
        elif number_string[0] != "0" and number_string[1] == "0":
            return other_tens[number_string[0]]
        else:
            return "-".join([other_tens[number_string[0]], ones[number_string[1]]])
    else: # 3 digit number
        if number_string[0] == "0":
            return process_part(number_string[1:])
        else:
            return (" ".join([ones[number_string[0]], place_value[len(number_string)], process_part(number_string[1:])])).strip()

def convert_to_list(number):
    number_string = str(number)
    number_list = []
    while number_string != "":
        number_list.append(number_string[-3:])
        if len(number_string) < 3:
            number_string = ""
        else:
            number_string = number_string[:(len(number_string) - 3)]
    return number_list


def say(number):
    if number < 0 or number > LIMIT:
        raise ValueError("input out of range")
    else:
        number_list = convert_to_list(number)
        number_list = number_list[::-1]
        n = len(str(number))
        result = ""
        for ii in number_list:
            if ii != "000":
                result = result + " " + process_part(ii) 
                if n > 3:
                    result = result + " " + place_value[n]  
            n -= 3
        return result.strip()