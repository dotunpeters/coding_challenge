

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    """
        ########PSEUDOCODE###########
        sort array
        for index in range(len):
            if index == 0:
                continue
            if array[index] == array[index - 1]:
                continue
            if array[index] - array[index - 1] > 1:
                if array[index] < 1:
                    return 1
                else:
                    return array[index] - 1
    """
    
    A.sort()
    print(A)
    for index in range(len(A)):
        if index == 0:
            continue
        if A[index] == A[index - 1]:
            continue

        if A[index] - A[index - 1] > 1:
            if A[index - 1]+1 < 1:
                return 1
            else:
                return A[index - 1] + 1
    return A[-1]+1

A = [-5, -4, 3]
print(solution(A))