n = int(input())
*a, = map(int, input().split())
a.sort()
ans = []
pos, neg = [], []
for i in range(n):
    if a[i] >= 0:
        pos.append(a[i])
    else:
        neg.append(a[i])
if len(pos) == 0:
    neg.sort()
    pos.append(neg.pop())
if len(neg) == 0:
    pos.sort(reverse=True)
    neg.append(pos.pop())
print(sum(pos) - sum(neg))
for _ in range(n - 1):
    x, y = pos.pop(), neg.pop()
    if len(pos) <= len(neg):
        print(x, y)
        pos.append(x - y)
    else:
        print(y, x)
        neg.append(y - x)
