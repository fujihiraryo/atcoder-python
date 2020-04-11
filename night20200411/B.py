n = int(input())
S = [int(input()) for i in range(n)]
S.sort()
x = sum(S)
if x % 10 == 0:
    for i in range(n):
        if S[i] % 10 != 0:
            x -= S[i]
            print(x)
            exit()
    print(0)
else:
    print(x)
