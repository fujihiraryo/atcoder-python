n = int(input())


def div3(x):
    # 3で割れるだけ割って、割れた回数と結果を返す
    y = x
    c = 0
    while y % 3 == 0:
        y //= 3
        c += 1
    return c, y


cnt = [0] * n
fct = [1] * n
for x in range(1, n):
    c, y = div3(x)
    cnt[x] = cnt[x - 1] + c
    fct[x] = fct[x - 1] * y % 3


def cmb(x, y):
    # xCyを3で割ったあまり
    if cnt[x] > cnt[x - y] + cnt[y]:
        return 0
    return fct[x] * fct[x - y] * fct[y] % 3


dic = {"W": 0, "B": 1, "R": 2}
rev = ["W", "B", "R"]
a = [dic[x] for x in input()]
ans = 0
for i in range(n):
    ans += cmb(n - 1, i) * a[i]
    ans %= 3
ans *= pow(2, n - 1, 3)
ans %= 3
print(rev[ans])
