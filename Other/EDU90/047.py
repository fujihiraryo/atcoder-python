MOD = 10 ** 9 + 7
n = int(input())
pow3 = [1] * n
for i in range(1, n):
    pow3[i] = pow3[i - 1] * 3 % MOD
inv3 = pow(3, MOD - 2, MOD)

pow5 = [1] * n
for i in range(1, n):
    pow5[i] = pow5[i - 1] * 5 % MOD
inv5 = pow(5, MOD - 2, MOD)


s = input()
t = input()
d = {"R": 0, "G": 1, "B": 2}
a, b = [], []
for i in range(n):
    a.append(d[s[i]])
    b.append(d[t[i]])
b0 = [(0 - b[i]) % 3 for i in range(n)]
b1 = [(1 - b[i]) % 3 for i in range(n)]
b2 = [(2 - b[i]) % 3 for i in range(n)]


def count(a, b):
    cnt = 0
    x3, y3 = 0, 0
    x5, y5 = 0, 0
    for i in range(n):
        x3 = (a[n - 1 - i] + x3 * 3) % MOD
        x5 = (a[n - 1 - i] + x5 * 5) % MOD
        y3 = (y3 + b[i] * pow3[i]) % MOD
        y5 = (y5 + b[i] * pow5[i]) % MOD
        if x3 == y3 and x5 == y5:
            cnt += 1
    for i in range(n - 1):
        x3 = (x3 - a[n - 1 - i] * pow3[n - 1 - i]) % MOD
        x5 = (x5 - a[n - 1 - i] * pow5[n - 1 - i]) % MOD
        y3 = (y3 - b[i]) * inv3 % MOD
        y5 = (y5 - b[i]) * inv5 % MOD
        if x3 == y3 and x5 == y5:
            cnt += 1
    return cnt


ans = count(a, b0) + count(a, b1) + count(a, b2)
print(ans)
