MOD = 10 ** 9 + 7
MAX = 60
n, b, k = map(int, input().split())
*lst, = map(int, input().split())

# pow10[i] = pow(10, pow(2, i), b)
pow10 = [10 % b] * (MAX + 1)
for i in range(MAX):
    pow10[i + 1] = pow10[i] * pow10[i] % b

# dp[i][j] = 2**i桁でbで割ったあまりがjの個数
dp = [[0] * b for _ in range(MAX + 1)]
for c in lst:
    dp[0][c % b] += 1
for i in range(MAX):
    for j in range(b):
        for k in range(b):
            l = (pow10[i] * j + k) % b
            dp[i + 1][l] += dp[i][j] * dp[i][k]
            dp[i + 1][l] %= MOD

ans = [0] * b
ans[0] = 1
for i in range(MAX):
    if not (1 << i) & n:
        continue
    new = [0] * b
    for j in range(b):
        for k in range(b):
            l = (pow10[i] * j + k) % b
            new[l] += ans[j] * dp[i][k]
            new[l] %= MOD
    ans = new
print(ans[0])
