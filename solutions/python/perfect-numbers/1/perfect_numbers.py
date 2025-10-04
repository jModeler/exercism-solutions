import math

def get_factors(number):
    """ Function to get factors of a number, excluding the number itself
    :param number: int a positive integer
    :return: list the list of factors
    """

    factors = set()
    num_sqrt = math.sqrt(number)

    for ii in range(1, int(num_sqrt) + 1):
        if number % ii == 0:
            factors.add(ii)
            factors.add(number//ii)
    
    # remove the number itself
    factors = factors - {number}

    return sorted(factors)

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        factors = get_factors(number)
        if number == sum(factors):
            return "perfect"
        elif number > sum(factors):
            return "deficient"
        elif number < sum(factors):
            return "abundant"
