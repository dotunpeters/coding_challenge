message = "Hello World"

print(len(message[0:5]))

import sys

import math

for i in range(len(message)):
    if (message[i] == " "):
        print(f"{i}: ---")
    else:
        print(f"{i}:{message[i]}", end="\t")


xword = "fuckhaton {0}".format("hi")

if ("fuck" in xword):
    xword = xword.replace("fuck", "***")


xword = "thiz\tIs\tcs50"

print(xword)
print(dir(xword))

print(xword.casefold() == xword.lower())

print(xword.lower().count("i"))

print(xword.encode("utf-32", "strict").decode("utf-32") )

fword = xword.encode("utf-32", "strict")
print(fword)
fword = fword.decode("utf-32")
print(fword)

print(xword.endswith("cs50", 0, -1))

print(xword.center(50,"-"))

print(xword.expandtabs(1))

print(xword.find("s", 0, -1))

point = {"a":1, "b":-3, "c":2}
point_list = [1, -2, 3]
print("{a}, {c}, {b}".format_map(point))

print("{a}, {b}, {c}".format(**point))

# xword = int(input("type something: "))

#def main():
#    print("nothing")
#    return None

print(xword.index('s'))

print(xword.find('x'))

xword = "hi--*-"
numb = "123455"
char = 'a'
print(xword)
print(xword.strip("-"))
print(numb.rjust(8, "~"))
print(str.maketrans("abc", "def", "uvwxyz"))
print(xword.rpartition("hi"))
print(xword.replace("hi",""))
print(xword.rsplit("*"))
print(xword.center(50,"-"))
print(xword.translate({"-":1, "*":2, "h":3, "i":4}))

word = "catwalk"

if word.endswith("walk", 0, -1):
    print("yes")
else:
    print("no")

print('---------------------')
condition = ' '
if condition:
    print('True')
else:
    print('False')

print(sys.path)

#print(sys.api_version())

print(math.radians(90))

from my_class import Employee

emp4 = Employee.parse_string('Hello-Worls-130000')
print('employee4 fullname: ', emp4.get_fullname())
print('employee4 email: ', emp4.get_email())
print(emp4.pay)
Employee.increase_pay(1.05)
emp4.apply_raise()
print(emp4.pay)