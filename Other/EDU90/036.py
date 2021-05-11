n, q = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(n)]
max_plus = max(x + y for x, y in lst)
max_minus = max(x - y for x, y in lst)
min_plus = min(x + y for x, y in lst)
min_minus = min(x - y for x, y in lst)
for _ in range(q):
    i = int(input()) - 1
    x, y = lst[i]
    plus, minus = x + y, x - y
    print(
        max(
            abs(plus - max_plus),
            abs(plus - min_plus),
            abs(minus - max_minus),
            abs(minus - min_minus),
        )
    )
