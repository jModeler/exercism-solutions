# direct attack is too slow for large inputs
# using euclid's method to represent the triplets, 
# a = m**2 - n**2
# b = 2mn
# c = m**2 + n**2
# number = a + b + c = 2mn(m+n)
# we now search for m, n which is simpler
# this also uncovers a restriction on number: it _has_ to be even
# complexity goes from O(n^2) to O(n)

def triplets_with_sum(number):
    result = []
    if number % 2 != 0:
        return result
    
    # search for m, n
    total = number // 2

    for m in range(2, int(total ** 0.5) + 1):
        for n in range(1, m):
            base_sum = m*(m + n)
            if total % base_sum == 0:
                k = total // base_sum
                a = k * (m**2 - n**2)
                b = k * 2*m*n
                c = k * (m**2 + n**2)
                triplet = sorted([a, b, c])
                if triplet not in result:
                    result.append(triplet)
    
    return result