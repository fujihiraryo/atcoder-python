n, k = map(int, input().split())
*p, = map(int, input().split())
p.sort()
print(sum(p[:k]))
