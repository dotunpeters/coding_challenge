#Kevin and Stuart want to play the 'The Minion Game'.

#Game Rules

#Both players are given the same string, .
#Both players have to make substrings using the letters of the string .
#Stuart has to make words starting with consonants.
#Kevin has to make words starting with vowels. 
#The game ends when both players have made all possible substrings. 

#Scoring
#A player gets +1 point for each occurrence of the substring in the string .



def minion_game(string):
    # your code goes here
    counter = len(string)
    kevin_score = 0
    stuart_score = 0
    vowels = "A E I O U".split()
    consonant = "B C D F G H J K L M N P Q R S T V W X Y Z".split()

    for char in string:
        if char in vowels:
            kevin_score += counter
            counter -= 1
        else:
            stuart_score += counter
            counter -= 1

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

    
if __name__ == '__main__':
    s = input()
    minion_game(s)