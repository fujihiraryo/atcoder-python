h, w, m = map(int, input().split())
R = [0] * h
C = [0] * w
XY = [tuple(map(lambda x: int(x) - 1, input().split())) for i in range(m)]
for x, y in XY:
    R[x] += 1
    C[y] += 1
maxR, maxC = max(R), max(C)
cnt0 = R.count(maxR) * C.count(maxC)
cnt1 = sum(R[x] == maxR and C[y] == maxC for x, y in XY)
print(maxR + maxC - int(cnt0 == cnt1))
