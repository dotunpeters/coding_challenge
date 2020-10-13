my_code = '''
#number of fibonacci sequence
numb = 10

x = 0
y = 1
if numb == 1:
	print(x)
elif numb == 2:
	print(x)
	print(y)
elif numb > 2:
	for _ in range(numb - 2):
		x, y = y, x+y

'''

my_code2 = '''
x_list = input("values seperated by space: ").split()
x_list = [int(i) for i in x_list]
print(f"sum: {sum(x_list)}")

'''
from timeit import timeit
print(f"time: {timeit(stmt = my_code2,number = 10) / 10}seconds")