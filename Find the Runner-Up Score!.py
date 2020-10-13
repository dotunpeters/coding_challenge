#Given the participants' score sheet for your University Sports Day, 
#you are required to find the runner-up score. You are given scores. 
#Store them in a list and find the score of the runner-up.

arr = map(int, input().split())
arr = list(set(arr))
print(arr)
arr.sort()
print(arr)
print(arr[-2])
