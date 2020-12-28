n, k = map(int, input().split())
(*a,) = map(int, input().split())
a.sort()
s = sum(a)
div = [1, s]
tmp = 2
while tmp ** 2 < s:
    if s % tmp == 0:
        div.append(tmp)
        div.append(s // tmp)
    tmp += 1
div.sort(reverse=True)
for d in div:
    rem = [a[i] % d for i in range(n)]
    rem.sort()
    m = len(rem)
    cum0, cum1 = [0] * (m + 1), [0] * (m + 1)
    for i in range(1, m + 1):
        cum0[i] = cum0[i - 1] + rem[i - 1]
        cum1[i] = cum1[i - 1] + d - rem[i - 1]
    for i in range(m):
        if cum0[i] == cum1[m] - cum1[i]:
            break
    if cum0[i] <= k:
        print(d)
        exit()
