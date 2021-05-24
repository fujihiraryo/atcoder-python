n, m = map(int, input().split())
cond = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    cond[x].append((y, z))
dp = [0] * (1 << n)
dp[0] = 1
for s in range(1, 1 << n):
    x = bin(s).count("1")
    ok = 1
    for y, z in cond[x]:
        cnt = 0
        for i in range(n):
            if (1 << i) & s and i < y:
                cnt += 1
        if cnt > z:
            ok = 0
    if ok:
        for i in range(n):
            if (1 << i) & s:
                dp[s] += dp[s - (1 << i)]
print(dp[-1])
