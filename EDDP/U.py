n = int(input())
A = [list(map(int, input().split())) for i in range(n)]
DP = []
for s in range(2 ** n):
    bit = bin(s)[2:].zfill(n)
    tmp = 0
    for i in range(n):
        for j in range(i + 1, n):
            if bit[i] == "1" and bit[j] == "1":
                tmp += A[i][j]
    DP.append(tmp)
    t = s
    while t:
        DP[s] = max(DP[s], DP[t] + DP[s - t])
        t = (t - 1) & s
print(DP[-1])
