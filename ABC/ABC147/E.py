def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = [list(map(int, input().split())) for _ in range(h)]
    c = [[a[i][j] - b[i][j] for j in range(w)] for i in range(h)]
    dp = [[set() for j in range(w)] for i in range(h)]
    dp[0][0].add(abs(c[0][0]))
    for i in range(h):
        for j in range(w):
            if i > 0:
                for k in dp[i - 1][j]:
                    dp[i][j].add(abs(k + c[i][j]))
                    dp[i][j].add(abs(k - c[i][j]))
            if j > 0:
                for k in dp[i][j - 1]:
                    dp[i][j].add(abs(k + c[i][j]))
                    dp[i][j].add(abs(k - c[i][j]))
    print(min(dp[h - 1][w - 1]))


main()
