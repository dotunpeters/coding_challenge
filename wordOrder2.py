
from collections import Counter
n = int(input())
words = [input() for i in range(n)]
words = Counter(words)
print(len(words))
for key, value in words.items():
    print(value, end=" ")