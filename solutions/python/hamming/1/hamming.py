def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        hamming_dist = 0
        for ii in range(len(strand_a)):
            if strand_a[ii] != strand_b[ii]:
                hamming_dist += 1
        return hamming_dist
    else:
        raise ValueError("Strands must be of equal length.")
