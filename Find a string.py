#In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

#NOTE: String letters are case-sensitive.

def count_substring(string, sub_string):
    count = string.count(sub_string[0])
    counter = 0
    for i in range(count):
        if sub_string in string:
            counter += 1
            ind = string.index(sub_string)
            string = string[0 : ind : ] + string[ind + 1 : :]
            print(string)
        
    
    return counter

string = input()
sub_string = input()
print(count_substring(string, sub_string))
