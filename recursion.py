
from timeit import timeit


def recurFact():
	print("Hello World")


def linearFact():
	print("Hello World")


print(timeit(stmt=recurFact, number=100)/100)
print(timeit(stmt=linearFact, number=100)/100)
