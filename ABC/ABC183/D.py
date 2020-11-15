n, w = map(int, input().split())
lst = [tuple(map(int, input().split())) for i in range(n)]
lst.sort()
m = 2 * 10 ** 5 + 1
box = [0] * m
for s, t, p in lst:
    box[s] += p
    box[t] -= p
cum = [0] * m
cum[0] = box[0]
for i in range(1, m):
    cum[i] = cum[i - 1] + box[i]
if all(x <= w for x in cum):
    print("Yes")
else:
    print("No")
