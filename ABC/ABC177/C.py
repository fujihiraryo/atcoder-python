n = int(input())
*A, = map(int, input().split())
MOD = 10**9 + 7
x = ((sum(A) % MOD)**2) % MOD
y = sum(a**2 % MOD for a in A) % MOD
print(((x - y) % MOD) * pow(2, MOD - 2, MOD) % MOD)
