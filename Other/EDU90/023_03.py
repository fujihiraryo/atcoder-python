MOD = 10 ** 9 + 7
h, w = map(int, input().split())
if w > 17:
    exit()
c = [[1 if x == "#" else 0 for x in input()] for _ in range(h)]
dp = [0] * (1 << (w + 1))
dp[0] = 1
for i in range(h):
    for j in range(w):
        nx = [0] * (1 << (w + 1))
        for s in range(1 << (w + 1)):
            nx[s >> 1] += dp[s]
            nx[s >> 1] %= MOD
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
                nx[(s >> 1) + (1 << w)] += dp[s]
                nx[(s >> 1) + (1 << w)] %= MOD
        dp = nx
print(sum(dp) % MOD)
