import bisect
n = int(input())
S = list(input())
R, G, B = [], [], []
for i in range(n):
    if S[i] == 'R':
        R.append(i)
    if S[i] == 'G':
        G.append(i)
    if S[i] == 'B':
        B.append(i)
r = len(R)
g = len(G)
b = len(B)
cnt = 0
Rset, Gset, Bset = set(R), set(G), set(B)
# RGB
for i in range(r):
    g0 = bisect.bisect_right(G, R[i])
    for j in range(g0, g):
        b0 = bisect.bisect_right(B, G[j])
        cnt += b - b0
        x = 2*G[j]-R[i]
        if x in Bset:
            cnt -= 1
# RBG
for i in range(r):
    b0 = bisect.bisect_right(B, R[i])
    for j in range(b0, b):
        g0 = bisect.bisect_right(G, B[j])
        cnt += g - g0
        x = 2*B[j]-R[i]
        if x in Gset:
            cnt -= 1
# GBR
for i in range(g):
    b0 = bisect.bisect_right(B, G[i])
    for j in range(b0, b):
        r0 = bisect.bisect_right(R, B[j])
        cnt += r - r0
        x = 2*B[j]-G[i]
        if x in Rset:
            cnt -= 1
# GRB
for i in range(g):
    r0 = bisect.bisect_right(R, G[i])
    for j in range(r0, r):
        b0 = bisect.bisect_right(B, R[j])
        cnt += b - b0
        x = 2*R[j]-G[i]
        if x in Bset:
            cnt -= 1
# BRG
for i in range(b):
    r0 = bisect.bisect_right(R, B[i])
    for j in range(r0, r):
        g0 = bisect.bisect_right(G, R[j])
        cnt += g - g0
        x = 2*R[j]-B[i]
        if x in Gset:
            cnt -= 1
# BGR
for i in range(b):
    g0 = bisect.bisect_right(G, B[i])
    for j in range(g0, g):
        r0 = bisect.bisect_right(R, G[j])
        cnt += r - r0
        x = 2*G[j]-B[i]
        if x in Rset:
            cnt -= 1
print(cnt)
