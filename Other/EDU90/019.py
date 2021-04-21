from functools import lru_cache

INF = 10 ** 9
n = int(input())
*a, = map(int, input().split())


@lru_cache(None)
def dp(i, j):
    if i == j:
        return 0
    res = abs(a[i] - a[j - 1]) + dp(i + 1, j - 1)
    for k in range(i + 2, j, 2):
        res = min(res, dp(i, k) + dp(k, j))
    return res


print(dp(0, 2 * n))
