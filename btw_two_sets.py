
import math
import os
import random
import re
import sys
from datetime import datetime
from pytz import UTC

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
    max_a, min_b = max(a), min(b)
    factors_a, factors_b, check = list(), list(), list()
    possible_factors = {i for i in range(max_a, min_b + 1)} 

    for factor in possible_factors:
        for numb in a:
            if factor % numb == 0:
                check.append(True)
            else:
                check.append(False)

        if set(check) == {True}:
            factors_a.append(factor)
        check = list()

    for factor in possible_factors:
        for numb in b:
            if numb % factor == 0:
                check.append(True)
            else:
                check.append(False)
        if set(check) == {True}:
            factors_b.append(factor)
        check = list()

    return len(set(factors_a).intersection(set(factors_b)))



if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))
    time1 = datetime.now(tz=UTC).microsecond
    print(getTotalX(arr, brr))
    time2 = datetime.now(tz=UTC).microsecond
    print(time2 - time1)