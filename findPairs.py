
def findPairs(values, target):
    values = set(values)
    print(values)
    for value in values:
        diff = target - value
        if diff > 0 and diff in values:
            return (value, diff)
    return "No valid pair"

print(findPairs([14, 13, 6, 7, 8, 10, 4, 2], 18))