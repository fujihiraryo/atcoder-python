S = list(input())
S.reverse()
N = len(S)
mod = 10 ** 9 + 7
ans = [[0 for r in range(13)] for n in range(N)]
if S[0] == '?':
    ans[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
else:
    ans[0][int(S[0])] = 1
for n in range(1, N):
    if S[n] == '?':
        for r in range(13):
            count = 0
            for d in range(10):
                r1 = d * (10 ** n) % 13
                r0 = (r - r1) % 13
                count += ans[n - 1][r0] % mod
            ans[n][r] = count % mod
    else:
        for r in range(13):
            d = int(S[n])
            r1 = d * (10 ** n) % 13
            r0 = (r - r1) % 13
            ans[n][r] = ans[n-1][r0] % mod
print(ans[N-1][5])
