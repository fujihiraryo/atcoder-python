MOD = 10 ** 9 + 7
h, w = map(int, input().split())
S = [input() for i in range(h)]
A = [[0] * w for i in range(h)]
tate = [[0] * w for i in range(h)]
yoko = [[0] * w for i in range(h)]
nana = [[0] * w for i in range(h)]
for i in range(h):
    for j in range(w):
        if S[i][j] == "#":
            tate[i][j] = 0
            yoko[i][j] = 0
            nana[i][j] = 0
            A[i][j] = 0
            continue
        if i == 0 and j == 0:
            A[i][j] = 1
            tate[i][j] = 1
            yoko[i][j] = 1
            nana[i][j] = 1
            continue
        if i > 0:
            A[i][j] = (A[i][j] + tate[i - 1][j]) % MOD
        if j > 0:
            A[i][j] = (A[i][j] + yoko[i][j - 1]) % MOD
        if i > 0 and j > 0:
            A[i][j] = (A[i][j] + nana[i - 1][j - 1]) % MOD
        tate[i][j] = A[i][j]
        yoko[i][j] = A[i][j]
        nana[i][j] = A[i][j]
        if i > 0:
            tate[i][j] = (tate[i][j] + tate[i - 1][j]) % MOD
        if j > 0:
            yoko[i][j] = (yoko[i][j] + yoko[i][j - 1]) % MOD
        if i > 0 and j > 0:
            nana[i][j] = (nana[i][j] + nana[i - 1][j - 1]) % MOD
print(A[h - 1][w - 1])
