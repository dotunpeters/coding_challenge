
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

print(matrix_new)
last_matrix = []
for i in matrix_new:
    for j in i:
        last_matrix.append(j)
print(last_matrix)
counter = -1
add_matrix = []
while True:
    if last_matrix[counter].isalnum():
        break
    else:
        add_matrix.append(last_matrix[counter])
        counter -= 1

print(f"add_matrix: {add_matrix}")
add_matrix.reverse()
print(f"add_matrix: {add_matrix}")
for i in range(len(word)):
    if i == (len(word)-1):
        print(word[i], end="")
    else:
        print(word[i], end=" ")
for j in add_matrix:
    print(j, end="")
print()

