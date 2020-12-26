import sys

sys.setrecursionlimit(100000)

MOD = 10 ** 9 + 7
n, k = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
quene = [0]
visited = [0] * n
child = [[] for _ in range(n)]
while quene:
    x = quene.pop()
    visited[x] = 1
    for y in graph[x]:
        if visited[y]:
            continue
        child[x].append(y)
        quene.append(y)
memo = [None] * n


def rec(x):
    if memo[x] is not None:
        return memo[x]
    prd = 1
    tmp = k - 2
    for y in child[x]:
        prd = (prd * tmp * rec(y)) % MOD
        tmp -= 1
    memo[x] = prd
    return prd


prd = 1
tmp = k - 1
for x in child[0]:
    prd = (prd * tmp * rec(x)) % MOD
    tmp -= 1
print(k * prd % MOD)
