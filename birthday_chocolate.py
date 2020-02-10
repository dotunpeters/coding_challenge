
# Complete the birthday function below.
def birthday(s, d, m):
    counter = 0
    skip = []
    for i in s:
        skip.append(i)
        if i not in skip:
            x = s.index(i)+1
        else:
            count = skip.count(i)

        for j in s[x:]:
            if i + j == d:
                counter += 1
    return counter


if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    print(birthday(s, d, m))
