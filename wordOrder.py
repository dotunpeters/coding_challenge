
words = [input() for i in range(int(input()))]

def wordOrder(words):
    counter = []
    setWords = []
    for y in words:
        if y not in setWords:
            setWords.append(y) 
                 
    print(len(setWords))
    setWords = iter(setWords)
    for x in setWords:
        count = words.count(x)
        counter.append(count)
    yield counter


result = wordOrder(words)
for value in result:
    print(value, end="")
    for i in value:
        print(i, end="")