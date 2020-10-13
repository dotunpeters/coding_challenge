
def my_square(values):
    for each in values:
        yield each * each


result = my_square([2, 4, 3, 5, 7, 5, 3, 8, 6, 9, 3, 6, 7])

for each in result:
    print(each)