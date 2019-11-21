
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_a, count_b = 0, 0
    min_a, min_b = s - a, b - t
    max_a, max_b = t - a, b - s
    for i in apples:
        if i >= 0 and i >= min_a and i <= max_a:
            count_a += 1
    for i in oranges:
        if i < 0 and abs(i) >= min_b and abs(i) <= max_b:
            count_b += 1
    print(count_a)
    print(count_b)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
