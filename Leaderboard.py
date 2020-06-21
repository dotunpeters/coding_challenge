
from bisect import insort

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)))
    lenght = len(scores)
    start = 0
    for score in alice:
        print("start", start)
        insort(scores, score)
        print("scores", scores)
        print("scores new", scores[lenght::-1])
        index = scores[lenght::-1].index(score) + 1
        print(index)
        start = index


scores = [100, 90, 90, 80, 75, 60]
alice = [50, 65, 77, 90, 102]
climbingLeaderboard(scores, alice)