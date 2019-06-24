
n = int(input())

def staircase(n):
    space = n - 1
    hash = 0

    for i in range(n):
        for j in range(n):
            if space <= hash:
                print("#", end="")
            else:
                print(" ", end="")
                space -= 1

        hash += 1
        space = n - 1
        if i == n - 1:
            continue
        else:
            print()

staircase(n)