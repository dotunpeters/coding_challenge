

def solution(value):
    bin_equ = bin(value)[2:]
    print("binary: ", bin_equ)

    listing = {0}
    start = False
    counter = 0

    for each in bin_equ:
        if each == "1" and start == False:
            start = True
            continue
        if each == "0" and start == True:
            counter += 1
            continue
        if each == "1" and start == True:
            listing.add(counter)
            counter = 0
    print("List: ", listing)
    return max(listing)

print(solution(32))
        
