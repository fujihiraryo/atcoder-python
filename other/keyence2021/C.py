from collections import defaultdict

MOD = 998244353
two_third = 2 * pow(3, MOD - 2, MOD) % MOD
h, w, k = map(int, input().split())
_grid = {}
for _ in range(k):
    i, j, c = input().split()
    i, j = int(i) - 1, int(j) - 1
    _grid[(i, j)] = c


def grid(i, j):
    if (i, j) in _grid:
        return _grid[(i, j)]
    if 0 <= i < h and 0 <= j < w:
        return ""
    return None


dp0 = defaultdict(int)
dp0[0] = 1
for j in range(w):
    if grid(0, j - 1) in ("R", "X"):
        dp0[j] = (dp0[j] + dp0[j - 1]) % MOD
    if grid(0, j - 1) == "":
        dp0[j] = (dp0[j] + dp0[j - 1] * two_third) % MOD
    if grid(0, j) == "":
        dp0[j] = dp0[j] * 3 % MOD
for i in range(1, h):
    dp1 = defaultdict(int)
    for j in range(w):
        upper = grid(i - 1, j)
        left = grid(i, j - 1)
        if upper in ("D", "X"):
            if left == "":
                dp1[j] = (dp1[j] + dp0[j] * 3) % MOD
            else:
                dp1[j] = (dp1[j] + dp0[j]) % MOD
        if upper == "":
            if left == "":
                dp1[j] = (dp1[j] + dp0[j] * 2) % MOD
            else:
                dp1[j] = (dp1[j] + dp0[j] * two_third) % MOD
        if left in ("R", "X"):
            if upper == "":
                dp1[j] = (dp1[j] + dp1[j - 1] * 3) % MOD
            else:
                dp1[j] = (dp1[j] + dp1[j - 1]) % MOD
        if left == "":
            if upper == "":
                dp1[j] = dp1[j] + dp1[j - 1] * 2
            else:
                dp1[j] = (dp1[j] + dp1[j - 1] * two_third) % MOD
        if grid(i, j) == "":
            dp1[j] = dp1[j] * 3 % MOD
    dp0 = dp1
    print(dp0)
print(dp0[w - 1])
