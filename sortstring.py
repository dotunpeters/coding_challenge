
"""
############### Pseudocode ##############
split word on " "
sort list
return " ".join(list)
"""

def sort_string(words):
    list_word = words.split(" ")
    list_word.sort(key=lambda word: word.lower())
    return " ".join(list_word)

print(sort_string(input("Words: ")))