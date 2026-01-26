def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if any(x < 0 for x in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if any(x >= input_base for x in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if digits == []:
        return [0]

    number_10 = convert_base_10(input_base, digits)
    new_digits = get_digits(output_base, number_10)

    return new_digits


def convert_base_10(input_base, digits):
    digits.reverse()
    number = 0
    for ii, digit in enumerate(digits):
        number += digit * (input_base**ii)
    return number

def get_digits(output_base, number_10):
    new_digits = []
    quotient = number_10 // output_base
    remainder = number_10 % output_base
    new_digits.append(remainder)
    while quotient >= output_base:
        remainder = quotient % output_base
        new_digits.append(remainder)
        quotient = quotient // output_base
    if quotient != 0:
        new_digits.append(quotient)
    new_digits.reverse()
    return new_digits
