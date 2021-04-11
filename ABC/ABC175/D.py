INF = 10 ** 10
n, k = map(int, input().split())
(*p,) = map(lambda x: int(x) - 1, input().split())
(*c,) = map(int, input().split())
ans = -INF
for i in range(n):
    arr = []
    cur = i
    cnt = 0
    for _ in range(k):
        cur = p[cur]
        arr.append(c[cur])
        cnt += 1
        if cur == i:
            break
    cum = [0] * (cnt + 1)
    for j in range(cnt):
        cum[j + 1] = cum[j] + arr[j]
    if cnt == k or cum[-1] < 0:
        ans = max(ans, max(cum[1:]))
        continue
    q, r = divmod(k, cnt)
    ans = max(ans, cum[-1] * q + max(cum[: r + 1]), cum[-1] * (q - 1) + max(cum))
print(ans)
