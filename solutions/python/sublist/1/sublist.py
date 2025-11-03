"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

def get_indices(number, bigger_list):
    return [i for i, x in enumerate(bigger_list) if x == number]

def check_sublist(list_one, list_two):
    """
    This is only called when list_one is smaller than list_two
    """
    n1 = len(list_one)

    if n1 == 0:
        return SUBLIST
    
    indices = get_indices(list_one[0], list_two)
    n2 = len(list_two)
    
    for ii in indices:
        if n1+ii <= n2:
            sublist = list_two[ii:(n1+ii)]
            if list_one == sublist:
                return SUBLIST 
        else:
            return UNEQUAL

    return UNEQUAL

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL 
    elif len(list_one) < len(list_two):
        return check_sublist(list_one, list_two)
    else:
        result = check_sublist(list_two, list_one)
        if result == SUBLIST:
            return SUPERLIST
        else:
            return result