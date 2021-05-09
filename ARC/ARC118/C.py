MAX = 10000
n = int(input())
start = (6, 10, 15)
a = set(start)
for x in start:
    for y in range(2 * x, MAX + 1, x):
        a.add(y)
print(*list(a)[:n])
