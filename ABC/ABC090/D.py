n, k = map(int, input().split())
if k == 0:
    print(n ** 2)
    exit()
ans = 0
for b in range(1, n + 1):
    ans += (n // b) * max(0, b - k) + max(0, n % b + 1 - k)
print(ans)
