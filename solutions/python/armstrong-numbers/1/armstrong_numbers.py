def is_armstrong_number(number):
    # get the number of digits
    digits = len(str(number))
    # get the digits themselves
    digit_list = list(str(number))
    # get the sum of digits raised to the appropriate power
    result = 0
    for ii in digit_list:
        result += int(ii)**digits 
    return number == result
