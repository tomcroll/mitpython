testList = [1, -4, 8, -9]


def incInt(x):
    x += 1
    print x
    return x


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


print applyToEach(testList, incInt)
print testList
