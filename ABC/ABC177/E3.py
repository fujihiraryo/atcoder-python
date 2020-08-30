n = int(input())
*A, = map(int, input().split())
m = max(2, max(A))
P = {p: True for p in range(2, m + 1)}
for i in range(2, m + 1):
    for j in range(2 * i, m + 1, i):
        P[j] = False
Pmap = {p: 0 for p in P if P[p]}
Amap = {a: 0 for a in range(1, m + 1)}
for a in A:
    Amap[a] += 1
for p in Pmap:
    for a in range(p, m + 1, p):
        Pmap[p] += Amap[a]
s = max(Pmap.values())
if s < 2:
    print('pairwise coprime')
elif s < n:
    print('setwise coprime')
else:
    print('not coprime')
