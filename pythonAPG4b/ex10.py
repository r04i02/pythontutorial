n = int(input())
a = list(map(int,input().split()))
average = 0
for i in range(n):
    average += a[i]

average //= n
for i in range(n):
    print(abs(a[i]-average))