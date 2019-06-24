

#Given an array of integers, find and print the maximum number of integers you 
#can select from the array such that the absolute difference between any two of 
#the chosen integers is less than or equal to . For example, if your array is , 
#you can create two subarrays meeting the criterion:  and . The maximum length 
#subarray has  elements.


list = input().split()
list = [int(i) for i in list]
list.sort()
print(list)

def pickingNumbers(list):
    # Write your code here
    maximum = []
    maxim = 0
    while len(list) > 1:

        if len(list) != 0:
            A = max(list)
            count_max = list.count(A)
            for j in range(count_max):
                list.remove(max(list))
            maxim += count_max
        else:
            return max(maximum)

        if len(list) != 0:
            B = max(list)
            count_max = list.count(B)
            maxim += count_max
        else:
            return max(maximum)

        if abs(A - B) <= 1:
            maximum.append(maxim)
            maxim = 0
    return max(maximum)


print(pickingNumbers(list))