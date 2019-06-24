
#!/bin/python3

import math
import os
import random
import re
import sys

nm = input().split()
n = int(nm[0])
m = int(nm[1])

strng = ""
newstrng = ""

for _ in range(n):
        matrix_item = input()      
        strng = strng +"\n"+ matrix_item

for i in range(m):
    
        expr= r'^.{'+str(i)+r'}(.)'
        pattern = re.compile(expr,re.MULTILINE)
        mo = re.findall(pattern, strng)
        
        newstrng = newstrng + "".join(mo)
    
    
expr = r'(?<=[0-9a-zA-Z])[!@#$%& ]+(?=[0-9a-zA-Z])'
print(re.sub(expr," ",newstrng))
