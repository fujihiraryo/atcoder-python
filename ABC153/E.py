inf = 10**10
H, N = map(int, input().split())
A = []
B = []
for n in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
dp = [[0 for h in range(H+1)] for n in range(N+1)]
# dp[n][h]は0~n-1の魔法で体力hを削るのに使う魔力
dp[0] = [0] + [inf for h in range(1, H+1)]
for n in range(1, N+1):
    for h in range(H+1):
        dp[n][h] = min(dp[n - 1][h], dp[n][max(0, h - A[n - 1])] + B[n - 1])
print(dp[N][H])
