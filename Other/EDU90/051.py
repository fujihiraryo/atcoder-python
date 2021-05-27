import bisect

n, k, p = map(int, input().split())
(*a,) = map(int, input().split())
a0, a1 = a[: n // 2], a[n // 2 :]
n0, n1 = len(a0), len(a1)
l0 = [[] for _ in range(n0 + 1)]
l1 = [[] for _ in range(n1 + 1)]
for bit in range(1 << n0):
    cnt = bin(bit).count("1")
    tot = sum(a0[i] for i in range(n0) if (1 << i) & bit)
    l0[cnt].append(tot)
for bit in range(1 << n1):
    cnt = bin(bit).count("1")
    tot = sum(a1[i] for i in range(n1) if (1 << i) & bit)
    l1[cnt].append(tot)
for i in range(n0):
    l0[i].sort()
for i in range(n1):
    l1[i].sort()
ans = 0
for i in range(min(n0, k) + 1):
    j = k - i
    if not 0 <= j <= n1:
        continue
    for x in l0[i]:
        ans += bisect.bisect_right(l1[j], p - x)
print(ans)
