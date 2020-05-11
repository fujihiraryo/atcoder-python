n, m, x = map(int, input().split())
CA = [list(map(int, input().split())) for i in range(n)]
C = [CA[i][0] for i in range(n)]
A = [CA[i][1:] for i in range(n)]
MC = []
for s in range(1 << n):
    X = [0 for j in range(m)]
    c = 0
    for i in range(n):
        if (s >> i) & 1 == 1:
            for j in range(m):
                X[j] += A[i][j]
            c += C[i]
    if all([X[j] >= x for j in range(m)]):
        MC.append(c)
if MC == []:
    print(-1)
else:
    print(min(MC))
