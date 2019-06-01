speed = [2, 8, 6, 4, 3]
pos = [0, 1, 2, 3, 4]


def collision(speed, pos):
    # Write your code here
    new_pos = []
    counter = 0
    for i in range(len(pos)):
        for j in pos:
                new_pos[j] = speed[j] + pos[j]
        print(new_pos)
            


print(collision(speed, pos))