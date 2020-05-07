#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    counter = 0
    for each in range(i, j+1):
        value = int(str(each)[::-1])
        evalu = abs(each - value)
        evalu /= k
        if evalu == int(evalu):
            counter += 1

    return counter



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
