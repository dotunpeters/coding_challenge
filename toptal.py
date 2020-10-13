# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, K):
    # write your code in Python 3.6
    S = list(S)
    S.sort()
    S_set = set(S)
    S_dict = {}
    for each in S_set:
        S_dict[each] = S.count(each)
        
    print(S_dict)
    checks = False
    for key in S_dict:
        if checks:
            S_dict[key] -= K
            K = 0
        if K == 0:
            value = "".join([f"{S_dict[key]}{key}" for key in S_dict if S_dict[key] > 0])
            value = "".join([x for x in value if x != "1"])
            print(value)
            return len(value)
        if S_dict[key] <= K:
            K = K - S_dict[key]
            S_dict[key] = 0
            checks = True
            