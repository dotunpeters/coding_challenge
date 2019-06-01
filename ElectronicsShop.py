#Monica wants to buy a keyboard and a USB drive from her favorite electronics store. The store has several models of each. Monica #wants to spend as much as possible for the
#
#items, given her budget.
#
#Given the price lists for the store's keyboards and USB drives, and Monica's budget, find and print the amount of money Monica will #spend. If she doesn't have enough money to both a keyboard and a USB drive, print -1 instead. She will buy only the two required #items.


b = 50
keyboards= [5, 67, 3, 9, 10, 15]
drives = [34, 23, 12, 10, 11, 2, 5, 8, 19]

def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    maximum = 0
    for kprice in keyboards:
        for dprice in drives:
            if (kprice + dprice <= b) and (kprice + dprice > maximum):
                maximum = kprice + dprice
            else:
                continue
    
    if maximum == 0:
        return -1
    else:
        return maximum

print(getMoneySpent(keyboards, drives, b))