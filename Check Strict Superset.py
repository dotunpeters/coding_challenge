#You are given a set  and  other sets. 
#Your job is to find whether set  is a strict superset of each of the  sets.
#Print True, if  is a strict superset of each of the  sets. Otherwise, print False.
#A strict superset has at least one element that does not exist in its subset.


A = set(input("SuperSet: ").split())
N = int(input("Number of Subset: "))
result = "None"

for i in range(N):
    otherSet = set(input(f"Subset{i+1}: ").split())
    otherSet = set(otherSet)
    if result == False:
        break
    for eachValue in otherSet:
        if eachValue in A:
            result = True
            continue
        else:
            result = False
            break

print(result)