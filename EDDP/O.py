def main():
    n = int(input())
    A = [list(map(int, input().split())) for i in range(n)]
    p = 10 ** 9 + 7
    DP = [0 for s in range(1 << n)]
    DP[0] = 1
    for s in range(1, 1 << n):
        lng = bin(s).count("1")
        for i in range(n):
            if ((1 << i) & s) * A[lng - 1][i]:
                DP[s] += DP[~(1 << i) & s]
                DP[s] %= p
    print(DP[(1 << n) - 1])


main()
