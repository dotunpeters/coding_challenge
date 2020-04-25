
def palindrome(word):
    word = "".join([char.lower() for char in word if char.isalpha()])
    return word == word[::-1]

print(palindrome(input("Word: ")))