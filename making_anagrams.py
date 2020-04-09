#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    delete = 0
    list_a, list_b = list(a), list(b)
    for i in a:
        if i not in list_b:
            list_a.remove(i)
            delete += 1
        if i in list_b:
            list_b.remove(i)
    return delete + len(list_b)


if __name__ == '__main__':

    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(res)
