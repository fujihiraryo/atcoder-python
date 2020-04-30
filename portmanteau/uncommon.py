n, m = map(int, input().split())
A = [int(input()) for i in range(n)]
# Aのカウンターを作る
C = {a: 0 for a in range(1, 10**5 + 1)}
for a in A:
    C[a] += 1
# Aの中で1,...,mの倍数がそれぞれ何個あるか数える
D = {}
for j in range(1, m + 1):
    D[j] = sum([C[k] for k in range(j, 10**5 + 1, j)])
# エラトステネスの篩
P = {}
X = list(range(2, m + 2))
while X[0]**2 <= m:
    x0 = X[0]
    P[x0] = 0
    X_ = []
    for x in X:
        if x != x0 and x % x0 == 0:
            P[x] = x0
        elif x % x0 != 0:
            X_.append(x)
    X = X_
for x in X:
    P[x] = 0
# 1,...,mの素因数のリストを作る
M = {1: []}
for j in range(2, m + 1):
    M[j] = set()
    k = j
    while P[k]:
        M[j].add(P[k])
        k = k // P[k]
    M[j].add(k)
    M[j] = list(M[j])
# 1,...,mと互いに素なaの個数を包除原理により求める
for j in range(1, m + 1):
    Mj = M[j]
    cnt = 0
    for k in range(2**len(Mj)):
        # kを2進数展開したとき1になる桁の積
        x = 1
        # 1になる桁の個数の偶奇により決まる符号
        sgn = 1
        for ll in range(len(Mj)):
            if k % 2 != 0:
                x *= Mj[ll]
                sgn *= -1
            k = k // 2
        cnt += sgn * D[x]
    print(cnt)
