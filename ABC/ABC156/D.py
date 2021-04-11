n, a, b = map(int, input().split())
p = 10 ** 9 + 7


def comb(n, a):
    ans = 1
    for i in range(1, a + 1):
        ans = ans * (n - i + 1) * pow(i, p - 2, p) % p
    return ans


ans = (pow(2, n, p) - 1 - comb(n, a) - comb(n, b)) % p
print(ans)
