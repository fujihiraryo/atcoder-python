MOD = 10 ** 9 + 7
n = int(input())
*a, = map(int, input().split())
a = list(set(a))
a.sort()
n = len(a)
b = [0] * (n - 1)
for i in range(n - 1):
    b[i] = a[i + 1] - a[i]
ans = a[0] + 1
for i in range(n - 1):
    ans *= b[i] + 1
    ans %= MOD
print(ans)
