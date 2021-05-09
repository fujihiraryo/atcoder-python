t, n = map(int, input().split())
n -= 1
lst = []
for x in range(1, 100):
    y0 = (100 + t) * x // 100
    y1 = (100 + t) * (x + 1) // 100
    if y0 + 1 != y1:
        lst.append(y0 + 1)
size = len(lst)
i, j = n // size, n % size
print(i * (100 + t) + lst[j])
