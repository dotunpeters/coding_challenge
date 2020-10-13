#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 >= v1:
        return "NO"
    elif x1 > x2 and v1 >= v2:
        return "NO"
    elif x1 == x2:
        return "YES"
    try:
        return kangaroo(x1 + v1, v1, x2 + v2, v2)
    except RuntimeError:
        return "YES"

if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])
    time1 = datetime.now().minutes
    result = kangaroo(x1, v1, x2, v2)
    time2 = datetime.now().minutes
    print(f"{time2 - time1} secs")

    print(result)
