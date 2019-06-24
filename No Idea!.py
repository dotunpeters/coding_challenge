
get = input().split()
n = int(get[0])
m = int(get[1])

list = input().split()
list = [int(x) for x in list]

A = input().split()
A = [int(x) for x in A]
a = set(A)

B = input().split()
B = [int(x) for x in B]
B = set(B)

happiness = 0

for value in list:
    if value in A:
        happiness += 1
    elif value in B:
        happiness -= 1
    else:
        pass

print(happiness)
