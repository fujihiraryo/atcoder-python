n, k = map(int, input().split())
*H, = map(int, input().split())
X = [0]
for i in range(1, n):
    x = 1 << 30
    for j in range(1, min(i, k)+1):
        x = min(x, X[i-j]+abs(H[i]-H[i-j]))
    X.append(x)
print(X[n-1])
