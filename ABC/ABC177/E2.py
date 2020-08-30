n = int(input())
*A, = map(int, input().split())

m = max(A)
is_prime = [True] * (m + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, m + 1):
    for j in range(i * 2, m + 1, i):
        is_prime[j] = False
primes = [i for i in range(m + 1) if is_prime[i]]

Amap = {a: 0 for a in range(1, m + 1)}
for a in A:
    Amap[a] += 1

# Pmap[p]はAにでてくるpの倍数の数
Pmap = {p: 0 for p in primes}
for p in primes:
    for a in range(p, m + 1, p):
        Pmap[p] += Amap[a]

try:
    score = max(Pmap.values())
except BaseException:
    print('pairwise coprime')
    exit()
if score == 1:
    print('pairwise coprime')
elif score != n:
    print('setwise coprime')
else:
    print('not coprime')
