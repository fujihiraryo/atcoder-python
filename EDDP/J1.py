# n = int(input())
# *A, = map(int, input().split())


def main():
    n = 300
    A = [3] * n
    a, b, c = A.count(1), A.count(2), A.count(3)
    DP = [[[None for k in range(n + 1)] for j in range(n + 1)]
          for i in range(n + 1)]
    DP[0][0][0] = 0.0

    def dp(i, j, k):
        if i < 0 or j < 0 or k < 0:
            return 0.0
        if DP[i][j][k] is not None:
            return DP[i][j][k]
        DP[i][j][k] = (n + dp(i - 1, j, k) * i + dp(i + 1, j - 1, k)
                       * j + dp(i, j + 1, k - 1) * k) / (i + j + k)
        return DP[i][j][k]

    print(dp(a, b, c))


main()
