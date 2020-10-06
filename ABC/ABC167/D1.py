n, k = map(int, input().split())
(*A,) = map(int, input().split())
A = [0] + A
bit = list(bin(k)[2:][::-1])
m = len(bit)
DP = [[None for j in range(m)] for i in range(n + 1)]
for i in range(n + 1):
    DP[i][0] = A[i]
for j in range(1, m):
    for i in range(n + 1):
        DP[i][j] = DP[DP[i][j - 1]][j - 1]
i = 1
for j, b in enumerate(bit):
    if b == "1":
        i = DP[i][j]
print(i)
