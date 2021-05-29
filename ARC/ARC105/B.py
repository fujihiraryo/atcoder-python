from math import gcd

n = int(input())
*a, = map(int, input().split())
ans = a[0]
for i in range(n):
    ans = gcd(ans, a[i])
print(ans)
