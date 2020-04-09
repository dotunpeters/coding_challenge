
from timeit import timeit


recurFact = '''
def recurFact(factorial):
	if factorial == 1:
		return 1
	return factorial * recurFact(factorial - 1)
print(recurFact(986))
'''


linearFact = '''
def linearFact(factorial):
	fact = 1
	for i in range(1, factorial + 1):
		fact *= i
	return fact
print(linearFact(986))
'''


print(f"recursion time: {timeit(stmt=recurFact, number=1)}")
print(f"loop time: {timeit(stmt=linearFact, number=1)}")