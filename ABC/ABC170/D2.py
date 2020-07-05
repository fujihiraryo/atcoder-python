n = int(input())
*A, = map(int, input().split())
maxA = max(A)
C = {a: 0 for a in A}
for a in A:
    C[a] += 1
D = {a: 0 for a in A}
for a in A:
    if C[a] > 1:
        D[a] = 1
    for b in range(2 * a, maxA + 1, a):
        D[b] = 1
print(sum([D[a] == 0 for a in A]))
