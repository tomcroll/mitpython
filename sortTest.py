def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


## Consider the following code, which is an alternative version of search.


def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False


myList  = []#  [ 2, 3, 4, 5, 6, 2, 4]
myVar = 4

print search(myList, myVar)
print newsearch(myList, myVar)
