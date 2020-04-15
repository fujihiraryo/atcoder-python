n = int(input())
a, b, c = 0, 0, 0
for i in range(n):
    ai, bi, ci = map(int, input().split())
    a, b, c = ai + max(b, c), bi + max(c, a), ci + max(a, b)
print(max(a, b, c))
