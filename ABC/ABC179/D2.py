p = 998244353
n, k = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(k)]
DP = [0] * (2 * n + 1)
DP[0] = 1
DP[1] = -1
for i in range(n):
    for l, r in LR:
        DP[i + l] += DP[i]
        DP[i + r + 1] -= DP[i]
    DP[i + 1] += DP[i]
    DP[i + 1] %= p
print(DP[n - 1])
