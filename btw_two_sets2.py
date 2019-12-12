
import math
import os
import random
import re
import sys
from datetime import datetime, time

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    def factors(i, x):
        for value in x:
            if i%value == 0 and i >= value:
                continue
            elif value%i == 0 and value >= i:
                continue
            else:
                return 1
        return 0
    factors_a = {i for i in range(max(a), min(b) + 1) if factors(i, a) == 0}
    factors_b = {i for i in range(max(a), min(b) + 1) if factors(i, b) == 0}

    return len(factors_a.intersection(factors_b))



if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))
    time1 = time.clock()
    print(getTotalX(arr, brr))
    time2 = time.clock()
    print(time2 - time1)