
#Joe is a prisoner who has been sentenced to hard labor for his crimes. Each day he is given a pile of large rocks to break into tiny rocks. To make matters worse, they do not provide any tools to work with. Instead, he must use the rocks themselves. He always picks up the largest two stones and smashes them together. If they are of equal weight, they both disintegrate entirely. If one is larger, the smaller one is disintegrated and the larger one is reduced by the weight of the smaller one. Eventually there is either one stone left that cannot be broken or all of the stones have been smashed. Determine the weight of the last stone, or return 0 if there is none.

a_count = int(input().strip())
a = []

for _ in range(a_count):
    a_item = int(input().strip())
    a.append(a_item)

def lastStoneWeight(a):
    # Write your code here
    print(f"before sort: {a}")
    a.sort()
    print(f"after sort: {a}")
    b = a[0]
    for i in range(len(a)):
        if len(a) >= 2:
            b = abs(a[-1] - a[-2])
            if b == 0:
                a.remove(a[-1])
                a.remove(a[-1])
            else:
                a.remove(a[-1])
                a[-1] = b
        else:
            print(f"last output: {a}")
            return b

print(f"result: {lastStoneWeight(a)}")