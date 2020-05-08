n, m = map(int, input().split())
*H, = map(int, input().split())
X = [1 for i in range(n)]
for j in range(m):
    a, b = map(int, input().split())
    if H[a - 1] <= H[b - 1]:
        X[a - 1] = 0
    if H[b - 1] <= H[a - 1]:
        X[b - 1] = 0
print(sum(X))
