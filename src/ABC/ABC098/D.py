n = int(input())
*a, = map(int, input().split())
x, y = 0, 0
j = 0
ans = 0
for i in range(n):
    while j < n and (x + a[j]) == (y ^ a[j]):
        x += a[j]
        y ^= a[j]
        j += 1
    ans += j - i
    x -= a[i]
    y ^= a[i]
print(ans)
