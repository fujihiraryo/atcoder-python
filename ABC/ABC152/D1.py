n = int(input())
X = ['']
for i in range(1, 6):
    for j in range(10**i):
        X.append(str(j).zfill(i))
cnt = 0
for a in range(1, n+1):
    x = str(a)[0]
    y = str(a)[-1]
    if x == y:
        cnt += 1
    if y == '0':
        continue
    l, r = -1, len(X)-1
    while r-l > 1:
        c = (l+r)//2
        if int(y+X[c]+x) <= n:
            l = c
        else:
            r = c
    cnt += r
print(cnt)
