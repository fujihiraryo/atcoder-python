MOD = 200
n = int(input())
a = [int(x) % MOD for x in input().split()]
dp0 = [[None] * MOD for _ in range(n + 1)]
dp1 = [[None] * MOD for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(MOD):
        # できるだけi番目を使わない
        if dp0[i - 1][j] is not None:
            dp0[i][j] = dp0[i - 1][j][:]
        elif dp0[i - 1][(j - a[i - 1]) % MOD] is not None:
            dp0[i][j] = dp0[i - 1][(j - a[i - 1]) % MOD][:]
            dp0[i][j].append(i)
        elif j == a[i - 1] % MOD:
            dp0[i][j] = [i]
        # できるだけi番目を使う
        if j == a[i - 1] % MOD:
            dp1[i][j] = [i]
        elif dp1[i - 1][(j - a[i - 1]) % MOD] is not None:
            dp1[i][j] = dp1[i - 1][(j - a[i - 1]) % MOD][:]
            dp1[i][j].append(i)
        elif dp1[i - 1][j] is not None:
            dp1[i][j] = dp1[i - 1][j][:]
for i in range(1, n + 1):
    for j in range(MOD):
        if dp0[i][j] is None or dp1[i][j] is None:
            continue
        if dp0[i][j] == [] or dp1[i][j] == [] or dp0[i][j] == dp1[i][j]:
            continue
        print("Yes")
        print(len(dp0[i][j]), *dp0[i][j])
        print(len(dp1[i][j]), *dp1[i][j])
        exit()
print("No")
