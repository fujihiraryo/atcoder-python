N = int(input())
A = [format(i, "060b") for i in map(int, input().split())]
ans = 0
mod = 10 ** 9 + 7
for k in range(60):
    count = [a[60 - 1 - k] for a in A].count("0")
    ans += count * (N - count) * (2 ** k) % mod
print(ans % mod)
