n, m = map(int, input().split())
l0, r0 = 1, n
for j in range(m):
    l1, r1 = map(int, input().split())
    l0 = max(l0, l1)
    r0 = min(r0, r1)
print(max(0, r0-l0+1))
