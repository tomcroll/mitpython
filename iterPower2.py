def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = base
    while exp > 1:
        result *= base
        exp -= 1
    return result

print iterPower(2, 5)
