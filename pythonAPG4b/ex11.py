a = input()
ans = 1
for i in range(len(a)//2):
    if(a[i*2+1] == '+'):
        ans += 1
    else:
        ans -= 1

print(ans)