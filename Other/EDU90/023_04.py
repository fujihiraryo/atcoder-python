MOD = 10 ** 9 + 7
h, w = map(int, input().split())
c = [[1 if x == "#" else 0 for x in input()] for _ in range(h)]
dp = {}
dp[0] = 1
for i in range(h):
    for j in range(w):
        nx = {}
        for s in dp:
            if dp[s] == 0:
                continue
            t = s >> 1
            if t in nx:
                nx[t] += dp[s]
                nx[t] %= MOD
            else:
                nx[t] = dp[s]
            ok = 1
            if i - 1 >= 0 and j - 1 >= 0 and s & (1 << 0):
                ok = 0
            if i - 1 >= 0 and s & (1 << 1):
                ok = 0
            if i - 1 >= 0 and j + 1 < w and s & (1 << 2):
                ok = 0
            if j - 1 >= 0 and s & (1 << w):
                ok = 0
            if ok and c[i][j] == 0:
                t = (s >> 1) + (1 << w)
                if t in nx:
                    nx[t] += dp[s]
                    nx[t] %= MOD
                else:
                    nx[t] = dp[s]
        dp = nx
print(sum(dp[s] for s in dp) % MOD)
