def gcdIter(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    smallerInt = min(a, b)
    largerInt = max(a, b)
    if largerInt % smallerInt == 0:
        return smallerInt
    else:
        for i in range(smallerInt, 0, -1):
            if i == 1:
                return 1
            elif a % i == 0 and b % i == 0:
                return i


print gcdIter(6, 12)
