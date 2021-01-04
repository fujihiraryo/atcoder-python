MOD = 10 ** 9 + 7
n = int(input())
# 二項係数
inv = lambda a: pow(a, MOD - 2, MOD)
fct = [1]
ict = [1]
for i in range(1, n + 1):
    fct.append(fct[-1] * i % MOD)
    ict.append(ict[-1] * inv(i) % MOD)
cmb = lambda a, b: fct[a] * ict[b] * ict[a - b] % MOD
# 隣接リストの構築
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    tree[x - 1].append(y - 1)
    tree[y - 1].append(x - 1)
# 0を根とするときのトポロジカル順序と各頂点の子のリストと親
child = [[] for _ in range(n)]
parent = [None] * n
order = []
que = [0]
for x in que:
    order.append(x)
    for y in tree[x]:
        if y == parent[x]:
            continue
        child[x].append(y)
        parent[y] = x
        que.append(y)
# 各頂点を根とする部分木の大きさ
size = [1] * n
for x in order[::-1]:
    for y in child[x]:
        size[x] += size[y]
# 葉から順に部分木の計算
dp0 = [1] * n
dp1 = [{} for _ in range(n)]
for x in order[::-1]:
    dp0[x] = fct[size[x] - 1]
    for y in child[x]:
        dp0[x] = dp0[x] * dp0[y] * ict[size[y]] % MOD
    for y in child[x]:
        dp1[x][y] = dp0[x] * inv(dp0[y]) * inv(cmb(size[x] - 1, size[y]) % MOD) % MOD
# 根から順にxを根とする木全体の計算
for x in order[1:]:
    dp0[x] = dp0[x] * dp1[parent[x]][x] * cmb(n - 1, n - size[x]) % MOD
    for y in child[x]:
        dp1[x][y] = (
            dp1[x][y] * dp1[parent[x]][x] * cmb(n - 1 - size[y], n - size[x]) % MOD
        )
print(*dp0, sep="\n")
