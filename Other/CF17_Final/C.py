n = int(input())
(*d,) = map(int, input().split())
cnt = [0] * 13
for i in range(n):
    cnt[d[i]] += 1
ans = 0
for s in range(1 << 13):
    x = []
    for i in range(13):
        if cnt[i] == 0:
            continue
        elif cnt[i] == 1:
            if (1 << i) & s:
                x.append(i)
            else:
                x.append(24 - i)
        elif cnt[i] == 2:
            x.append(i)
            x.append(24 - i)
        else:
            x.append(i)
            x.append(i)
            x.append(24 - i)
    x.append(0)
    k = len(x)
    tmp = 24
    for i in range(k - 1):
        for j in range(i + 1, k):
            tmp = min(tmp, abs(x[i] - x[j]), 24 - abs(x[i] - x[j]))
    ans = max(ans, tmp)
print(ans)
