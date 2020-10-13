import string

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    
    alpha = list(string.ascii_lowercase)
    counter = 0
    s_list = list(s)
    n = len(s) - 1
    check = int(len(s)/2)

    for i in range(check):
        if (s_list[i] !=  s_list[n]):
            x = alpha.index(s_list[i])
            y = alpha.index(s_list[n])
            counter += abs(x - y)
            n -= 1
        else:
            n -= 1

    return counter

print(theLoveLetterMystery("cba"))