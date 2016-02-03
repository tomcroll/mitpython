def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
    l = [start + k * step for k in range(int((stop - start) / step))]
    return sum(f(x) * step for x in l)

print radiationExposure(0, 5, 1)
