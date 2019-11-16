N = int(input())
h = list(map(int, input().split()))
dp = [10 ** 10] * N
# dp[n]はあとnのところからのN-1に行くのに支払うコストの最小値
dp[0] = 0
dp[1] = abs(h[N-1]-h[N-2])
for n in range(0, N-2):
    dp[n+2] = min(dp[n+1]+abs(h[(N-1)-(n+2)]-h[(N-1)-(n+1)]),
                  dp[n]+abs(h[(N-1)-(n+2)]-h[(N-1)-n]))
print(dp[N-1])
