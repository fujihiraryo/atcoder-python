h, w, k = map(int, input().split())
# h, w, k = 15, 8, 5
# h, w, k = 2, 3, 1
# h, w, k = 2, 3, 3
# h, w, k = 1, 3, 2
p = 10**9+7
# DP[i][j]=i段目まで見て0からjに着くパターン数
# 最終的にDP[h][k-1]を求める
DP = [[0 for j in range(w+1)] for i in range(h+1)]
DP[0][0] = 1
F = [1, 1, 2, 3, 5, 8, 13, 21]
for i in range(h):
    for j in range(w):
        a = DP[i][j-1]*F[j-1]*F[w-1-j]
        b = DP[i][j+1]*F[j]*F[w-2-j]
        c = DP[i][j]*F[j]*F[w-1-j]
        DP[i+1][j] = (a+b+c) % p
print(DP[h][k-1])
