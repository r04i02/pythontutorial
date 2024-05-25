n = int(input())
a = list(map(int,input().split()))
ans = min(a)
for i,v in enumerate(a):
    if ans == v:
        print(i+1)
        break