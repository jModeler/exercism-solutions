def primes(limit):
    result = []
    if limit < 2:
        return result
    else:
        nums = list(range(2, limit+1))
        marked = [0]*len(nums)
        for ii in range(len(nums)):
            if marked[ii] == 0:
                result.append(nums[ii])
                marked = sieve(nums[ii], nums, limit, marked)
    return result


def sieve(number, nums, limit, marked): 
    multiple = 2
    n = number * multiple
    while n <= limit:
        non_prime_index = nums.index(n)
        marked[non_prime_index] = 1
        multiple += 1
        n = number * multiple        
    return marked