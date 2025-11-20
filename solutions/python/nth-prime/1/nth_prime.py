from math import sqrt

def is_prime(number):
    if number == 1:
        return False
    else:
        factors = set()
        num_sqrt = sqrt(number)
        for ii in range(1, int(num_sqrt) + 1):
            if number % ii == 0:
                factors.add(ii)
                factors.add(number//ii)
        return (factors == {1, number})

def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    else:
        ii = 0
        jj = 1
        while ii < number:
            if is_prime(jj):
                ii += 1
            jj += 1
        return (jj-1)
        

