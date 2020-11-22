n = 100
DP = [[[None for z in range(n + 1)] for y in range(n + 1)] for x in range(n + 1)]
for x in range(n + 1):
    for y in range(n + 1):
        for z in range(n + 1):
            if x == n or y == n or z == n:
                DP[x][y][z] = 0


def dp(x, y, z):
    if DP[x][y][z] is not None:
        return DP[x][y][z]
    DP[x][y][z] = 1 + (
        dp(x + 1, y, z) * x + dp(x, y + 1, z) * y + dp(x, y, z + 1) * z
    ) / (x + y + z)
    return DP[x][y][z]


a, b, c = map(int, input().split())
print(dp(a, b, c))
