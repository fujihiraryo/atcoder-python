n, k = map(int, input().split())
cnt = [0] * k
for i in range(1, n + 1):
    cnt[i % k] += 1
ans = 0
for a in range(1, n + 1):
    if 2 * a % k == 0:
        ans += cnt[-a % k] ** 2
print(ans)
