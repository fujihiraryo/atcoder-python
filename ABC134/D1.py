n = int(input())
*A, = map(int, input().split())
A = [0] + A
X = [0 for i in range(n + 1)]
for i in range(n, 0, -1):
    j = 2 * i
    while j <= n:
        X[i] += X[j]
        j += i
    X[i] = (X[i] + A[i]) % 2
print(sum(X))
B = []
for i in range(1, n+1):
    if X[i] == 1:
        B.append(i)
print(*B)
