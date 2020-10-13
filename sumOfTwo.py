
def sumOfTwo(a, b, v):
    # result = {True for x in a for y in b if x + y == v}
    # print(type(result))
    # print(result)
    # return True if True in result else False
    for i in a:
        for j in b:
            if i + j == v:
                return True
    return False

a = [0, 1, 2, 3]
b = [10, 20, 39, 40]
v = 42
print(sumOfTwo(a, b, v)) 