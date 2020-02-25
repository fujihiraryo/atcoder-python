N = int(input())
A, B, C = [], [], []
for n in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
a, b, c = 0, 0, 0
for n in range(N):
    a, b, c = A[n] + max(b, c), B[n] + max(c, a), C[n] + max(a, b)
print(max(a, b, c))
