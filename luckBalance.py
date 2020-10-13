#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck = 0
    contests.sort(key=lambda x: x[0], reverse=True)
    important = [[i[0], i[1]] for i in contests if i[1] == 1]
    unimportant = [[i[0], i[1]] for i in contests if i[1] == 0]

    for i in important:
        if k > 0:
            luck += i[0]
            k -= 1
        else:
            luck -= i[0]
            k -= 1

    for i in unimportant:
        luck += i[0]
        k -= 1

    return luck

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
