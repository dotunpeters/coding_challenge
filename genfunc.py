
def gen(sentence):
    values = sentence.split(" ")
    for value in values:
        yield value



results = gen("This is a test")
next(results)
for result in results:
    print(result)
