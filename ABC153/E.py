H, N = map(int, input().split())
A = []
B = []
for n in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
dp = [[0 for h in range(H + 1)] for n in range(N + 1)]
# dp[n][h]は0~n-1の魔法で体力hを削るのに使う魔力
for n in range(1, N+1):
    for h in range(1, H + 1):
        if A[n] > h:
            dp[n][h] = dp[n-1][h]
        else:
            x = dp[n-1][h]
            y = dp[n-1][h - A[n-1]]+B[n-1]
            z = dp[n][h - A[n]] + B[n]
            dp[n][h] = min(x, y, z)
print(dp[N][H])
