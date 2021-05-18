MOD = 10 ** 9 + 7
h, w = map(int, input().split())
if w > 17:
    exit()
c = [input() for _ in range(h)]
dp = [0] * (1 << (w + 1))
dp[0] = 1
for i in range(h):
    for j in range(w):
        nx = [0] * (1 << (w + 1))
        for s in range(1 << (w + 1)):
            if j == 0:
                msk = (1 << w) - 1
                nx[(s & msk) << 1] += dp[s]
                nx[(s & msk) << 1] %= MOD
                if s & 1 or (w > 1 and s & 2) or c[i][j] == "#":
                    continue
                nx[(s & msk) << 1 | 1] += dp[s]
                nx[(s & msk) << 1 | 1] %= MOD
            else:
                msk = (1 << (w + 1)) - 1 - (1 << j)
                nx[s & msk] += dp[s]
                nx[s & msk] %= MOD
                if (
                    s & (1 << (j - 1))
                    or s & (1 << j)
                    or s & (1 << (j + 1))
                    or s & (1 << (j + 2))
                    or c[i][j] == "#"
                ):
                    continue
                nx[s & msk | (1 << j)] += dp[s]
                nx[s & msk | (1 << j)] %= MOD
        dp = nx
print(sum(dp) % MOD)
