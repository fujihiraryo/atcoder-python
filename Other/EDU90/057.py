def free_degree(a, b):
    global MOD
    n, m = len(a), len(a[0])
    r = 0
    for j in range(m):
        p = -1
        for i in range(r, n):
            if a[i][j]:
                p = i
                break
        if p == -1:
            continue
        a[p], a[r] = a[r], a[p]
        b[p], b[r] = b[r], b[p]
        for i in range(n):
            if i == r or not a[i][j]:
                continue
            for k in range(m):
                a[i][k] ^= a[r][k]
            b[i] ^= b[r]
        r += 1
    for i in range(n):
        if all(a[i][j] == 0 for j in range(m)) and b[i]:
            return -1
    return m - r


MOD = 998244353
int0 = lambda x: int(x) - 1
n, m = map(int, input().split())
a = [[0] * n for _ in range(m)]
for j in range(n):
    input()
    for i in map(int0, input().split()):
        a[i][j] = 1
b = list(map(int, input().split()))
deg = free_degree(a, b)
print(0 if deg == -1 else pow(2, deg, MOD))
