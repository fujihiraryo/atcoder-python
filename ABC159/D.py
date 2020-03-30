from collections import Counter
N = int(input())
*A, = map(int, input().split())
C = Counter(A)
D = {}
for key in C.keys():
    D[key] = C[key] * (C[key] - 1) // 2
S = sum(D.values())
for k in range(N):
    print(S - C[A[k]] + 1)