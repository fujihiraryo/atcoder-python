d, g = map(int, input().split())
v, p, c = [], [], []
for i in range(d):
    pi, ci = map(int, input().split())
    v.append(100 * (i + 1))
    p.append(pi)
    c.append(ci)
ans = 1 << 30
for s in range(1 << d):
    tmp, cnt = 0, 0
    for i in range(d):
        if (1 << i) & s:
            tmp += v[i] * p[i] + c[i]
            cnt += p[i]
    for i in range(d)[::-1]:
        if tmp >= g:
            break
        if (1 << i) & s:
            continue
        x = min((g - tmp) // v[i], p[i] - 1)
        cnt += x
        tmp += x * v[i]
    if tmp >= g:
        ans = min(ans, cnt)
print(ans)
