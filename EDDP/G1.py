import sys
sys.setrecursionlimit(10000)
n, m = map(int, input().split())
G = [[] for i in range(n)]
for j in range(m):
    x, y = map(int, input().split())
    G[x-1].append(y-1)
DP = [None for i in range(n)]


def dp(i):
    if DP[i] != None:
        return DP[i]
    ret = 0
    for j in G[i]:
        ret = max(ret, dp(j)+1)
    DP[i] = ret
    return ret


print(max([dp(i) for i in range(n)]))
