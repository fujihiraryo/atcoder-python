n = int(input())
INF = 10 ** 10
y = INF
for i in range(n):
    a, p, x = map(int, input().split())
    if x > a:
        y = min(y, p)
print(y if y < INF else -1)
