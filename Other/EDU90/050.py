MOD = 10 ** 9 + 7
n, l = map(int, input().split())
a = [0] * (n + 1)
a[0] = 1
for i in range(1, n + 1):
    a[i] = a[i - 1]
    if i - l >= 0:
        a[i] += a[i - l]
        a[i] %= MOD
print(a[n])
