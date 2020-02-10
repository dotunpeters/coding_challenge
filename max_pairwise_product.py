
def maximum(values):
	values.sort()
	return values[-1]*values[-2]

def maximum_max(values):
	values.sort()
	val1 = values.pop()
	val2 = values.pop()
	return val1*val2

def naive_max(values):
	product  = []
	for i in range(len(values)):
		for j in range(len(values)):
			if i != j:
				product.append(values[i]*values[j])
			else:
				continue
	return max(product)

values = [int(i) for i in input("Values: ").split()]
print(f"Max pairwise: {naive_max(values)}")

good = '''
values = [i for i in range(1000)]
product  = 0
result = 0
for i in range(len(values)):
	for j in range(len(values)):
		if i != j:
			product = values[i]*values[j]
			result = max(product, result)
		else:
			continue
'''

better = '''
values = [i for i in range(1000000)]
values.sort()
val1 = values.pop()
val2 = values.pop()
val1*val2
'''

best = '''
values = [i for i in range(1000000)]
values.sort()
values[-1]*values[-2]
'''
from timeit import timeit
print(f"best time: {timeit(stmt=best, number=10)/10} seconds")
print(f"better time: {timeit(stmt=better, number=10)/10} seconds")
print(f"good time: {timeit(stmt=good, number=10)/10} seconds")
