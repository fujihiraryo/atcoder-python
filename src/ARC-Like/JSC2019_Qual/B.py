import bisect

MOD = 10 ** 9 + 7
n, k = map(int, input().split())
*a, = map(int, input().split())
cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            cnt += 1
rank = 0
a.sort()
for i in range(n):
    rank += bisect.bisect_left(a, a[i])
print((cnt * k + rank * (k - 1) * k // 2) % MOD)
