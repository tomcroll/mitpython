s='bobbbobobboobobookobobbobbboj'


def count_bobs(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):
        if string[i:i+3] == "bob":
            count += 1
    return count

print(count_bobs(s))
