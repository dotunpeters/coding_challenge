
# Complete the birthday function below.
def birthday(s, d, m):
    if m == 0:
        return 0
    for choc in s:
        month = m
        result = choc + birthday(s[s.index(choc)+1:], d, month-1)  
        
        counter = 0
        if result == d:
            counter += 1


if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    print(birthday(s, d, m))
