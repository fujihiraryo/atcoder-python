C = [[0 for j in range(51)] for i in range(51)]
for i in range(51):
    C[i][0] = 1
for i in range(1, 51):
    for j in range(1, 51):
        C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
n, a, b = map(int, input().split())
*V, = map(int, input().split())
V.sort(reverse=True)
print(sum(V[:a]) / a)
if V[0] == V[a - 1]:
    x = V.count(V[a - 1])
    print(sum([C[x][y] for y in range(a, b + 1)]))
else:
    x = V.count(V[a - 1])
    y = a - len([v for v in V if v > V[a - 1]])
    print(C[x][y])
