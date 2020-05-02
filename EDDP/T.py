n = int(input())
S = input()
p = 10**9 + 7
DP = [[0 for j in range(n + 1)] for i in range(n + 1)]
for j in range(n):
    DP[1][j] = 1
for i in range(2, n + 1):
    A = [0]
    for j in range(n):
        A.append(A[-1] + DP[i - 1][j])
    for j in range(n - i + 1):
        if S[i - 2] == '<':
            DP[i][j] = (A[n - i + 1 + 1] - A[j + 1]) % p
        else:
            DP[i][j] = A[j + 1] % p
print(DP[n][0])
