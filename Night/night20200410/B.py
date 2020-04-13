import itertools
n = int(input())
XY = []
for i in range(n):
    x, y = map(int, input().split())
    XY.append((x, y))
d = 0
for P in itertools.permutations(XY):
    for i in range(1, n):
        x0, y0 = P[i-1]
        x1, y1 = P[i]
        d += ((x0-x1)**2+(y0-y1)**2)**0.5
k = 1
for i in range(1, n+1):
    k *= i
print(d/k)
