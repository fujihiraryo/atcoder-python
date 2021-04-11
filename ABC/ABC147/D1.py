MOD = 10 ** 9 + 7
n = int(input())
*a, = map(int, input().split())
cnt = [[0] * (n + 1) for _ in range(60)]
bit = [[0] * n for _ in range(60)]
for i in range(n):
    for j in range(60):
        cnt[j][i + 1] = cnt[j][i]
        if (1 << j) & a[i]:
            bit[j][i] = 1
            cnt[j][i + 1] += 1
        cnt[j][i + 1] %= MOD
ans = 0
for j in range(60):
    tmp = 0
    for i in range(n):
        if bit[j][i]:
            tmp += (n - 1 - i) - (cnt[j][n] - cnt[j][i + 1])
        else:
            tmp += cnt[j][n] - cnt[j][i + 1]
        tmp %= MOD
    ans += tmp * pow(2, j, MOD)
    ans %= MOD
print(ans)
