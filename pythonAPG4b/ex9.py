n = int(input())
for i in range(n+1):
    if i == 0:
        a = int(input())
    else:
        op,b = input().split()
        b = int(b)
        if op == '+':
            a += b
        elif op == '-':
            a -= b
        elif op == '*':
            a *= b
        elif op == '/':
            if b == 0:
                print("error")
                break
            else:
                a //= b
    if i != 0:
        print(
            i,
            a,
            sep = " "
        )