n = int(input())
c = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(n - 1):
        if c[j + 1][i] - c[j][i] != c[j + 1][0] - c[j][0]:
            print("No")
            exit()
        if c[i][j + 1] - c[i][j] != c[0][j + 1] - c[0][j]:
            print("No")
            exit()

a = [0] * n
b = [0] * n
a[0] = c[0][0]
for i in range(n - 1):
    a[i + 1] = a[i] + c[i + 1][0] - c[i][0]
    b[i + 1] = b[i] + c[0][i + 1] - c[0][i]
mina = min(a)
if mina < 0:
    a = [a[i] - mina for i in range(n)]
    b = [b[i] + mina for i in range(n)]
minb = min(b)
if minb < 0:
    a = [a[i] + minb for i in range(n)]
    b = [b[i] - minb for i in range(n)]
if min(a) >= 0 and min(b) >= 0:
    print("Yes")
    print(*a)
    print(*b)
else:
    print("No")
