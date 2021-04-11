n, m = map(int, input().split())
(*x,) = map(int, input().split())
x.sort()
d = [x[i] - x[i - 1] for i in range(1, m)]
d.sort()
if n >= m:
    print(0)
else:
    print(sum(d[: m - n]))
