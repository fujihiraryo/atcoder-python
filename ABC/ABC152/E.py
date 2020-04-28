from functools import reduce
import fractions
# input()
# *A, = map(int, input().split())
A = [10**6-i for i in range(10**4)]
# A = [1000000, 999999, 999998]
p = 10**9+7


def gcd(a, b):
    return int(fractions.gcd(a, b))


def lcm(a, b):
    return a*b*pow(gcd(a, b), p-2, p)


l = reduce(lcm, A) % p
print(l)
print(sum([l*pow(a, p-2, p) for a in A]) % p)
