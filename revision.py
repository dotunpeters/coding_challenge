
def other():
    list_value = [10, 23, 11]

    print(13 in list_value, end="")

    dict_value = {"name": "Dotun", "age": "Awenty nine", "profession": "Software Engineer"}

    print("Dotun" in dict_value)
    print(sorted(dict_value, key=lambda value: dict_value[value]))

    help(print)

class Students:
    pass

def main():
    sola = Students()
    sola.level = 100
    print(sola.level)
    
def checker():
    while True:
        try:
            value = int(input("initialize value: "))
        except ValueError:
            print("incorrect")
            continue
        else:
            print(value)
            return
        finally:
            print("I love you")


def sorter():
    class My_list:
        def __init__(self, *values):
            self.values = values
            self.current = 0

        def __next__(self):
            if self.current >= len(self.values):
                raise StopIteration
            result = self.values[self.current]
            self.current += 1
            return result

        def __iter__(self):
            return self

    values = My_list(8, 3, 4, 5)
    print(next(values))
    for i in values:
        print(i)

def iterating():

    def looper(value):
        for i in value:
            yield i

    xloop = looper((3, 5, 2, 6, 8, 7, 9,))

    for i in xloop:
        print(i)


def fibo(pos):

    def recur(pos):
        if pos == 1 or pos == 2:
            return 1
        
        return recur(pos-1) + recur(pos-2)

    return recur(pos)
    # later, prev = 0, 0
    # for each in range(1, pos+1):
    #     if (each == 1):
    #         prev = 1
    #     else:
    #         later, prev = prev, later + prev
    # return prev


if __name__ == "__main__":
    print(fibo(300), end="")