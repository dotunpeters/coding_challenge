#There are n particles numbered from 0 to n − 1 lined up from smallest to largest ID along the x-axis.
#The particles are all released simultaneously. Once released, each particle travels indefinitely in a
#straight line along the positive x-axis at a speed. When two particles collide, the faster particle moves through
#the slower particle and they both continue moving without changing speed or direction. Given a list of particle
#speeds for particles arranged left to right by position, determine the number of collisions that occur with the
#particle at index pos.For example, assume there are n=2 particles, p[0] and p[1], located at positions 0 and 1 at
#time t = 0. The particle p[0] is traveling to the right at speed[0] = 2 units velocity and particle pos[1] is
#traveling at speed[1] = 1 unit velocity per unit of time. At time t = 1, p[0] has moved to position 0 + 2 = 2, and 
#[1] is at position 1 + 1 = 2 on the x-axis. Since they both occupy the same position, they have collided at time t =
#1. At time t = 2, the particle p[0] is at position 2 + 2 = 4, and p[1] is at 2 + 1 = 3 at time t = 2. Since p[0] is
#moving faster than p[1], and is now ahead of p[1] on the x-axis, they will never collide again. In this case, there
#is 1 collision.




speed = [6,6,1,6,3,4,6,8]
pos = 2


def collision(speed, pos):
    # Write your code here
    new_pos = [0 for x in range(len(speed))]
    counter = 0
    collide = 0
    k = pos

    #append new position of each particle in a list
    for i in speed: 
        new_pos[counter] = counter + i
        counter += 1

    #check if pos is less or equal to particles below
    for j in range(pos):
        if new_pos[pos] <= new_pos[k-1]:
            collide += 1
            k -= 1

    #check if pos is greater or equal to particles above
    k = pos
    for l in range(len(speed) - (pos+1)):
        if new_pos[pos] >= new_pos[k+1]:
            collide += 1
            k += 1
    return collide
            


print(collision(speed, pos))