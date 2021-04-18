MOD = 3


pascal = [[0] * MOD for _ in range(MOD)]
pascal[0][0] = 1
for i in range(1, MOD):
    pascal[i][0] = 1
    for j in range(1, i + 1):
        pascal[i][j] = (pascal[i - 1][j - 1] + pascal[i - 1][j]) % MOD


def base(x):
    res = []
    y = x
    while y:
        res.append(y % MOD)
        y //= MOD
    return res


def lucas(x, y):
    if x < y or x < 0 or y < 0:
        return 0
    x_lst = base(x)
    y_lst = base(y)
    for _ in range(len(x_lst) - len(y_lst)):
        y_lst.append(0)
    res = 1
    for i, j in zip(x_lst, y_lst):
        res *= pascal[i][j]
        res %= MOD
    return res


n = int(input())
dic = {"W": 0, "B": 1, "R": 2}
rev = ["W", "B", "R"]
a = [dic[x] for x in input()]
ans = 0
for i in range(n):
    ans += lucas(n - 1, i) * a[i]
    ans %= MOD
ans *= pow(2, n - 1, MOD)
ans %= MOD
print(rev[ans])
