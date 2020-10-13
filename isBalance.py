
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    n = len(s)
    s = list(s)
    braces = ['(','[','{']
    if n%2 != 0:
        return "NO"
    else:
        for i in range(n):
            if s[0] not in braces:
                return "NO"
            if s[0] == '(':
                try:
                    s.remove(')')
                except:
                    return "NO"
                s = s[1:]
                if not s:
                    break
                continue
            elif s[0] == '[':
                try:
                    s.remove(']')
                except:
                    return "NO"
                s = s[1:]
                if not s:
                    break
                continue
            elif s[0] == '{':
                try:
                    s.remove('}')
                except:
                    return "NO"
                s = s[1:]

                if not s:
                    break
                continue
    return "YES"

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result)
