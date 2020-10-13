

# Complete the breakingRecords function below.
def breakingRecords(scores):
    count_max, count_min = 0, 0
    current_highest = scores[0]
    current_lowest = scores[0]
    for val in scores:
        if val > current_highest:
            current_highest = val
            count_max += 1
        if val < current_lowest:
            current_lowest = val
            count_min += 1
    return (count_max, count_min)

if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    print(breakingRecords(scores))
