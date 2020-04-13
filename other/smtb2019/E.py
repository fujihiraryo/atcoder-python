mod = 10**9+7
n = int(input())
*A, = map(int, input().split())
X = [0, 0, 0]
cnt = 1
for a in A:
    cnt = cnt*X.count(a) % mod
    for i in range(3):
        if X[i] == a:
            X[i] += 1
            break
print(cnt % mod)
