n = int(input())
*A, = map(int, input().split())
inf = 10**18
# DP[i][0]=i番目まででi//2個選んだ最大値
# DP[i][1]=i番目まででi//2+1個選んだ最大値
DP = [[-inf]*2 for i in range(n)]
DP[0][0] = 0
DP[0][1] = A[0]
DP[1][0] = 0
DP[1][1] = max(A[0], A[1])
for i in range(2, n):
    if i % 2 == 0:
        DP[i][0] = max(DP[i-2][0]+A[i], DP[i-1][1])
        DP[i][1] = DP[i-2][1]+A[i]
    else:
        DP[i][0] = max(DP[i-2][0]+A[i], DP[i-1][0])
        DP[i][1] = max(DP[i-2][1]+A[i], DP[i-1][1])
if n % 2 == 0:
    print(DP[n-1][1])
else:
    print(DP[n-1][0])
