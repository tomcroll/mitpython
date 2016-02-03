def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0 or base == 1:
        return 1
    return base*recurPower(base, exp-1)

print recurPower(17, 2)
