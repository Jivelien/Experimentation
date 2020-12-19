def distance(strand_a, strand_b):
    nucCount=len(strand_a)
    if len(strand_a)!=len(strand_b):
        raise ValueError('strands lenght doesn\'t match')
    
    hamming=0
    for i in range(nucCount):
        if strand_a[i]!=strand_b[i]:
            hamming += 1
    return hamming