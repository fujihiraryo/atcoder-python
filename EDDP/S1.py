n = int(input())
d = int(input())
p = 10**9+7
DP = {}
for i in range(10):
    DP[i] = [j % d for j in range(d)]
