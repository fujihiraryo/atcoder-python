n = int(input())
A = [list(map(int, input().split())) for i in range(n)]
p = 10 ** 9 + 7
DP = [-1 for s in range(1 << n)]
DP[0] = 1


def dp(s, l):
    if DP[s] != -1:
        return DP[s]
    tmp = 0
    for i in range(n):
        if s & (1 << i) and A[l - 1][i]:
            tmp += dp(s & ~(1 << i), l - 1)
    DP[s] = tmp % p
    return DP[s]


print(dp((1 << n) - 1, n))
