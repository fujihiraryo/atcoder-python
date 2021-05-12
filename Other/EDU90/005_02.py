MOD = 10 ** 9 + 7
n, b, k = map(int, input().split())
if b > 30:
    exit()
*lst, = map(int, input().split())
mat = [[0] * b for _ in range(b)]
for j in range(b):
    for c in lst:
        mat[j][(10 * j + c) % b] += 1
dp = [0] * b
dp[0] = 1
while n:
    if n % 2:
        tmp = [0] * b
        for i in range(b):
            for j in range(b):
                tmp[i] += mat[i][j] * dp[j]
                tmp[i] %= MOD
        dp = tmp
    n //= 2
    tmp = [[0] * b for _ in range(b)]
    for i in range(b):
        for j in range(b):
            for k in range(b):
                tmp[i][j] += mat[i][k] * mat[k][j]
                tmp[i][j] %= MOD
    mat = tmp
print(dp[0])
