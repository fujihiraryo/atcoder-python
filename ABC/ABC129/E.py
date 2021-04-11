MOD = 10 ** 9 + 7
a = input()
n = len(a)
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + int(a[i - 1] == "1")
ans = 1
for i in range(1, n + 1):
    ans = (3 * ans - pow(2, s[i] + 1, MOD) * int(a[i - 1] == "0")) % MOD
print(ans)
