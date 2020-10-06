import sys

sys.setrecursionlimit(100000)
# n = int(input())
# d = int(input())
n = 10 ** 10000
d = 100
p = 10 ** 9 + 7
DP = {}
DP[-1] = [0] * d
DP[0] = [0] * d
DP[0][0] = 1


def dp(i):
    try:
        return DP[i]
    except BaseException:
        pass
    q, r = i // 10, i % 10
    DP[i] = []
    for j in range(d):
        tmp = 0
        for k in range(r + 1):
            tmp += dp(q)[(j - k) % d]
        for k in range(r + 1, 10):
            tmp += dp(q - 1)[(j - k) % d]
        DP[i].append(tmp % p)
    return DP[i]


print((dp(n)[0] - 1) % p)
