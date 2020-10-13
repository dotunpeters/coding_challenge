
nm = input().split()
n = int(nm[0])
m = int(nm[1])
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

list = []
new_matrix = []
for i in matrix:
    for j in i:
        if j:
            list.append(j)
    new_matrix.append(list)
    list = []

matrix_new = []
for i in range(m):
    for j in range(n):
        list.append(new_matrix[j][i])
    matrix_new.append(list)
    list = []
list = matrix_new

word = []
for i in list:
    for j in i:
        if j.isalnum():
            word.append(j)
        else:
            word.append(" ")

word = "".join(i for i in word)
word = word.split()

for i in word:
    print(i, end=" ")
print()
