s = 'asdfjlOIUeiokl'


def countVowels(string):
    vowel = "aeiou"
    string = string.lower()
    return sum(letter in vowel for letter in string)

print(countVowels(s))
