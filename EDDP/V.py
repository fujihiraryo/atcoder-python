n, m = map(int, input().split())
G = [[] for i in range(n)]
for i in range(n - 1):
    x, y = map(int, input().split())
    G[x - 1].append(y - 1)
    G[y - 1].append(x - 1)
Q = [0]
V = [False for i in range(n)]
C = [[] for i in range(n)]
P = [None for i in range(n)]
while Q:
    x = Q.pop()
    V[x] = True
    for y in G[x]:
        if not V[y]:
            C[x].append(y)
            P[y] = x
            Q.append(y)
DP = [None for i in range(n)]
for i in range(n):
    if C[i] == []:
        DP[i] = 1


def dp(i):
    if DP[i] is not None:
        return DP[i]
    tmp = 1
    for j in C[i]:
        tmp *= 1 + dp(j)
    DP[i] = tmp
    return DP[i]


print(P)
print(C)
print(dp(0) % m)
print(DP)

ANS = [None for i in range(n)]
ANS[0] = dp(0)


def ans(i):
    if ANS[i] is not None:
        return ANS[i]
    return DP[i] * ans(P[i]) // (1 + DP[i])


for i in range(n):
    print(ans(i))
