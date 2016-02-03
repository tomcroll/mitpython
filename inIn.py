def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    low = 0
    high = len(aStr) - 1
    middle = (high + low) / 2
    if aStr == "":
        return False
    elif len(aStr) == 1:
        return aStr == char
    elif aStr[middle] == char:
        return True
    elif char < aStr[middle]:
        return isIn(char, aStr[:middle - 1])
    else:
        return isIn(char, aStr[middle + 1:])
