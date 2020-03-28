N, X, Y = map(int, input().split())
f = [0] * N
for i in range(1, N):
    for j in range(i + 1, N + 1):
        d = min(j - i, abs(i - X) + abs(j - Y) + 1)
        f[d] += 1
for k in range(1, N):
    print(f[k])