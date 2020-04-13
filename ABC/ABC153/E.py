def main():
    inf = 10**9
    H, N = map(int, input().split())
    AB = []
    for n in range(N):
        a, b = map(int, input().split())
        AB.append((a, b))
    AB.sort(reverse=True, key=lambda x: x[0])
    dp = [inf] * (H + 10 ** 4)
    dp[0] = 0
    for a, b in AB:
        for h in range(H):
            if dp[h] != inf:
                tmp = dp[h] + b
                if tmp < dp[h + a]:
                    dp[h + a] = tmp
    print(min(dp[H:]))


main()
