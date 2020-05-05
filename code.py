"""
value
: check if even
: 

"""


def evenOdd(value):
    result = value % 2
    result = str(result)
    result = result.replace("0", "even")
    result = result.replace("1", "odd")
    return result

print(evenOdd(2121))
