def factrize(x):
    # 試し割りによるxの素因数分解
    f = {}
    tmp = x
    i = 2
    while i**2 <= tmp:
        cnt = 0
        while tmp % i == 0:
            cnt += 1
            tmp = tmp // i
        if cnt > 0:
            f[i] = cnt
        i += 1
    if tmp != 1 or f == {}:
        f[tmp] = 1
    return f


C = []
c = 0
for i in range(50):
    if i in (1, 3, 6, 10, 15, 21, 28, 36, 45):
        c += 1
    C.append(c)

n = int(input())
if n == 1:
    print(0)
else:
    f = factrize(n)
    ans = 0
    for i in f.keys():
        ans += C[f[i]]
    print(ans)
