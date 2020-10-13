
def FirstNoneDuplicate(word):
    for letter in word:
        if word.count(letter) == 1:
            return letter
    return "_"


print(FirstNoneDuplicate("aaabcccde"))