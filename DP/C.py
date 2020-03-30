N = int(input())
a, b, c = 0, 0, 0
for n in range(N):
    an, bn, cn = map(int, input().split())
    a, b, c = an + max(b, c), bn + max(c, a), cn + max(a, b)
print(max(a, b, c))
