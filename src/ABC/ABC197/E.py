n = int(input())
x, c = [], []
for _ in range(n):
    xi, ci = map(int, input().split())
    x.append(xi)
    c.append(ci)
cs = list(set(c))
cs.sort()
rank = {}
for i, ci in enumerate(cs):
    rank[ci] = i
lstlst = [[] for r in range(len(cs))]
for i in range(n):
    lstlst[rank[c[i]]].append(x[i])
for lst in lstlst:
    lst.sort()
lstlst = [[0]] + lstlst + [[0]]
# dp
m = len(lstlst)
y = [[None] * m for _ in range(2)]
for i in range(m):
    y[0][i] = lstlst[i][0]
    y[1][i] = lstlst[i][-1]
dp = [[1 << 60] * m for _ in range(2)]
dp[0][0] = 0
dp[1][0] = 0
for i in range(1, m):
    dp[0][i] = min(
        dp[0][i - 1] + abs(y[1][i - 1] - y[0][i - 1]) + abs(y[1][i - 1] - y[0][i]),
        dp[1][i - 1] + abs(y[1][i - 1] - y[0][i - 1]) + abs(y[0][i - 1] - y[0][i]),
    )
    dp[1][i] = min(
        dp[0][i - 1] + abs(y[1][i - 1] - y[0][i - 1]) + abs(y[1][i - 1] - y[1][i]),
        dp[1][i - 1] + abs(y[1][i - 1] - y[0][i - 1]) + abs(y[0][i - 1] - y[1][i]),
    )
print(dp[0][m - 1])
