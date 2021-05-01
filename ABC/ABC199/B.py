n = int(input())
*a, = map(int, input().split())
*b, = map(int, input().split())
ans = 0
for x in range(1, 1000 + 1):
    if all(a[i] <= x <= b[i] for i in range(n)):
        ans += 1
print(ans)
