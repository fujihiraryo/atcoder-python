n = int(input())
xyh = [tuple(map(int, input().split())) for _ in range(n)]
for cx in range(0, 100 + 1):
    for cy in range(0, 100 + 1):
        h_set = set()
        for i in range(n):
            xi, yi, hi = xyh[i]
            dist = abs(xi - cx) + abs(yi - cy)
            h_set.add(hi + dist)
        for h in h_set:
            flag = True
            for i in range(n):
                xi, yi, hi = xyh[i]
                dist = abs(xi - cx) + abs(yi - cy)
                if hi != max(h - dist, 0):
                    flag = False
            if flag:
                print(cx, cy, h)
                exit()
