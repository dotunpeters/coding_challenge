
arr = [[-1, 1, -7, -8], [-10, -8, -5, -2], [0, 9, 7, -1], [4, 4, -2, 1]]

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    counter = 0
    f_sum = 0
    s_sum = 0
    for i in arr:
        f_sum += i[counter]
        counter += 1

    counter -= 1
    for i in arr:
        s_sum += i[counter]
        counter -= 1   
    return abs(f_sum - s_sum)

print(diagonalDifference(arr))