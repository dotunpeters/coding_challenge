
def solution(list_value, lenght):
    temp = {}
    for each in list_value:
        temp[each] = list_value.count(each)

    temp = sorted(temp, key=lambda x: temp[x], reverse=True)
    for each in temp:
        return temp[each]

print(solution([1, 2, 3, 1, 2, 1], 5))