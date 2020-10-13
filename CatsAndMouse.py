# Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to determine
# which cat will reach the mouse first, assuming the mouse doesn't move and the cats travel at equal speed. If the cats arrive at
# the same time, the mouse will be allowed to move and it will escape while they fight.


x, y, z = [31, 31, 31]
# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    first = abs(z - y)
    second  = abs(z - x)
    
    #print(f"first: {first} second: {second}")
    if first == second:
        return "Mouse C"
    elif first < second:
        return "Cat B"
    else:
        return "Cat A"


print(catAndMouse(x, y, z))