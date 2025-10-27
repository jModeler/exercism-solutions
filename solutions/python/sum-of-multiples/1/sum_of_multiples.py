def get_multiples(limit, multiple):
    if multiple == 0:
        return []
    else:
        quot = limit  // multiple
        rem = limit % multiple
        if quot == 0:
            return []
        else:
            if rem != 0:
                return [multiple * (ii+1) for ii in range(quot)]
            else:
                return [multiple * (ii+1) for ii in range(quot-1)]

def sum_of_multiples(limit, multiples):
    mult_list = []
    for multiple in multiples:
        mult_list.extend(get_multiples(limit, multiple))
    # remove duplicates
    mult_list = set(mult_list)
    # return the sum
    return sum(mult_list)
