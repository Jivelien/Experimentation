def prime_factors(natural_number):
    if natural_number==1:
        return []
    i=2
    result=[]
    while True:
        if natural_number % i == 0:
            result.append(i)
            if (natural_number // i == 1):
                break
            natural_number = natural_number // i
            i=2
        else:
            i += 1
    return result