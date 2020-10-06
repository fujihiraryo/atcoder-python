n = int(input())
AB = [tuple(map(int, input().split())) for i in range(n)]
X = sorted(AB, key=lambda x: x[0])
Y = sorted(AB, key=lambda x: x[1])
if n % 2 == 0:
    print((Y[n // 2 - 1][1] + Y[n // 2][1]) - (X[n // 2 - 1][0] + X[n // 2][0]) + 1)
else:
    print(Y[n // 2][1] - X[n // 2][0] + 1)
