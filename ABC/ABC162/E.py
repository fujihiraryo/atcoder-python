n, k = map(int, input().split())
mod = 10 ** 9 + 7
A = {}
# A[i]=最大公約数がiであるような配列の個数
ans = 0
for i in range(k, 0, -1):
    A[i] = pow(k // i, n, mod)
    # 最大公約数が2i,3i,...の個数を引く
    for j in range(2 * i, k + 1, i):
        A[i] -= A[j]
    ans = (ans + A[i] * i) % mod
print(ans)
