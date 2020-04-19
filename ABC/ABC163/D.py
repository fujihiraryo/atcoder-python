n, k = map(int, input().split())
# n, k = 3, 2
# n, k = 141421, 35623
p = 10**9+7
s = 0
for l in range(k, n+1+1):
    s = (s+(n+1)*l-l**2+1) % p
print(s)
