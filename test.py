s = 'cmolcqrjxxnhggiq'


def alph_order(string):
    string = string.lower()
    result = []
    temp = []
    for char in string:
        if(len(temp) == 0):
            temp.append(char)
        elif(char >= temp[-1]):
            temp.append(char)
        elif(char < temp[-1]):
            if len(temp) > len(result):
                result = temp
            temp = []
            temp.append(char)

    return ''.join(result)

print('Longest substring in alphabetical order is: ' + alph_order(s))
