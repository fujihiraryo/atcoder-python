n, q = map(int, input().split())
n -= 2
X = [[n] * n, [n] * n]
H = [n, n]
ans = n ** 2
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 2
    for i in range(b, H[a]):
        X[a][i] = H[a ^ 1]
    H[a] = min(H[a], b)
    ans -= X[a][b]
print(ans)
