#A company is organizing a car race to get publicity. They have sponsorships for n cars numbered 1 to n. There are m participants registered, and each has a preferred number. A participant will only drive a car if the car's number is a factor of the driver's preferred number.

#Given a list of preferred numbers of the m participants and the number of cars, n, determine the maximum number of participants in the race.

#For example, there are m = 4 participants whose number preferences are prefNums = [1, 3, 6, 8] and n = 4 cars, numbered 1, 2, 3 and 4.  The first driver takes car 1 because 1 is the only factor of 1. Car 3 can be driven by driver 2 because 3 is a factor of 3 (factors = 1, 3). The third driver chooses car 2 because 2 is a factor of 6 (factors = 1,2,3,6). Finally, driver 4 chooses car 4, (factors of 8 = 1,2,4,8). All four drivers can have a car.


n = int(input().strip())

prefNums_count = int(input().strip())

prefNums = []

for _ in range(prefNums_count):
    prefNums_item = int(input().strip())
    prefNums.append(prefNums_item)

def maxParticipants(n, prefNums):
    # Write your code here
    par = prefNums
    car = [x+1 for x in range(n)]
    list = []
    for i in par:
        for j in car:
            if i%j == 0 and j not in list:
                list.append(j)

    return len(list)

    print(par)
    print(prefNums)

result = maxParticipants(n, prefNums)
print(f"result: {result}")