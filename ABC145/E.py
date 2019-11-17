import numpy as np
N, T = map(int, input().split())
AB = [tuple(map(int, input().split())) for n in range(N)]
AB.sort()

dp = np.zeros(T, dtype=int)
ans = 0
for a, b in AB:
    ans = max(ans, dp[-1] + b)
    np.maximum(dp[a:], dp[:-a] + b, out=dp[a:])
print(ans)
