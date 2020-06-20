

# 26 is even
# 25 is odd
# 24 is even and represents 2 dozen
# 23 is odd


"""
int x
loop x(-1):
    if each is even and multpile of 12:
        print("each is even and represents each//12 dozen ")
    if each is odd:
        print("each is odd ")
    if each is even:
        print("each is even ")
"""

def checks(value):
    while value > 0:
        if value%2 == 0:
            if value%12 == 0:
                print(f"{value} is even and represents {value//12} dozen ")
            else:
                print(f"{value} is even ")

        else:
            print(f"{value} is odd ")
            
        value -= 1

checks(48)