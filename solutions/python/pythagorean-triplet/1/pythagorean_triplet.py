def triplets_with_sum(number):
    result = []
    for ii in range(1, number+1):
        for jj in range(ii+1, number+1):
            kk = number - ii - jj 
            if kk < jj:
                break
            else:
                if check_triplet([ii, jj, kk]):
                    result.append([ii, jj, kk])
    return result

def check_triplet(nums):
    # nums need to be ordered from lowest to highest
    return (nums[0]**2 + nums[1]**2 == nums[2]**2)
