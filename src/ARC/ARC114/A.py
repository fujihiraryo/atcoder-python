def prime_sieve(n):
    is_prime = [1] * n
    is_prime[0], is_prime[1] = 0, 0
    for i in range(2, n):
        if not is_prime[i]:
            continue
        for j in range(2 * i, n, i):
            is_prime[j] = 0
    return is_prime


def gcd(a, b):
    x, y = a, b
    while x:
        x, y = y % x, x
    return y


n = int(input())
*x, = map(int, input().split())
is_prime = prime_sieve(50)
p = [i for i in range(50) if is_prime[i]]
k = len(p)
ans_list = []
for s in range(1 << k):
    ans = 1
    for i in range(k):
        if (1 << i) & s:
            ans *= p[i]
    ans_list.append(ans)
ans_list.sort()
for ans in ans_list:
    if all(gcd(x[i], ans) > 1 for i in range(n)):
        print(ans)
        exit()
