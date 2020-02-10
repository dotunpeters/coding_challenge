
#Sum of numbers
#number of values to add
#times = int(input("Number of values to add: "))
#initial = 0
#for i in range(times):
#	x_value = int(input(f"Value {i+1}: "))
#	initial = x_value + initial

#print(f"Sum = {initial}")




#Sum of the first 5 digit of a string
#get user input in string format
x = input("Numbers to add: ")
sum = 0
for i in range(5):
	sum += int(x[i])

print(f"sum: {sum}")
