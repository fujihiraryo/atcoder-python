n, s = map(int, input().split())
a, b = [], []
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
dp = [[0] * (s + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(s + 1):
        if j - a[i] >= 0 and dp[i][j - a[i]]:
            dp[i + 1][j] = 1
        elif j - b[i] >= 0 and dp[i][j - b[i]]:
            dp[i + 1][j] = 1
if dp[n][s]:
    ans = []
    j = s
    for i in range(n)[::-1]:
        if j - a[i] >= 0 and dp[i][j - a[i]]:
            ans.append("A")
            j -= a[i]
        elif j - b[i] >= 0 and dp[i][j - b[i]]:
            ans.append("B")
            j -= b[i]
    print("".join(ans[::-1]))
else:
    print("Impossible")
