n = int(input())
*H, = map(int, input().split())
DP = [0 for i in range(n)]
DP[1] = abs(H[0] - H[1])
for i in range(2, n):
    DP[i] = min(DP[i - 2] + abs(H[i] - H[i - 2]),
                DP[i - 1] + abs(H[i] - H[i - 1]))
print(DP[n - 1])
