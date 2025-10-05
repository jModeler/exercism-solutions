import string 

def is_valid(isbn):
    # remove dashes
    nums = isbn.replace("-", "")
    if len(nums) != 10:
        return False
    mult = list(range(10, 0, -1))
    check = 0
    ii = 0
    for num in nums:
        if ii+1 != len(nums):
            if num in string.ascii_letters:
                return False
            else:
                check += int(num) * mult[ii]
        else:
            if num != 'X' and (num in string.ascii_letters):
                return False
            elif num == 'X':
                check += 10 * mult[ii]
            else:
                check += int(num) * mult[ii]
        ii += 1
    return check % 11 == 0
