n = int(input())
*D, = map(int, input().split())
mod = 998244353
if D[0] != 0:
    print(0)
    exit()
C = {}
for d in D:
    try:
        C[d] += 1
    except BaseException:
        C[d] = 1
ans = 1
for d in D[1:]:
    try:
        ans = (ans * C[d - 1]) % mod
    except BaseException:
        ans = 0
print(ans)
