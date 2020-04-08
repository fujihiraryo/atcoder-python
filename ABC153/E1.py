h, n = map(int, input().split())
A, B = [], []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
F = [0]
for i in range(1, h+1):
    f = 1 << 30
    for a, b in zip(A, B):
        if i < a:
            f = min(f, b)
        else:
            f = min(f, F[i-a]+b)
    F.append(f)
print(f)
