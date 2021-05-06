n, m = map(int, input().split())
cond = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    cond[x].append((y, z))
dp = [0] * (1 << n)
dp[0] = 1
for s in range(1, 1 << n):
    x = bin(s).count("1")
    if any(bin(s)[-y:].count("1") > z for y, z in cond[x]):
        continue
    t = s
    while t:
        i = len(bin(t)) - 3
        dp[s] += dp[s - (1 << i)]
        t -= 1 << i
print(dp[-1])
