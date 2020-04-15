n = int(input())
d = int(input())
p = 10**9+7
N = [int(i) for i in list(str(n))]
DP = [[[0 for j in range(d)]for i in range(len(N))] for _ in range(2)]
for i in range(len(N)):
    if i == 0:
        for j in range(d):
            for k in range(N[i]):
                if k % d == j:
                    DP[0][i][j] += 1
                    DP[1][i][j] += 1
            if N[i] % d == j:
                DP[1][i][j] += 1
    else:
        for j in range(d):
            for k in range(N[i]):
                DP[0][i][j] += DP[1][i-1][(j-k) % d]
            for k in range(N[i], 10):
                DP[0][i][j] += DP[0][i-1][(j-k) % d]
            for k in range(N[i]+1):
                DP[1][i][j] += DP[1][i-1][(j-k) % d]
            for k in range(N[i]+1, 10):
                DP[1][i][j] += DP[1][i-1][(j-k) % d]
print(DP[1][-1][0]-1)
print(DP[0][0])
print(DP[1][0])
