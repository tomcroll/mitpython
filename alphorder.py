s = 'jcvhfboqvdmojgjdtgugem'

def alph_order(string):
    string = string.lower()
    result = []
    temp = []
    for i in range(len(string)-1):
        print string[i]
        if string[i+1] >= string[i]:
            print string[i]
            temp.append(string[i])
            print temp
        else:
            if len(temp) > len(result):
                temp.append(string[i])
                result = temp
                temp = []
    return ''.join(result)

#print len(s)
print('Longest substring in alphabetical order is: ' + alph_order(s))
