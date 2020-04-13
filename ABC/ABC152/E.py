from functools import reduce
import fractions
N = int(input())
* A, = map(int, input().split())
mod = 10**9+7


def gcd(a, b):
    return int(fractions.gcd(a, b))


def lcm(a, b):
    return a*b//gcd(a, b)


LCM = reduce(lcm, A)

ans = 0
for a in A:
    ans += LCM * pow(a, mod - 2, mod) % mod
print(ans % mod)
