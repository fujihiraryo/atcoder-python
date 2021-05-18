def generate(n):
    # 1が連続しないn桁以内の2進数
    if n == 1:
        yield 0
        yield 1
    else:
        for s in generate(n - 1):
            if not s & 1:
                yield (s << 1)
                yield (s << 1) | 1
            else:
                yield s << 1


MOD = 10 ** 9 + 7
h, w = map(int, input().split())
c = [input() for _ in range(h)]
lst = list(generate(w + 1))
dic = {s: i for i, s in enumerate(lst)}
# dst[j][k][l] = j列にいるときのlst[k]の遷移先のl番目
dst = [[[None] * 2 for _ in lst] for _ in range(w)]
for j in range(w):
    for k, s in enumerate(lst):
        if j == 0:
            msk = (1 << w) - 1
            dst[j][k][0] = dic[(s & msk) << 1]
            if not s & 1:
                dst[j][k][1] = dic[(s & msk) << 1 | 1]
        else:
            msk = (1 << (w + 1)) - 1 - (1 << j)
            dst[j][k][0] = dic[s & msk]
            if not s & (1 << (j - 1)) and not s & (1 << (j + 1)):
                dst[j][k][1] = dic[s & msk | (1 << j)]

n = len(lst)
dp = [0] * n
dp[0] = 1
for i in range(h):
    for j in range(w):
        nx = [0] * n
        for k, s in enumerate(lst):
            if j == 0:
                nx[dst[j][k][0]] += dp[k]
                nx[dst[j][k][0]] %= MOD
                if s & 1 or (w > 1 and s & 2) or c[i][j] == "#":
                    continue
                nx[dst[j][k][1]] += dp[k]
                nx[dst[j][k][1]] %= MOD
            else:
                nx[dst[j][k][0]] += dp[k]
                nx[dst[j][k][0]] %= MOD
                if (
                    s & (1 << (j - 1))
                    or s & (1 << j)
                    or s & (1 << (j + 1))
                    or s & (1 << (j + 2))
                    or c[i][j] == "#"
                ):
                    continue
                nx[dst[j][k][1]] += dp[k]
                nx[dst[j][k][1]] %= MOD
        dp = nx
print(sum(dp) % MOD)
