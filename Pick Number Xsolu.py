
n=int(input())
a=input().split()
b=[]
for i in range(1,100):
    b.append(a.count(f"{i}")+a.count(f"{i+1}"))
print(max(b))