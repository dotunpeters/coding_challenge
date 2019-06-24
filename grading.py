
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
# 

def gradingStudents(grades):
    # Write your code here
    print(grades)
    roundGrade = []

    def mult5(value):
        while True:
            if value%5 == 0:
                return value
            else:
                value += 1

    for i in grades:
        if i < 37:
            roundGrade.append(i)
            continue
        elif mult5(i) - i < 3:
            roundGrade.append(mult5(i))
            continue
        else:
            roundGrade.append(i)
    return roundGrade

if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
