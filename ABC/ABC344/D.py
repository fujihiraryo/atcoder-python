t = input()
n = int(input())
a = []
s = [set() for _ in range(n)]
for i in range(n):
    a_s = input().split()
    a.append(int(a_s[0]))
    s[i] = set(a_s[1:])

m = len(t)
INF = 10**10
dp = [[INF] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(m + 1):
        dp[i + 1][j] = dp[i][j]
    for j in range(m):
        for k in range(j + 1):
            if t[k : j + 1] in s[i]:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][k] + 1)
print(dp[n][m] if dp[n][m] < INF else -1)
