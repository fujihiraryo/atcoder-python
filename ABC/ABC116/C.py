n = int(input())
(*h,) = map(int, input().split())
h.append(0)
ans = 0
while max(h) > 0:
    cnt = 0
    for i in range(n):
        if h[i] != 0 and h[i + 1] == 0:
            cnt += 1
    ans += cnt
    for i in range(n + 1):
        h[i] = max(0, h[i] - 1)
print(ans)
