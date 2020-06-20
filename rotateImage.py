"""
    ########PSEUDOCODE###########
    result = []
    for i in range(len(word)):
        temp = []
        for j in range(len(word)):
            temp.append(each[j][i])
        result.append(temp)

"""

def rotateImage(value):
    result = []
    lenght = len(value)
    for i in range(lenght):
        temp = []
        for j in range(lenght):
            temp.append(value[j][i])
        result.append(temp[::-1])
    return result


print(rotateImage([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))