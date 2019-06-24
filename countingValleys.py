#Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill, , or a downhill,  step. Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude. We define the following terms:

#A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
#A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
#Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

#For example, if Gary's path is , he first enters a valley  units deep. Then he climbs out an up onto a mountain  units high. Finally, he returns to sea level and ends his hike.


#Input test data
n = 34
s = "UDDUDUDDUUDDDUUDUDDUUUDDDDDDUUUUUU"


def countingValleys(n, s):
    valley = []
    valley_count = 0
    counter = 0
    for step in s:
        if step == "U":
            counter += 1
        elif step == "D":
            counter -= 1

        valley.append(counter)
        if valley[-1] == 0:
            if valley[-2] and valley[-2] == -1:
                valley_count += 1

    return valley_count


print(countingValleys(n, s))
