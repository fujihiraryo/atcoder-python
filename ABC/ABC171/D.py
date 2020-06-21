n = int(input())
*A, = map(int, input().split())
C = {i: 0 for i in range(1, 10**5 + 1)}
for a in A:
    C[a] += 1
s = sum(A)
q = int(input())
for _ in range(q):
    b, c = map(int, input().split())
    tmp = C[b]
    C[b] = 0
    C[c] += tmp
    s += (c - b) * tmp
    print(s)
