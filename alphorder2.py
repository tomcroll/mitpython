s = 'abcdefghijklmnopqrstuvwxyz'

def alph_order(string):
    string = string.lower()
    result = []
    temp = []
    for char in string:
        print '...........'
        print char
        print 'temp = ', temp
        print 'result = ', result
        if(len(temp) == 0):
            print 'len tem == 0'
            temp.append(char)
            print temp
        elif(char >= temp[-1]):
            print 'char >= temp[-1]', char, temp[-1]
            temp.append(char)
        elif(char<temp[-1]):
            print 'char < temp[-1]', char, temp[-1]
            if len(temp) > len(result):
                print 'len temp >'
                result = temp
            temp=[]
            temp.append(char)
    if len(temp) > len(result):
        print 'len temp >'
        result = temp

    return ''.join(result)

#print len(s)
print('Longest substring in alphabetical order is: ' + alph_order(s))
