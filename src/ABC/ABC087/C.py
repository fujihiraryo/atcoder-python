n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]
s = [[0] * (n + 1) for _ in range(2)]
for i in range(n):
    s[0][i + 1] = s[0][i] + a[0][i]
    s[1][i + 1] = s[1][i] + a[1][i]
ans = max([s[0][i + 1] + s[1][n] - s[1][i] for i in range(n)])
print(ans)
